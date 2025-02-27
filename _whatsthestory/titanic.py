import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset("titanic")

survivors = titanic.groupby("class")["alive"].value_counts().unstack(level=0)
print(survivors)

plot_surv= survivors.plot(kind="bar",
title="Survivors",
color=["orange", "magenta", "blue"],
ec="black",
xlabel="",
# stacked=True
);

for container in plot_surv.containers:
    plot_surv.bar_label(container)
plt.show()