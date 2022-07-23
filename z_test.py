from statsmodels.stats.weightstats import ztest
import pandas as pd
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')
print(ztest(x1 = scores['Exam1'],  value = 86))

from statsmodels.stats.proportion import proportions_ztest
counts = 161
nobs = 275
value = .54
print(proportions_ztest(counts, nobs, value, prop_var = value))
