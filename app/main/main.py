import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the dataset in pandas dataframe
df = pd.read_csv('performance_tests_data.csv', header=0)
df.columns = ['timestamp', 'avgRT', 'p90', 'throughput', 'latency']

# understanding the data
print(df.head())

# understanding the shape
print(df.shape)

# data points for each class label
print(df['p90'].value_counts())

# general statistical analysis
print(df.describe())

# distribution plot to map p90 across different timestamps
sns.FacetGrid(df, hue="timestamp").map(sns.histplot, "p90").add_legend()
plt.show()

# joint plot
sns.jointplot(x="timestamp", y="p90", data=df)
plt.show()