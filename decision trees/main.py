#decision tree for playing tennis or not depending on the weather
import pandas as pd
from sklearn import tree

# Create a simple dataset
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'High', 'Normal', 'Normal'],
    'Windy': [False, True, False, False, True, True, False, False, False, True],
    'Play': [False, False, True, True, True, False, True, False, True, True]
}

df = pd.DataFrame(data)

# Preprocess the data
X = df.drop('Play', axis=1)
y = df['Play']

# Convert categorical variables to numerical
X = pd.get_dummies(X)

# Train the decision tree classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

# Visualize the decision tree
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))
tree.plot_tree(clf, feature_names=X.columns, class_names=['No', 'Yes'], filled=True)
plt.show()
# Predicting with the trained model
sample = pd.DataFrame({ 
    'Outlook_Sunny': [1],
    'Outlook_Overcast': [0],
    'Outlook_Rain': [0],
    'Temperature_Hot': [0],
    'Temperature_Mild': [1],
    'Temperature_Cool': [0],
    'Humidity_High': [0],
    'Humidity_Normal': [1],
    'Windy_False': [1],
    'Windy_True': [0]
})
prediction = clf.predict(sample)
print("Prediction for the sample input:", "Play" if prediction[0] else "Don't Play")
# Save the model if needed
# import joblib
# joblib.dump(clf, 'decision_tree_model.pkl')
# Load the model if needed
# clf = joblib.load('decision_tree_model.pkl')
# Example usage of the model
# sample = pd.DataFrame({
#     'Outlook_Sunny': [1],
#     'Outlook_Overcast': [0],      