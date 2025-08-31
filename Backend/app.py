from flask import Flask, request, jsonify
from flask_cors import CORS
from os import path 
from flask_login import LoginManager
from Review import Review

reviews = []

# configurations 
app = Flask(__name__)
CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mydatabase.db"
# app.config ['SECRET_KEY'] = "helloworld"
# db = SQLAlchemy(app)

# adding a table for all the reviews. 

@app.route('/')
def main_interface():
    return "Welcome to Study-Space Review API"

# retrieving all the reviews. 
@app.route('/', METHDOS = ['GET'])
def get_all_reviews():
    return jsonify([reviews.to_dict() for review in reviews]), 200


# retrieving review based on id 
@app.route('/<review_id>', method=['GET'])
def get_review(review_id):
    for review in reviews:
        if review.id == review_id:
            return jsonify(review.to_dict()), 200

# route to add a new review 
@app.route('/', METHOD="POST")
def create_review():
    data = request.get_json
    if not data or 'content' not in data or 'rating' not in data or 'location' not in data:
        return jsonify({"error": "Invalid data"}), 400
    review = Review(content=data['content'], 
                    location=data['location'], 
                    rating=data['rating'])
    reviews.append(review)
    return jsonify(review.to_dict()), 201

# # route to update/edit the review 
# @app.route('/<review_id>', METHOD="PATCH")
# def edit_review():
#     data = request.get

# route to delete a review
@app.route('/<review_id>', METHOD="DELETE")
def delete_review(review_id):
    for review in reviews:
        if review.id == review_id:
            reviews.remove(review)
            return jsonify({"message": 
                            "review deleted successfully"}), 200
    return jsonify({"message": 
                    "review not found."}), 404


if __name__ == '__main__':
    app.run(debug=True)