from sklearn.model_selection import train_test_split

from sklearn.datasets import load_wine

data = load_wine(as_frame=True)["frame"]
X, y = data.iloc[:, :-1], data["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)
