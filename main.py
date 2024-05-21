import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from lightgbm import LGBMClassifier
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv(r'C:\Users\ASUS\Phishr-API-main\data\url_dataset_processed.csv')

# Separate features and labels (assuming 'result' is the name of the target column)
features = data.drop(columns=['url', 'result'])
labels = data['result']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Initialize the models
dt_model = DecisionTreeClassifier(random_state=42)
rf_model = RandomForestClassifier(random_state=42)
mlp_model = MLPClassifier(random_state=42)
lgbm_model = LGBMClassifier(random_state=42)

# Train the models
dt_model.fit(X_train, y_train)
rf_model.fit(X_train, y_train)
mlp_model.fit(X_train, y_train)
lgbm_model.fit(X_train, y_train)

# Make predictions using the models
dt_predictions = dt_model.predict(X_test)
rf_predictions = rf_model.predict(X_test)
mlp_predictions = mlp_model.predict(X_test)
lgbm_predictions = lgbm_model.predict(X_test)

# Calculate accuracy of each model
dt_accuracy = accuracy_score(y_test, dt_predictions)
rf_accuracy = accuracy_score(y_test, rf_predictions)
mlp_accuracy = accuracy_score(y_test, mlp_predictions)
lgbm_accuracy = accuracy_score(y_test, lgbm_predictions)

# List of accuracies and corresponding models
accuracies = [dt_accuracy, rf_accuracy, mlp_accuracy, lgbm_accuracy]
models = ['Decision Tree', 'Random Forest', 'MLP', 'LightGBM']

# Plot the accuracies
plt.figure(figsize=(10, 6))
plt.bar(models, accuracies, color=['blue', 'orange', 'green', 'red'])
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.title('Comparison of Model Accuracies')
plt.ylim(0, 1)  # Set y-axis limit between 0 and 1
plt.show()
