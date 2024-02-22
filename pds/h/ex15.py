from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Text data for the cat and dog articles
cat_article = """
The cat (Felis catus) is a domestic species of small carnivorous mammal. It is the only domesticated species in the family Felidae and is often referred to as the domestic cat to distinguish it from wild members of the family...
"""

dog_article = """
The domestic dog (Canis lupus familiaris or Canis familiaris) is a domesticated descendant of the wolf, characterized by an upturning tail. They were the first species to be domesticated...
"""

# Create a custom preprocessor to clean and preprocess the text
def custom_preprocessor(text):
    # Add your custom preprocessing logic here, e.g., lowercasing, removing special characters, etc.
    return text.lower()

# Create a text classification pipeline
ngram_range = (2, 5)  # Adjust the n-gram range as needed
tfidf_vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=ngram_range, preprocessor=custom_preprocessor)
classifier = SVC(kernel='linear')

# Prepare the training data
X = [cat_article, dog_article]
y = ['Cat', 'Dog']  # Ensure you have two distinct class labels

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the classifier to the training data
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
classifier.fit(X_train_tfidf, y_train)

# Predict and evaluate on the test set
X_test_tfidf = tfidf_vectorizer.transform(X_test)
y_pred = classifier.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_rep)
