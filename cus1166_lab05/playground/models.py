from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Course(db.Model):
   __tablename__= "Course"
   id = db.Column(db.Integer,primary_key=True)
   course_number = db.Column(db.String, nullable = False)
   course_title = db.Column(db.String, nullable = False)
   course = db.relationship("course", backref="course", hard_course=True)

class RegisteredStudent(db.Model):
    __tablename__= "RegisteredStudent"
   id = db.Column(db.Integer,primary_key=True)
   name = db.Column(db.String, nullable = False)
   grade = db.Column(db.String, nullable = False)
   student = db.relationship("student", backref="course", hardworking=True)
