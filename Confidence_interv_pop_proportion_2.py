import pandas as pd
import scipy.stats as st
import math

#poll report .36 approval rating and margin of error .01

p = .36
marg_err = .01

#how many voters sampled at 90% confidence interval
conf = .9
z = 1.645
#calculate n

n = ((z/marg_err) ** 2) * (p * (1 - p))

print (n)

#how many voters sampled at 95% confidence interval
conf = .95
z = 1.960
n = ((z/marg_err) ** 2) * (p * (1 - p))

print (n)

#how many voters should be sampled at 95% confidence interval if no previous estimates are given 
p = 0.5
n = ((z/marg_err) ** 2) * (p * (1 - p))

print (n)

#in a poll of 1000 randomly selected voters in a local election 497 voters were against school bond measures
p = 497/1000
n = 1000
#margin of error @ 99% conf level
c = .99
z = 2.576
marg_err = z * math.sqrt((p * ( 1 - p)) / n)
print("sample proportion is", p)
print("margin of error is", marg_err)

#in a poll of 1000 randomly selected voters in a local election 907 voters were against school bond measures
p = 907/1000
n = 1000
#what is 90% confidence interval
conf = .9
z = 1.645
marg_err = z * math.sqrt((p * ( 1 - p)) / n)
print(marg_err)
print("confidence interval [", p - marg_err, ", ", p + marg_err)

#a poll reported 55% support for a statewide election witha  margin of error of 2.84 percentage points
p = .55
marg_err = .0284
#how many voters should be sampled for a 95% confidence interval
conf = .95
z = 1.960
n = ((z/marg_err) ** 2) * (p * (1 - p))

print (n)

#statewide election has margin of error of 2.32 percentage points
marg_err = .0232
#how many voters should be sampled at 95% confidence interval  round up assume p = 0.5
p = 0.5
n = ((z/marg_err) ** 2) * (p * (1 - p))

print (n)
