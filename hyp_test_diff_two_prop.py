import pandas as pd
import scipy as sp
import math
from statsmodels.stats.proportion import proportions_ztest



#populations
pop_1 = 5000
pop_2 = 5000
#success of populations
succ_1 = 95
succ_2 = 125
# proportions
prop_1 = succ_1 / pop_1
prop_2 = succ_2 / pop_2
prop_all = (succ_1 + succ_2) / (pop_1 + pop_2)
print('Proportion 1 is', prop_1)
print('Proportion 2 is', prop_2)
print('Proportion of entire group is', prop_all)

#Standard error estimate
stand_err = math.sqrt(prop_all * (1 - prop_all) * ((1 / pop_1) + (1 / pop_2)) )
print('Standard Error is', stand_err)

#individuals meeting criteria
counts = [succ_1, succ_2]
#total number of individuals
n = [pop_1, pop_2]

z_test_script = proportions_ztest(counts,n)
print('Z-Score is (z-score & two-tail p value)', z_test_script)