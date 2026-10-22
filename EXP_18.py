from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[6]])

print("Linear Regression")
print("Training completed successfully")
print("Input:", 6)
print("Predicted Output:", prediction[0])
