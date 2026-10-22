
from sklearn.naive_bayes import GaussianNB

X = [[1, 20], [2, 21], [3, 22], [6, 30], [7, 31], [8, 32]]
y = [0, 0, 0, 1, 1, 1]

model = GaussianNB()
model.fit(X, y)

prediction = model.predict([[2, 21]])

print("Naive Bayes Classification")
print("Training completed successfully")
print("Input: [2, 21]")
print("Predicted Class:", prediction[0])
