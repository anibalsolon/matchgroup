import numpy as np
import pandas as pd

# https://github.com/cran/e1071/blob/master/man/matchControls.Rd
# https://stat.ethz.ch/education/semesters/ss2012/ams/slides/v4.2.pdf


def gower(df, numerical_columns, categorical_columns):
    # https://github.com/scikit-learn/scikit-learn/pull/9555/files

    df_cat = np.array(df[categorical_columns])
    df_num = np.array(df[numerical_columns])

    df_num_max = df_num.max(axis=0)
    df_num_range = np.nan_to_num(1 - df_num.min(axis=0) / df_num_max)
    df_num = np.nan_to_num(df_num / df_num_max)

    cat_distance = np.apply_along_axis(
        lambda row: row != df_cat, axis=1, arr=df_cat).sum(axis=2)

    num_distance = (np.apply_along_axis(
        lambda row: np.abs(row - df_num), axis=1, arr=df_num) /
                    df_num_range).sum(axis=2)

    distance = cat_distance + num_distance
    distance /= float(len(categorical_columns) + len(numerical_columns))

    return distance


def distance_selection(group, group_distance):

    # TODO pareto sort, multi optimimzing for several lesser-group participants
    samples = group.index.copy()
    selections = group.index[0:0]

    for lesser in range(group_distance.shape[0]):
        sel = group_distance[lesser].argmin()
        others = list(set(range(len(samples))) - set([sel]))

        selections = selections.union(samples[sel:sel + 1])
        group_distance = group_distance[:, others]
        samples = samples[others]

    return selections


def match(data, target_variable, comparison_variables=None):

    if isinstance(target_variable, pd.Series):
        target_variable = target_variable.name

    if comparison_variables is not None:
        columns = list(set(comparison_variables + [target_variable]))
        sub_data = data[columns].copy()
    else:
        sub_data = data.copy()

    if sub_data.isnull().values.any():
        raise ValueError("This method does not support missing values.")

    target = sub_data[target_variable]

    columns = sub_data.columns
    numerical = [
        c for c in columns if pd.api.types.is_numeric_dtype(sub_data[c].dtype)
    ]
    categorical = [c for c in columns if c not in numerical]

    # TODO optimize, just compute distance from lesser group
    distance = gower(data, numerical, categorical)

    sub_data['reference'] = np.arange(distance.shape[0])

    group_count = target.value_counts()
    lesser_target = min(group_count.index, key=group_count.get)
    lesser_group = sub_data[target == lesser_target]
    other_groups = sub_data.loc[sub_data.index.difference(lesser_group.index)]

    final_population = lesser_group.index.copy()

    distance = distance[lesser_group.reference.tolist()]

    for _, group in other_groups.groupby(target.name):

        if not len(group):
            continue

        group_distance = distance[:, group.reference.tolist()]
        selections = distance_selection(group, group_distance)
        final_population = final_population.union(selections)

    return data.loc[final_population]
