# Homework 1: A POST API
# ------------------------------------------------------------
# TOPICS: FastAPI, POST, JSON in and JSON out
#
# PROBLEM
# Build a FastAPI app with ONE POST route /greet.
# - The JSON body has a name (text) and an age (number). Use a BaseModel.
# - Return JSON with a message, and a group: adult if age is 18 or more,
#   otherwise minor.
# - Run it:  uvicorn 01_post_api:app --reload   (from inside the homework folder)
#
# TEST IT WITH TALEND API TESTER
# Install the Talend API Tester extension in your browser, then:
#   Method: POST    URL: http://127.0.0.1:8000/greet
#   Body (JSON): {"name": "Ali", "age": 21}
#   Press Send and check the response.
#
# EXPECTED OUTPUT (your program should behave like this)
#   POST /greet  {"name": "Ali", "age": 21}
#     ->  {"message": "Hello, Ali", "group": "adult"}
#   POST /greet  {"name": "Sam", "age": 12}
#     ->  {"message": "Hello, Sam", "group": "minor"}
# ------------------------------------------------------------
# Write your code below this line


