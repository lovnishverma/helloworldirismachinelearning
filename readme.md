# Iris Machine Learning Web App

This is a simple **Flask-based machine learning web application** that predicts the **species of an Iris flower** based on user inputs. The model is trained using **Logistic Regression** and deployed on **Glitch.com**.

## 🎥 Youtube Tutorial (Hindi)
[Click here view youtube video!](https://youtu.be/DlCdQ1MZXsc?si=ACw7zrwmCLGsYNVp)

## 🌐 Live Demo
[Click here to try the app!](https://irismachinelearning.glitch.me/)

## 📂 Project Links
- **Glitch Project:** [Glitch Editor](https://glitch.com/edit/#!/irismachinelearning)
- **GitHub Repository:** [GitHub](https://github.com/lovnishverma/helloworldirismachinelearning)

## 🛠️ Technologies Used
- **Flask** (Web Framework)
- **Scikit-Learn** (Machine Learning Model)
- **Pandas & NumPy** (Data Processing)
- **HTML & Jinja2** (Frontend Template Engine)
- **Glitch.com** (Free Deployment Platform)

## 📌 Features
✅ Train and deploy a **Logistic Regression** model for Iris species classification.  
✅ Simple web interface to input flower measurements.  
✅ Real-time predictions displayed on the web page.  
✅ Deployed on **Glitch** for easy access.  

## 📦 Installation & Setup
To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lovnishverma/helloworldirismachinelearning.git
   cd helloworldirismachinelearning
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**
   ```bash
   python app.py
   ```

5. **Access the web app locally:**
   Open a browser and go to `http://127.0.0.1:5000/`

## 🚀 Deployment on Glitch
To deploy the app on Glitch:
1. Go to [Glitch.com](https://glitch.com/)
2. Click **New Project** → **Import from GitHub**
3. Paste your repository URL: `https://github.com/lovnishverma/helloworldirismachinelearning`
4. Wait for the installation to complete.
5. Click **Show Live** to access your app!

## 📷 Screenshot

![image](https://github.com/user-attachments/assets/0ab1debe-9dc7-4be2-a281-e52023a76dde)


## 📜 License
This project is licensed under the **MIT License**.

## 🤝 Contributing
Feel free to contribute to this project! You can fork the repo, create a new branch, and submit a pull request.

## ✨ Acknowledgments
- **Scikit-Learn** for the ML model.
- **Flask** for making web deployment easy.
- **Glitch** for providing free hosting.

##***Future Enhancements for This Project 🎯* **

This Flask-based *Iris Flower Classification* project can be improved further with the following enhancements:  

✅ *Use train-test split for better accuracy* – Implement `train_test_split` from `sklearn.model_selection` to split data into *80% training and 20% testing* for better generalization.  

Currently, the model is trained on the entire dataset, which is *not a good practice* because:  
- It might memorize the dataset instead of learning general patterns (overfitting).  
- We cannot evaluate how well it performs on unseen data.  

✅ *Feature Scaling for Better Predictions* (optional but recommended)– Use `StandardScaler` from `sklearn.preprocessing` to normalize feature values, ensuring better model performance.  

✅ *Train Once, Save Model for Future Use* – Use `joblib` or `pickle` to *save the trained model* and load it later instead of retraining it every time the app runs.  

✅ *Load Trained Model in Flask* – Instead of training on every restart, modify the code to *load a pre-trained model* for faster predictions.  

✅ *Enhance UI with Bootstrap* – Improve the *frontend* using *Bootstrap* for a more professional, responsive, and visually appealing UI.  

✅ *Error Handling & Input Validation* – Implement input validation and exception handling to *prevent crashes* due to invalid user inputs.  

✅ *Logging & Debugging* – Add `logging` to capture errors and debug issues more efficiently in a production environment.  

✅ *Deploy as a REST API* – Convert the app into an *API* using `Flask-RESTful` for better integration with *mobile apps or other web services*.  

✅ *Host Model and Project on Hugging Face* – Deploy the trained model and project on *Hugging Face*, which provides 24x7 accessibility.  
- Hugging Face is *better than Glitch* for ML projects as it supports *Flask, Streamlit, and Gradio*, while Glitch only supports Flask.  

✅ *Use a Database for Storing Predictions* – Store *user inputs and predictions* in a database like *SQLite or PostgreSQL* for better data analysis and tracking.  

💡 These improvements will make your ML model more efficient, user-friendly, and scalable!  

---
👉 Made with ❤️ by [Lovnish Verma](https://github.com/lovnishverma/) 🚀
