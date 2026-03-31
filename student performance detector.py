Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Student Performance Predictor using Machine Learning
... # This version takes input from user
... 
... # Step 1: Import libraries
... import pandas as pd
... from sklearn.model_selection import train_test_split
... from sklearn.linear_model import LinearRegression
... 
... # Step 2: Create dataset
... data = {
...     "hours_study": [2, 3, 4, 5, 6, 7, 8, 2, 1, 9],
...     "attendance": [60, 65, 70, 75, 80, 85, 90, 55, 50, 95],
...     "previous_marks": [50, 55, 60, 65, 70, 75, 80, 45, 40, 90],
...     "final_marks": [52, 56, 61, 66, 72, 78, 85, 48, 42, 92]
... }
... 
... # Convert dataset into table format
... df = pd.DataFrame(data)
... 
... # Step 3: Define input and output
... X = df[["hours_study", "attendance", "previous_marks"]]
... y = df["final_marks"]
... 
... # Step 4: Split dataset into training and testing
... X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
... 
... # Step 5: Create model
... model = LinearRegression()
... 
... # Step 6: Train model
... model.fit(X_train, y_train)
... 
... # Step 7: Take input from user
... print("Enter Student Details")
... 
... hours = float(input("Enter study hours per day: "))
... attendance = float(input("Enter attendance percentage: "))
... previous_marks = float(input("Enter previous marks: "))
... 
... # Step 8: Predict result
... prediction = model.predict([[hours, attendance, previous_marks]])
... 
... # Step 9: Display output
