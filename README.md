# Matchgroup

Find matched groups on your dataset!

It looks for the smallest group from your dataset, and matches the number of participants based on a Gower dissimilarity matrix from variables of your dataset (e.g. age and sex).


```python
import pandas as pd
import numpy as np

import matchgroup

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
})

participants['sex'] = participants['sex'].astype('category')
participants['group'] = participants['group'].astype('category')

matched_participants = matchgroup.match()
matched_participants.groupby(['group']).agg(['count'])
>>>         age   sex
>>>       count count
>>> group
>>> DX       60    60
>>> TC       60    60

matched_pheno.groupby(['group']).agg(['mean'])
>>>              age
>>>             mean
>>> group
>>> DX     39.226727
>>> TC     39.754736

matched_pheno.groupby(['group', 'age']).agg(['count'])
>>>             age
>>>           count
>>> group sex
>>> DX    F      38
>>>       M      22
>>> TC    F      38
>>>       M      22

```