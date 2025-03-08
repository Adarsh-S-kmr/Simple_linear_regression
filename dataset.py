import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

temperature=np.linspace(15,40,100) # generates temeprature values between 15C to 40C
sales=50 + 7 * (temperature-10) + np.random.normal(0,20,size=len(temperature)) #creates linear relation with sales and temperature
sales=np.maximum(sales, 10)# non negative sales
df=pd.DataFrame({"Temperature": temperature, "Ice_Cream_Sales": sales})# save dataset
df.to_csv("sales.csv", index=False)

# Plot the data
plt.figure(figsize=(8,5))
plt.scatter(temperature, sales,color='black',label="Data")
plt.plot(temperature, 50 + 7 * (temperature-10),color='red',label="Expected Trend",linewidth=2)
plt.xlabel("Temperature (°C)")
plt.ylabel("Ice Cream Sales")
plt.title("Ice Cream Sales vs Temperature")
plt.xlim(10,45)
plt.ylim(0,max(sales)+50)
plt.legend()
plt.show()

print("dataset saved as sales.csv")
