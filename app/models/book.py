from app import db



class Book(db.Model):
    #notice the Book class is connected to the model
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title  = db.Column(db.String)
    drescription = db.Column(db.String)

    def to_string(self):
        return f"{self.id}: {self.title} Description: {self.description}"



