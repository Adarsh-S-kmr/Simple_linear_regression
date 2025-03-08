import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('sales.csv')  #read dataset

def loss_function(m,b,points):  #Loss function (Mean squared error) measures how far the predicted line is from actual data
    total_error=0
    for i in range(len(points)):
        x=points.iloc[i].Temperature
        y=points.iloc[i].Ice_Cream_Sales

        total_error+=(y-(m * x + b)) ** 2
    return total_error/float(len(points))

def gradient_descent(m_now, b_now, points, L):  # Optimization algorithm
    m_grad=0
    b_grad=0
    n=len(points)

    for i in range(n):
        x=points.iloc[i].Temperature
        y=points.iloc[i].Ice_Cream_Sales

        m_grad+=(-2/n) * x * (y - (m_now * x + b_now))
        b_grad+=(-2/n) * (y - (m_now * x + b_now))

    m=m_now - m_grad * L
    b=b_now - b_grad * L
    return m, b



m=0
b=0 
L=0.001
epochs=1000

for i in range(epochs):
    if i%50==0:
        print(f"epoch:{i}")
    m,b=gradient_descent(m , b , data ,L)
print(m,b)

#poltting the result
plt.scatter(data.Temperature,data.Ice_Cream_Sales,color="black")
plt.plot(data.Temperature, [m * x + b for x in data.Temperature], color="red")
plt.show()
