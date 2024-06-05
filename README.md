# Comparative Judgement

A package for comparative judgement (CJ).


Importing the BCJ model:

```python
from cj.models import BayesianCJ

BCJ = BayesianCJ(4)
```

Creating the data:

```python
import numpy as np

data = np.asarray([
    [0, 1, 0],
    [0, 1, 0],
    [0, 3, 0],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 2, 1],
    [1, 2, 1],
    [1, 2, 1],
    [1, 2, 1],
    [1, 2, 1],
    [2, 1, 2],
    [2, 1, 2],
    [2, 1, 2],
    [2, 3, 2],
    [3, 0, 3],
    [3, 0, 3],
    [3, 0, 3],
    [3, 0, 3],
    [3, 2, 3],
    [3, 2, 3],
    [3, 2, 3],
])
```

running the model:

```python
BCJ.run(data)
```

Finding the $\mathbb{E}[\mathbf{r}]$
```python
BCJ.rank_scores
>>> [3.046875, 2.09765625, 3.05859375, 1.796875]
```
