import pandas as pd
import scipy.stats as st
import math

#addtl growth of plants in week recorded for 11 plants
#st dev of 3
#sample mean of 8 inches
#t* at 0.05 significance is 2.228

n = 11
stdev = 3
t = 2.228
df = n - 1
mean = 8

#margin error
marg_error = t * (stdev/math.sqrt(n))

#standard error 
std_err = stdev/math.sqrt(n)
#confidence interval

print('Margin of Error is', marg_error)
print('Confidence Interval',
st.t.interval(0.95, df, mean, std_err))