import pandas as pd
import scipy.stats as st
import math

#1000 population & 281 in favor

n = 1000
samp_n = 281

samp_proportion = samp_n / n

print(samp_proportion)

#what is margin of error for 90% conf interv
#z-value @ 90 1.645 
marg_err_90 = 1.645 * math.sqrt(samp_proportion * (1 - samp_proportion) / n )
print('Margin of error at 90% Confidence Level is', marg_err_90)

#zvalue @95 1.960 
marg_err_95 = 1.960 * math.sqrt(samp_proportion * (1 - samp_proportion) / n )
print('Margin of error at 95% Confidence Level is', marg_err_95)

conf_interv_95_low = samp_proportion - marg_err_95
conf_interv_95_high = samp_proportion + marg_err_95
print('Confidence Interval of 95% is', conf_interv_95_low, 'to', conf_interv_95_high)