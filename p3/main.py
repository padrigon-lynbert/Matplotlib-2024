from matplotlib import pyplot as plt

plt.style.use('ggplot')

# slices = [120,80,30,20]
# labels = ['reits', 'bonds', 'stocks', 'cash']
# colors = ['#6EFF88', '#6EB2FF', '#B982FF', '#AFAFAF']



# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.1,0]



plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, 
        autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})







plt.title('pie chart')
plt.tight_layout()
plt.savefig('model.png')
plt.show()

