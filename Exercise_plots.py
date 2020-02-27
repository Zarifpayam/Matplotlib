import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\User\\Desktop\\insurance.csv', header=0)

#1
plt.plot(df['charges'])
plt.show()
plt.savefig('C:\\Users\\User\\Desktop\\charges_plot.png',dpi=300)
plt.close()

#2
plt.hist(df['bmi'])
plt.show()
plt.savefig('C:\\Users\\User\\Desktop\\bmi_hist.png',dpi=300)
plt.close()

#3 and 4
plt.scatter(df['age'],df['charges'])
plt.xlabel('age')
plt.ylabel('charges')
plt.show()
plt.savefig('C:\\Users\\User\\Desktop\\age_charge_scatter.png',dpi=300)
plt.close()

#5- It needs further investigation, as there seems to be a high correlation between the two on the chart
#the previous exercise showed a mere 0.299
