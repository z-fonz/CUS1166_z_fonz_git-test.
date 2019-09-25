class_roster(grade_view):
student_name1 = "Zachary Fonseca"
student_grade1 = "A"
student_standing1 = "Junior"
student_name2 = "Zackary Sousa"
student_grade2 = "B"
student_standing2 = "Freshman"
student_name3 = "Peter Galvao"
student_grade3 = "A"
student_standing3 = "Sophomore"
student_name4 = "Dominic DeAndrade"
student_grade4 = "B"
student_standing4 = "Junior"
student_name5 = "Ashley Vargas"
student_grade5 = "C"
student_standing5 = "Senior"
student_name6 = "John Blake"
student_grade6 = "D"
student_standing6 = "Junior"
student_name7 = "Dimitri Smith"
student_grade7 = "F"
student_standing7 = "Senior"

if grade_view = 0:
    print(student_name1, student_grade1, student_standing1, student_name2, student_grade2, student_standing2,student_name3, student_grade3, student_standing3,student_name4, student_grade4, student_standing4, student_name5, student_grade5, student_standing5, student_name6, student_grade6, student_standing6, student_name7, student_grade7, student_standing7)

if grade_view = 1:
    print(student_name1, student_grade1, student_name2, student_grade2, student_name3, student_grade3, student_name4, student_grade4, student_name5, student_grade5, student_name6, student_grade6, student_name7, student_grade7)

if grade_view = 2:
    print(student_name1, student_standing1, student_name2, student_standing2, student_name3, student_standing3, student_name4, student_standing4, student_name5, student_standing5, student_name6, student_standing6, student_name7, student_standing7)

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)

 @route('/welcome/<string:student_name>')
def index(student_name):
  return render_template('welcome.html'):

@route('/roster/<int:grade_view>')
def index(grade_view):
    return render_template('roster.html'):
