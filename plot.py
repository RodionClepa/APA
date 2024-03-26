
x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000] 
# BFS
# y = [0.00010209083557128906, 0.0020752429962158205, 0.004286503791809082, 0.006279706954956055, 0.00723416805267334, 0.01127769947052002, 0.016883111000061034, 0.02193140983581543, 0.02773587703704834, 0.03535020351409912, 0.04472362995147705, 0.050635147094726565, 0.05900332927703857, 0.07396759986877441, 0.08294591903686524, 0.09126687049865723, 0.10748343467712403, 0.11488161087036133, 0.12775108814239503, 0.13991167545318603]# DFS
y = [1.0209083557128906e-05, 0.00020752429962158205, 0.0004286503791809082, 0.0006279706954956055, 0.000723416805267334, 0.001127769947052002, 0.0016883111000061033, 0.002193140983581543, 0.002773587703704834, 0.0035350203514099123, 0.004472362995147705, 0.005063514709472657, 0.005900332927703858, 0.007396759986877441, 0.008294591903686524, 0.009126687049865722, 0.010748343467712402, 0.011488161087036134, 0.012775108814239503, 0.013991167545318603]
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