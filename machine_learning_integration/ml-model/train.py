import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the dataset
df = pd.read_csv('housing1.csv').iloc[:, :-1].dropna()
print('Reading the dataset')

# Prepare the features and target variable
x = df.drop(columns='median_house_value')
y = df.median_house_value.copy()
print('split the dataset')

# Train the Linear Regression model
model = LinearRegression().fit(x, y)
print('model trained')

# Save the trained model to a file
joblib.dump(model, 'model.joblib')
print('model saved')
