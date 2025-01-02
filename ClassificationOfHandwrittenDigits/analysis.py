import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import GridSearchCV

(x_train, y_train), (_, _) = tf.keras.datasets.mnist.load_data()

# Stage 1/5: The Keras dataset
# Flatten each 28x28 image into a 1D array with 784 elements
n = x_train.shape[0]  # Number of images in the dataset
m = x_train.shape[1] * x_train.shape[2]  # Number of pixels in each image
x_train_reshape = x_train.reshape(n, m)

classes = np.unique(y_train)

print("Classes:", classes)
print("Features' shape:", x_train_reshape.shape)
print("Target's shape:", y_train.shape)
print(f"min: {np.min(x_train_reshape)}, max: {np.max(x_train_reshape)}")

# Stage 2/5: Split into sets
# Use the first 6000 rows of the dataset
x_subset = x_train_reshape[:6000]
y_subset = y_train[:6000]

x_train, x_test, y_train, y_test = train_test_split(
    x_subset, y_subset, test_size=0.3, random_state=40)

# Print new datasets' shapes
print("x_train shape:", x_train.shape)
print("x_test shape:", x_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# Check if the dataset is balanced
proportions = pd.Series(y_train).value_counts(normalize=True)
print("Proportion of samples per class in train set:")
print(proportions)

# Stage 4/5:Data preprocessing
normalizer = Normalizer()
x_train_norm = normalizer.fit_transform(x_train)
x_test_norm = normalizer.transform(x_test)

def fit_predict_eval(model, features_train, features_test, target_train, target_test):
    model.fit(features_train, target_train)
    predictions = model.predict(features_test)
    score = accuracy_score(target_test, predictions)
    models_acc[model.__class__.__name__] = score
    print(f'Model: {model}\nAccuracy: {score:.4f}\n')

models = [KNeighborsClassifier(),
          DecisionTreeClassifier(random_state=40),
          LogisticRegression(random_state=40, max_iter=200),
          RandomForestClassifier(random_state=40)]

models_acc = {}

for model in models:
    fit_predict_eval(model, x_train_norm, x_test_norm, y_train, y_test)

model_1st = max(models_acc, key=models_acc.get)
model_2nd = max(models_acc, key=lambda x: models_acc[x] if x != model_1st else 0)

print(f"The answer to the 1st question: yes\n")
print(f"The answer to the 2nd question: {model_1st}-{models_acc[model_1st]:.3f}, {model_2nd}-{models_acc[model_2nd]:.3f}")

# Stage 5/5: Hyperparameter tuning

# Select normalized data representation and top-performing models
selected_x_train, selected_x_test = x_train_norm, x_test_norm

# Define parameter grids
knn_param_grid = {
    'n_neighbors': [3, 4],
    'weights': ['uniform', 'distance'],
    'algorithm': ['auto', 'brute']
}

rf_param_grid = {
    'n_estimators': [300, 500],
    'max_features': ['sqrt', 'log2'],
    'class_weight': ['balanced', 'balanced_subsample']
}

# Initialize GridSearchCV
knn_grid = GridSearchCV(
    estimator=KNeighborsClassifier(),
    param_grid=knn_param_grid,
    scoring='accuracy',
    n_jobs=-1
)

rf_grid = GridSearchCV(
    estimator=RandomForestClassifier(random_state=40),
    param_grid=rf_param_grid,
    scoring='accuracy',
    n_jobs=-1
)

# Fit GridSearchCV on the train set
knn_grid.fit(selected_x_train, y_train)
rf_grid.fit(selected_x_train, y_train)

# Best estimators and accuracies
print("K-nearest neighbours algorithm")
knn_best_model = knn_grid.best_estimator_
knn_best_model.fit(selected_x_train, y_train)
knn_accuracy = accuracy_score(y_test, knn_best_model.predict(selected_x_test))
print(f"best estimator: {knn_best_model}")
print(f"accuracy: {knn_accuracy:.3f}")

print("\nRandom forest algorithm")
rf_best_model = rf_grid.best_estimator_
rf_best_model.fit(selected_x_train, y_train)
rf_accuracy = accuracy_score(y_test, rf_best_model.predict(selected_x_test))
print(f"best estimator: {rf_best_model}")
print(f"accuracy: {rf_accuracy:.3f}")
