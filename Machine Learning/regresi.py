import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from WildanML import Regression

# =============================== Regresi Linier ======================================

print('\n' + 15*'=' + ' Regresi Linier ' + 15*'=')
regresi = Regression()
data = pd.read_csv('../Dataset/dataRegresi.txt')
x = np.array(data['Biaya Iklan'])
y = np.array(data['Tingkat Penjualan'])
yPred = regresi.linearRegression(x, y, len(x), x)
data['Tingkat Penjualan (Predict)'] = yPred
error = abs(y-yPred)
data['Error'] = error
print(data)

# Visualization
plt.figure('Visualisasi Data')
plt.scatter(x, y)
plt.plot(x, yPred, 'r')
plt.title('Regresi Linier')
plt.xlabel('Biaya Iklan')
plt.ylabel('Tingkat Penjualan')
plt.show()

# Evaluation
print('Mean Absolute Error      :', regresi.meanAbsoluteError(y, yPred))
print('Mean Squared Error       :', regresi.meanSquaredError(y, yPred))
print('Root Mean Squared Error  :', regresi.rootMeanSquaredError(y, yPred))

# Prediction
xPred = 65
yPred = regresi.linearRegression(x, y, len(x), xPred)
print('Hasil Prediksi: ', yPred)

# =========================== Regresi Linier Berganda =================================

print('\n' + 15*'=' + ' Regresi Linier Berganda ' + 15*'=')

# Restructuring data
data = pd.read_csv('../Dataset/dummyMultiRegresi.csv')
data['Attendance'] = data['Attendance'].map({'Yes':1, 'No':0})
data = data[['SAT', 'Attendance', 'GPA']] # swap column position

x = np.array((data['SAT'], data['Attendance']))
y = np.array(data['GPA'])
gpaPred = regresi.multiLinearRegression(x[0], x[1], y, x[0], x[1])
data['GPA Prediction'] = gpaPred # add new column
error = abs(data['GPA'] - data['GPA Prediction'])
data['Error'] = error
print(data)

# Selecting data with specific Attendance
dataYes = data.loc[data['Attendance'] == 1]
dataNo = data.loc[data['Attendance'] == 0]

# Visualization
plt.figure('Visualisasi Data')
plt.scatter(data['SAT'], data['GPA'], c=data['Attendance'])
plt.plot(dataYes['SAT'], dataYes['GPA Prediction'], 'yellow')
plt.plot(dataNo['SAT'], dataNo['GPA Prediction'], 'purple')
plt.title('Regresi Linier Berganda')
plt.xlabel('SAT')
plt.ylabel('GPA')
plt.show()

# Evaluation
print('Mean Absolute Error      :', regresi.meanAbsoluteError(data['GPA'], data['GPA Prediction']))
print('Mean Squared Error       :', regresi.meanSquaredError(data['GPA'], data['GPA Prediction']))
print('Root Mean Squared Error  :', regresi.rootMeanSquaredError(data['GPA'], data['GPA Prediction']))

# Prediction
xPred = np.array([(1700,0), (1670,1)])
yPred = []
yPred.append(regresi.multiLinearRegression(x[0], x[1], y, xPred[:,0], xPred[:,1]))
print('Hasil Prediksi:', yPred)

# =========================== Interpolasi Lagrange =================================

print('\n' + 15*'=' + ' Interpolasi Lagrange ' + 15*'=')

data = pd.read_csv('../Dataset/dataLagrange.txt')
x = np.array(data['X'])
y = np.array(data['Y'])
yPred = np.array([])
for i in x:
    yPred = np.append(yPred, regresi.lagrange(x,y,i))

error = abs(y-yPred)
print('Error:', error)

# Visualization
plt.figure('Visualisasi Data')
plt.scatter(x,y)
plt.plot(x,yPred,'r')
plt.title('Interpolasi Lagrange')
plt.xlabel('Fitur X')
plt.ylabel('Fitur Y')
plt.show()

# Prediction
xPred = 3.5
yPred = regresi.lagrange(x,y,xPred)
print('Hasil Prediksi:', yPred)