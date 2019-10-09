{% extends "layout.html" %}
@app.route('/')
def home():
    return 'Hello!'
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

import courses as cs
df = cs.DataFrame(columns=["Course ID", "Course Number", "Course Title"])
    cs_id = raw_input("Enter the ID # of a course.")
    cs_number = raw_input("Enter the course number")
    cs_title = raw_input("Enter the title of the course")
df.index = range(len(df.index))
print df

import requests
url = "https://z_fonz.com/html"
res = requests.get('https://z_fonz.com/html')
payload = {'q':'python'}
df = requests.post(url, payload)
with open("requests_results.html", "w") as f:
    f.write(df.content)
print(res)

 @route('/add_course')
def index(student_name):
  return render_template('index.html'):


 @route('/register_student/int:course_id')
def index(student_name):
  return render_template('index.html'):

import requests
URL = "https://z_fonz.com/html"
r = requests.get(url = https://z_fonz.com/html)
data = r.json()
cs_id = data['cs_id'][0]['cs_number']['cs_title']
cs_number = data['cs_id'][0]['cs_number']['cs_title']
cs_title = data['cs_id'][0]['cs_number']['cs_title']
print df

import requests
API_KEY = "af04d1dd66389af969a92869ede28e1e"
source_code = '''
 cs_id = raw_input("Enter the ID # of a course.")
 cs_number = raw_input("Enter the course number")
 cs_title = raw_input("Enter the title of the course")
'''
data = {'api_dev_key':af04d1dd66389af969a92869ede28e1e,
        'api_option':'paste',
        'api_paste_code':, (cs_id = raw_input("Enter the ID # of a course.")
        cs_number = raw_input("Enter the course number")
        cs_title = raw_input("Enter the title of the course")
        'api_paste_format':'python'}
r = requests.post(url = af04d1dd66389af969a92869ede28e1e)
pastebin_url = r.text
return render_template('course_details.html')
