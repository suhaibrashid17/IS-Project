
SQL Injection Detection Demo

This project demonstrates a machine learning model for detecting SQL injection attempts in user inputs. It consists of two parts: a React frontend and a Flask backend. Follow the instructions below to run both parts locally.

Prerequisites

- Node.js (for React app)
- Python 3.x (for Flask app)
- Pip (for installing Python dependencies)

Step 1: Running the React App

1. Navigate to the sql-injection-detection directory:
   cd sql-injection-detection

2. Install the necessary dependencies:
   npm install

3. Once all packages are installed, start the React app:
   npm start

   The React app should now be running on http://localhost:3000.

Step 2: Running the Flask App

1. Open a new terminal and navigate to the flask-app directory:
   cd flask-app

2. Install the Python dependencies:
   pip install -r requirements.txt

3. Start the Flask server:
   python app.py

   The Flask app should now be running on http://localhost:5000.

Step 3: Testing the SQL Injection Detection

1. Open the React app in your browser (http://localhost:3000).
   
2. In the input field, type a SQL query. Make sure it's a valid query, as this demo is just to show how the model detects SQL injection attempts. In real-world scenarios, the query would be correctly written and tested, while only the user input could potentially be malicious.

3. Click on "Submit" and wait for the model's response.

4. The model will return whether the SQL query is a valid query or a potential SQL injection attempt.



