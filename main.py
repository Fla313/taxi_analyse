### Kleine Taxis Analyse
### Kleiner Testzweig

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("taxis")
sns.histplot(data=df, x="tip", hue="pickup_borough")

plt.show()