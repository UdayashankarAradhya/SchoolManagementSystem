# School Management System

This project is a simple school management system built with two main components:
1.  A backend student manager written in C.
2.  A Python chatbot (using Flask and Twilio) to interact with the data.

## Features

* **C Program:** Manages a database of 50 pre-filled student records. (List what it can do: add, delete, search, etc.)
* **Python Bot:** Allows users to query student information via an SMS chatbot.

## How to Run

### 1. C Program (C_code/)

1.  Navigate to the `C_code` directory: `cd C_code`
2.  Compile the program: `gcc student_manager.c -o student_manager`
3.  Run the program: `./student_manager`

### 2. Python Bot (Python_bot/)

1.  Navigate to the `Python_bot` directory: `cd Python_bot`
2.  Install the required dependencies: `pip install -r requirements.txt`
3.  (Add any steps to set up API keys, e.g., create a `.env` file)
4.  Run the Flask app: `python app.py`