from matplotlib import pyplot as plt
import numpy as np

plt.style.use('ggplot')

minutes = list(np.arange(1,10))

player1 = [1,2,3,3,4,4,4,4,5]
player2 = [1,1,1,1,2,2,2,3,4]
player3 = [1,1,1,2,2,2,3,3,3]

# plt.pie([1,1,1], labels=['p1','p2','p3'])
labels = ['p1','p2','p3']
colors = ['#6EFF88', '#6EB2FF', '#B982FF', '#AFAFAF']
plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

plt.title('stack plot')
plt.tight_layout()
plt.legend(loc='upper left')
plt.savefig('model')
plt.show()





