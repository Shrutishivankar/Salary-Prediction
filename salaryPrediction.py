''' 
SALARY PREDICTION (MACHINE LEARNING PROJECT)
Using Simple Linear Regression
'''

# STEP 1: Import library
import pandas as pd

#Step 2: Read Dataset
df = pd.read_csv('https://github.com/YBIFoundation/Dataset/raw/main/Salary%20Data.csv')
print(df)
h= df.head()
print(h)
df.info()
d= df.describe()
print(d)

# Step 3: Define y (output : dependent/label) & X (input : independent/features/attributes)
df.columns
y = df['Salary']
x = df[['Experience Years']]
print(x)
print(y)
p = df.shape,x.shape,y.shape
print(p)

# Step 4: Train Test Split
from sklearn.model_selection import train_test_split
x_train ,x_test ,y_train, y_test = train_test_split(x,y,random_state=2529)
print("x_train :",x_train)
print("y_train :",y_train)
print("x_test :",x_test)
print("y_test :",y_test)

# Step 5: Select Model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
print(model)

# Step 6: Train Model
tm = model.fit(x_train , y_train)
# model.intercept_
# model.coef_
print(tm)

# Step 7: Predict
y_pred = model.predict(x_test)
print(y_pred)
# model.predict([3.6]) : 3.6(exp year)

# Step 8: Evaluate
from sklearn.metrics import mean_absolute_percentage_error
err = mean_absolute_percentage_error(y_test,y_pred)
print(err)