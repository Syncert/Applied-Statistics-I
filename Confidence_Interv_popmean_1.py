import pandas as pd
import scipy.stats as st
import math

#list of student heights
student_heights = [67,71,72,73,60,67,68,61,73]

height_df = pd.DataFrame(student_heights, columns=['student_height'])
#std
std = 2
#calculate Mean & count
mean = height_df['student_height'].mean()
count = height_df['student_height'].count()
#standard error & margin of error @95
z_val = 1.960
stand_err = round(std/(math.sqrt(count)),4)
marg_err = round(z_val * std/(math.sqrt(count)),4)
#degree of freedom
n = count - 1

#print dataframe
print(height_df)
print()

#print mean, margin of error value
print('Mean is', mean)
print('Standard error is', stand_err)
print('Margin of error is', marg_err)

#print confidence interval
print('Confidence interval is', 
st.norm.interval(0.95, mean, stand_err))