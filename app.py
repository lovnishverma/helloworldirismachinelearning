from flask import Flask, render_template, request  # Flask modules
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load and preprocess the dataset
dataset = "iris.csv"  # Ensure this file exists
data = pd.read_csv(dataset, header=None)

# Extract features (X) and labels (y)
X = data.iloc[:, :-1].values  # All columns except the last one (features)
y = data.iloc[:, -1].values   # The last column (target labels)

# Encode labels because they are strings
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)  # Converts labels like "Iris-setosa" to numbers

# Train Logistic Regression model
model = LogisticRegression(solver="liblinear")  # Using liblinear for small datasets
model.fit(X, y)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/irisf', methods=["POST"])
def predict():
    try:
        # Extract input values and convert them to floats
        swidth = float(request.form.get("swidth"))
        sheight = float(request.form.get("sheight"))
        pwidth = float(request.form.get("pwidth"))
        pheight = float(request.form.get("pheight"))

        # Predict flower type
        prediction = model.predict([[swidth, sheight, pwidth, pheight]])
        flower_name = label_encoder.inverse_transform(prediction)[0]  # Convert number back to label

        return render_template("index.html", data=flower_name)
    except ValueError:
        return render_template("index.html", data="Invalid input! Please enter numbers.")

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development
