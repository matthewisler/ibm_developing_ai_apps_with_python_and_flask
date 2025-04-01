# Import the Flask class from the flask module
from flask import Flask, make_response, request

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world"

# Define a route for the "/no_content" URL
@app.route("/no_content")
def no_content():
    # Function that handles requests to the root URL
    # Return a plain text response
    return ({"message": "No content found"}, 204)

# Define a route for the "/no_content" URL
@app.route("/exp")
def index_explicit():
    # Function that handles requests to the root URL
    # Return a plain text response
    res = make_response({"message": "Hello World"})
    res.status_code = 200
    return res

'''
@app.route("/person", methods=['POST'])
def add_by_uuid():
    new_person = request.get_json
    if not new_person:
        return {"message": "Invalid input provided"}, 422
    
    try:
        data.append(new_person)
    except NameError:
        return {"message": "Data not defined"}, 500

    return {"message": "Person created successfully"}, 201
'''
@app.route("/person", methods=['POST'])
def add_by_uuid():
    new_person = request.json
    if not new_person:
        return {"message": "Invalid input parameter"}, 422
    # code to validate new_person ommited
    try:
        data.append(new_person)
    except NameError:
        return {"message": "data not defined"}, 500

    return {"message": f"{new_person['id']}"}, 200