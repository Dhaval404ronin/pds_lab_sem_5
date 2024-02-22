import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline

# Step 1: Define your own data
# Replace these lists with your own data
X = [
    "This is a positive sentence about a product.",
    "I love this product; it works great!",
    "This is a negative review; the product is terrible.",
    "The customer service was excellent.",
    "I had a bad experience with the company's support team."
]  # List of text data

y = [1, 1, 0, 1, 0]  # Corresponding labels (1 for positive, 0 for negative)

# Step 2: Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Create a text classification pipeline
tfidf_vectorizer = TfidfVectorizer()
classifier = SVC()

# Step 4: Perform grid search to find the best parameters
param_grid = {
    'tfidf_vectorizer__ngram_range': [(1, 1), (1, 2), (1, 3)],
    'classifier__C': [0.1, 1, 10],
    'classifier__kernel': ['linear', 'rbf']
}

grid_search = GridSearchCV(
    estimator=Pipeline([('tfidf_vectorizer', tfidf_vectorizer), ('classifier', classifier)]),
    param_grid=param_grid, cv=5, n_jobs=-1
)

grid_search.fit(X_train, y_train)

# Step 5: Get the best parameters and fit the model
best_params = grid_search.best_params_
best_model = grid_search.best_estimator_
best_model.fit(X_train, y_train)

# Step 6: Evaluate the model on the test set
y_pred = best_model.predict(X_test)

# Step 7: Calculate accuracy and classification report
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f"Best Parameters: {best_params}")
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_rep)
