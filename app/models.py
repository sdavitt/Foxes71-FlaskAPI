from flask_sqlalchemy import SQLAlchemy


# instantiate an instance of our ORM to handle database communication
db = SQLAlchemy()

# define a model - a model is going to be an entity/a table in our database
# and we define it with the SQL CREATE TABLE in mind (what columns do I want? what SQL datatypes will those columns be? what constraints will those columns have?)
class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    hiringprice = db.Column(db.String(20))
    age = db.Column(db.Integer)
    nationality = db.Column(db.String(50))
    bestperformance = db.Column(db.String(250))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'hiringprice': self.hiringprice,
            'age': self.age,
            'nationality': self.nationality,
            'bestperformance': self.bestperformance
        }