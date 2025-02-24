import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())

sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", style="time")

plt.savefig('scatterplot.png')
plt.show()