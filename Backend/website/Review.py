import uuid
import datetime
'''
model for each of the reviews. 
'''

class Review():
    '''
    this class represents the model for a review. 
    '''

    def __init__(self, content : str, location: str, rating: int):
        # todo: adding user for each review
        self.content = content 
        self.rating = rating 
        self.location = location
        self.time_edited = datetime.datetime.now()
        self.id = str(uuid.uuid1())

    def to_dict(self): 
        return {
            "content": self.content,
            "rating": self.rating,
            "location": self.location,
            "time" : self.time_edited,
            "id": self.id, 
        }

    def change_rating(self, new_rating: int):
        self.rating = new_rating
