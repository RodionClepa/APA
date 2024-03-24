
x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000] 
# BFS
# y = ['0.0000', '0.0000', '0.0163', '0.0762', '0.0082', '0.0000', '0.0206', '0.5041', '0.0923', '0.4447', '1.1379', '0.2955', '3.3274', '0.3365', '0.2496', '1.1738', '4.6009', '0.0083', '0.5610', '0.0345']
# DFS
y = ['0.0000', '0.0080', '0.0160', '0.0665', '0.0001', '0.0000', '0.0118', '0.4437', '0.0809', '0.4108', '1.0232', '0.2577', '3.0382', '0.3026', '0.2359', '1.0927', '4.0958', '0.0000', '0.5077', '0.0285']
y = [float(i) for i in y]
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(x)
ypoints = np.array(y)

plt.plot(xpoints, ypoints, marker = 'o')
plt.title("DFS")
plt.xlabel("N")
plt.ylabel("Time(s)")
plt.grid()
plt.show()