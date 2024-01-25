import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('ggplot')
df = pd.read_csv('p5/data.csv')

ages = df['Age']
dev_salaries = df['All_Devs']
py_salaries = df['Python']
js_salaries = df['JavaScript']

plt.plot(ages, dev_salaries, color='gray', linestyle='--', label='all')
plt.plot(ages, py_salaries, color='#76CBFF', linestyle='-', label='python')

overall_median = 57287
plt.fill_between(ages, py_salaries, overall_median, where=(py_salaries>overall_median), interpolate=True, color='#26FF0C', alpha=0.25, label='above avg')
plt.fill_between(ages, py_salaries, overall_median, where=(py_salaries<=overall_median), interpolate=True, color='blue', alpha=0.25, label='avg')
plt.fill_between(ages, py_salaries, overall_median, where=(py_salaries<=40000), interpolate=True, color='red', alpha=0.25, label='below avg')

plt.title("dev salaries USD")
plt.legend(loc=2)

plt.savefig('model.png')
plt.show()