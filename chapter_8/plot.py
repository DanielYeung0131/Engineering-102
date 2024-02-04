import matplotlib.pyplot as plt

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

x_values = [1,2,3,4,5,6,7]
y = [800,600,900,300,700,950,400]

plt.figure(layout='constrained')
plt.plot(x_values,y, marker ='o', linestyle='--',color='k', markersize=5)
plt.title('Frodo')
plt.xlabel('Day of week')
plt.ylabel('Walking distance')
plt.xticks(x_values,days)

plt.show()