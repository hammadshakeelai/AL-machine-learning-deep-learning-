#decision tree for playing tennis or not depending on the weather


import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Create a simple dataset
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain'],

    'PlayTennis': [False, False, True, True, True, False, True, False, True, True]
}

df = pd.DataFrame(data)
# Preprocess the data
X = df[['Outlook']]
y = df['PlayTennis']
# Convert categorical variables to numerical
X = pd.get_dummies(X, drop_first=True)
# Train the decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)
# Visualize the decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=X.columns, class_names=['No', 'Yes'], filled=True)
plt.show()
# Predicting with the trained model
sample = pd.DataFrame({
    'Outlook_Sunny': [1],
    'Outlook_Overcast': [0],
    'Outlook_Rain': [0]
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
#     'Outlook_Rain': [0]
# })
# prediction = clf.predict(sample)
# print("Prediction for the sample input:", "Play" if prediction[0] else "
# Don't Play")
# Save the model if needed
