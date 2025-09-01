from flask import Blueprint, jsonify, request
from .Review import Review

reviews = []

main_page = Blueprint("main_page", __name__)

@main_page.route('/', methods = ['GET'])
def get_all_reviews():
    return jsonify([review.to_dict() for review in reviews]), 200


# retrieving review based on id 
@main_page.route('/<review_id>', methods=['GET'])
def get_review(review_id):
    for review in reviews:
        if review.id == review_id:
            return jsonify(review.to_dict()), 200

# route to add a new review 
@main_page.route('/', methods=["POST"])
def create_review():
    data = request.get_json()
    if not data or 'content' not in data or 'rating' not in data or 'location' not in data:
        return jsonify({"error": "Invalid data"}), 400
    review = Review(content=data['content'], 
                    location=data['location'], 
                    rating=data['rating'])
    reviews.append(review)
    return jsonify(review.to_dict()), 201

# # route to update/edit the review 
# @main_page.route('/<review_id>', METHOD="PATCH")
# def edit_review():
#     data = request.get

# route to delete a review
@main_page.route('/<review_id>', methods=["DELETE"])
def delete_review(review_id):
    for review in reviews:
        if review.id == review_id:
            reviews.remove(review)
            return jsonify({"message": 
                            "review deleted successfully"}), 200
    return jsonify({"message": 
                    "review not found."}), 404