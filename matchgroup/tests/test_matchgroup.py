import os
import pdb
import sys
import time
import pytest

import numpy as np
import pandas as pd

from ..matchgroup import gower, match


@pytest.fixture
def example_pheno():
    """
    Example of phenotype data
    """

    np.random.seed(42)

    n_participants = 200
    dx_participants = int(.3 * n_participants)
    tc_participants = int(.7 * n_participants)

    age = np.concatenate([
        (40 + 5 * np.random.normal(size=dx_participants)),
        (45 + 10 * np.random.normal(size=tc_participants)),
    ])

    sex = np.concatenate([
        np.random.choice(['M', 'F'], dx_participants, p=(.4, .6)),
        np.random.choice(['M', 'F'], tc_participants, p=(.6, .4)),
    ])

    group = (['DX'] * dx_participants) + (['TC'] * tc_participants)

    random_id = np.random.randint(50000, 90000)

    participants = pd.DataFrame({
        'age': age,
        'sex': sex,
        'group': group,
        'external_id': random_id,
    })

    participants['sex'] = participants['sex'].astype('category')
    participants['group'] = participants['group'].astype('category')

    return participants


def test_gower(example_pheno):
    distance = gower(example_pheno, ['age'], ['sex'])
    assert np.all(np.diag(distance) == 0.0)


def test_matchgroup(example_pheno):
    matched_pheno = match(example_pheno, 'group', ['age', 'sex'])
    count_per_group = matched_pheno.group.value_counts().values

    assert len(count_per_group) == 2
    assert np.all(count_per_group == count_per_group[0])
