import numpy as np
import pytest
from maxima import find_maxima
    
seed = 42
np.random.seed(seed)
y = np.floor(np.random.rand(2,10)) 
y = y.ravel()

y[5] = y[5] + 10

exp = [5]

test_cases = [(y,exp)]
@pytest.mark.parametrize("inp,exp",test_cases)    
def  test_all(inp,exp):
        out=find_maxima(inp)
        assert exp == out
# additional tests for
# - max on both borders
#   x = [4, 2, 1, 3, 1, 2]
# - max on both borders, absolute max on right border
#   x = [4, 2, 1, 3, 1, 5]
# - one max (absolute) on left border
#   x = [4, 2, 1, 3, 1]
# - plateau
#   x = [1, 2, 2, 1]
#   (decide for a sensible output in this case)
# - test cases for plateau
#   x = [1, 2, 2, 3, 1]
#   x = [1, 3, 2, 2, 1]
#   x = [3, 2, 2, 3]
