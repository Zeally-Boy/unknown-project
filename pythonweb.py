#!C:\Users\user\Downloads
print("content-type: text/html")
print()

import cgi
print("<h1> Welcome to Python</h1>")
print("<hr/>")
print("<h1> Using input tag</h1>")
print("<body bgcolor = 'red'>")

form = cgi.FieldStorage()

id = form.getvalue("id")
username = form.getvalue("name")
address = form.getvalue("address")
phonenumber = form.getvalue("phone number")
email = form.getvalue("email")
gender = form.getvalue("gender")
course = form.getvalue("course")

import mysql.connector
con = mysql.connector.connect(user="root", password="", host="localhost", database="webpython")
cur = con.cursor()

cur.execute("insert into python values(%s, %s, %s, %s, %s, %s, %s)",(id, username, address, phonenumber, email, gender, course))

cur.close()
con.close()
print("<h3>Record Inserted Successfully</h3>")
print("<a href = 'http://localhost/DJANGO/index.html'> click here to go back</a>")
