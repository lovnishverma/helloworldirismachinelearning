from flask import *  # Import Flask and related modules to build a web application
import numpy as np  # Import NumPy for numerical operations
import pandas as pd  # Import pandas for data manipulation
from sklearn.linear_model import LogisticRegression  # Import Logistic Regression model from scikit-learn

# Initialize the Flask application
app = Flask(__name__)

# Load and train the model when the app starts
# Dataset containing information about Iris flowers
dataset = "iris.csv"  # Path to the CSV file with Iris data
data = pd.read_csv(dataset, header=None)  # Read the CSV file without assuming column headers
flower = data.values  # Convert the dataset into a NumPy array for easier processing

# Split the dataset into features (x) and target labels (y)
features = flower[:, :-1]  # All columns except the last one are the input features
labels = flower[:, -1]  # The last column contains the target labels (flower species)

# Train the Logistic Regression model
model = LogisticRegression()  # Create an instance of the Logistic Regression model
model.fit(features, labels)  # Train the model using the features and corresponding target labels

@app.route('/')
def iris():
   
    # Render the main page with the form to input flower dimensions.
   
    return render_template("index.html")  # Display the input form on the main page

@app.route('/irisf', methods=["POST"])
def page():
    
    # Handle form submission, predict flower type, and display the result.
   
    # Extract input values from the form submitted by the user
    swidth = float(request.form.get("swidth"))  # Get Sepal Width from the form
    sheight = float(request.form.get("sheight"))  # Get Sepal Height from the form
    pwidth = float(request.form.get("pwidth"))  # Get Petal Width from the form
    pheight = float(request.form.get("pheight"))  # Get Petal Height from the form

    # Predict the flower type using the trained model
    # The input values are passed as a 2D array since the model expects this format
    arr = model.predict([[swidth, sheight, pwidth, pheight]])

    # Render the main page again with the predicted flower type displayed
    return render_template("index.html", data=str(arr[0]))

if __name__ == '__main__':
    app.run()  # Start the Flask application and make it accessible
