import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

kk=0.5
bb=2
input_data = {"x" : np.arange(80),
              "y" : np.array([kk*z+bb for z in range (80)]) + np.random.normal(0, 3, 80)}

data = pd.DataFrame(input_data)
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
plt.plot(np.array([kk*z+bb for z in range (80)]), c = 'red')
plt.scatter(x, y, c = 'red', s=5)
plt.grid(True)
plt.show()
