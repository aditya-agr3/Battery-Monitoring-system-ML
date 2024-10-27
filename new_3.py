import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
##from imblearn.over_sampling import SMOTE
from warnings import filterwarnings

# Suppress warnings
filterwarnings('ignore')

# Load the dataset
data = pd.read_csv('Battery_RUL.csv')

print(data.columns)

# Separate input features (X) and output labels (Y)
X = data.drop(columns=['Charging time (s)','RUL'])
Y = data[['Charging time (s)','RUL']]

# Feature selection using chi-square test
fs = SelectKBest(score_func=chi2, k='all')
X_selected = fs.fit_transform(X, Y)

# Plot feature importance
features_data = pd.DataFrame({'Feature': X.columns, 'Scores': fs.scores_})
plt.figure(figsize=(9, 4))
sns.barplot(x='Scores', y='Feature', data=features_data, palette='twilight_shifted_r')
plt.savefig("FeatureImportance.png")
plt.show()

# Identify insignificant features
insignificant_features = features_data.loc[features_data['Scores'] < 50]['Feature'].values

# Remove insignificant features from input features
X = X.drop(columns=insignificant_features)

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Define separate SMOTE instances for each output label
smote_stroke = SMOTE(random_state=42)
smote_highbp = SMOTE(random_state=42)
smote_diabetes = SMOTE(random_state=42)

# Resample each output label individually
X_train_resampled_stroke, y_train_resampled_stroke = smote_stroke.fit_resample(X_train, y_train['Stroke'])
X_train_resampled_highbp, y_train_resampled_highbp = smote_highbp.fit_resample(X_train, y_train['HighBP'])
X_train_resampled_diabetes, y_train_resampled_diabetes = smote_diabetes.fit_resample(X_train, y_train['Diabetes'])

# Train separate Random Forest classifiers for each output label
rf_model_stroke = RandomForestClassifier(random_state=42)
rf_model_highbp = RandomForestClassifier(random_state=42)
rf_model_diabetes = RandomForestClassifier(random_state=42)

rf_model_stroke.fit(X_train_resampled_stroke, y_train_resampled_stroke)
rf_model_highbp.fit(X_train_resampled_highbp, y_train_resampled_highbp)
rf_model_diabetes.fit(X_train_resampled_diabetes, y_train_resampled_diabetes)

# Predict the output labels for the testing set
y_pred_stroke = rf_model_stroke.predict(X_test)
y_pred_highbp = rf_model_highbp.predict(X_test)
y_pred_diabetes = rf_model_diabetes.predict(X_test)

# Calculate and print accuracy for each output label
accuracy_stroke = accuracy_score(y_test['Stroke'], y_pred_stroke)
accuracy_highbp = accuracy_score(y_test['HighBP'], y_pred_highbp)
accuracy_diabetes = accuracy_score(y_test['Diabetes'], y_pred_diabetes)

print("Test Accuracy (Stroke):", accuracy_stroke)
print("Test Accuracy (HighBP):", accuracy_highbp)
print("Test Accuracy (Diabetes):", accuracy_diabetes)

# Print classification report for each output label
print("Classification Report (Stroke):")
print(classification_report(y_test['Stroke'], y_pred_stroke))

print("Classification Report (HighBP):")
print(classification_report(y_test['HighBP'], y_pred_highbp))

print("Classification Report (Diabetes):")
print(classification_report(y_test['Diabetes'], y_pred_diabetes))
