import tensorflow as tf
from tensorflow import keras
import numpy as np

# Generate some random data for binary classification
np.random.seed(0)
X = np.random.randn(100, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

# Create a sequential model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(2,)),      # Input layer with 2 features
    tf.keras.layers.Dense(10, activation='relu'),  # Hidden layer with 10 units and ReLU activation
    tf.keras.layers.Dense(1, activation='sigmoid')  # Output layer with 1 unit and sigmoid activation
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=100, verbose=0)

# Make predictions
predictions = model.predict(X)

# Print the first few predictions
print("Predictions:")
print(predictions[:5])

# Evaluate the model
loss, accuracy = model.evaluate(X, y)
print("\nModel Evaluation:")
print(f"Loss: {loss:.4f}")
print(f"Accuracy: {accuracy*100:.2f}%")
