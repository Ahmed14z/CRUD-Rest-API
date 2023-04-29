from flask import Flask , request , make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

class Person(db.Model):
     
     __tablename__ = 'Persons'

     id = db.Column(db.Integer, primary_key=True , unique=True)
     name = db.Column(db.String , nullable = False)
     age = db.Column(db.Integer , nullable = False)
     gender = db.Column(db.String , nullable = False)
     email = db.Column(db.String , nullable = False)

     def json(self):
        return{'id' : self.id , 'name' : self.name , 'age' : self.age , 'gender' : self.gender , 'email' : self.email}

db.create_all()

# Create test route

@app.route('/test' , methods=['GET'])
def test():
    return make_response(jsonify({'message' : 'test route'}), 200)

#Create a person
@app.route('/persons', methods=['POST'])
def create_person():
    try:
        data = request.get_json()
        new_person=Person(name=data['name'],age=data['age'], gender=data['gender'],email=data['email'])
        db.session.add(new_person)
        db.session.commit()
        return make_response(jsonify({'message':'person created successfully'}),201)
    except e:
     return make_response(jsonify({'message':'There was an error creating person'}),201)

#get all persons 
@app.route('/persons', methods=['GET'])
def get_persons():
    try:
        persons = Person.query.all()
        return make_response(jsonify([person.json() for person in persons]),200)

    except e:
        return make_response(jsonify({'message':'There was an error getting person'}),500)

#get a user by id 
@app.route('/persons/<int:id>', methods=['GET'])

def get_person(id):
    try:
        person = Person.query.filter_by(id=id).first()
        if person:
            return make_response(jsonify({'person':person.json()}),200)
            return make_response(jsonify({'message':'Person not found'}),404)

    except e:
        return make_response(jsonify({'message':'There was an error getting person'}),500)

#update person
@app.route('/persons/<int:id>' , methods = ['PUT'])
def update_person(id):
    try:
        person = Person.query.filter_by(id=id).first()
        if person:
            data = request.get_json()
            person.name = data['name']
            person.age = data['age']
            person.gender = data['gender']
            person.email = data['email']
            db.session.commit()
            return make_response(jsonify({'message':'Person Updated'}),200)
        return make_response(jsonify({'message':'Person not found'}),404)      
    except e:
        return make_response(jsonify({'message':'There was an error updating Person'}),500)          

#delete a person
@app.route('/persons/<int:id>',methods=['DELETE'])

def delete_user(id):
    try:
        person = Person.query.filter_by(id=id).first()
        if person:
            db.session.delete(person)
            db.session.commit()
            return make_response(jsonify({'message':'Person deleted successfully'}),200)
        return make_response(jsonify({'message':'Person not found'}),404)
    except e:
         return make_response(jsonify({'message':'Error deleting person'}),404) 




