# loads the seaborn library
import seaborn as sns

# loads the titanic dataset 
titanic = sns.load_dataset("titanic")
titanic.columns
titanic.age.min()