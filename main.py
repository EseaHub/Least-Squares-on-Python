import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filePath = 'dataset.xlsx' 
data = pd.read_excel(filePath)
print(data, '\n')


x = np.array(data['x'])
y = np.array(data['y'])
N = len(x)

a1 = np.dot(x.T ,y)/N
a2 = np.dot(x.T, x)/N
mx = x.sum()/N
my = y.sum()/N

k = (a1-mx*my)/(a2-mx**2)
b = my - k*mx

xMax = np.max(x)
xMin = np.min(x)
f = np.array([k*(xMin-5)+b, k*xMin+b, k*xMax+b, k*(xMax+5)+b])
X = np.array([xMin-5, xMin, xMax, xMax+5])

plt.plot(X, f, c='blue')
plt.scatter(x, y, c = 'red', s=5)
plt.grid(True)
plt.show()
