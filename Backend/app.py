from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config('SQLALCHEMY_DATABASE_URI')

# adding a table for all the reviews. 

@app.route('/')
def main_interface():
    return "Welcome to Study-Space Review API"

# retrieving all the reviews. 
@app.route('/reviews', METHDOS = ['GET'])

# route to add a new review 
@app.route('/', METHOD="POST")

# route to delete a review
@app.route('/', METHOD="PATCH")


@app.route('/', METHOD="DELETE")
# route to update/edit the review 

if __name__ == "__main__":
    app.run(debug = True)