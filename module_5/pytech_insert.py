""" 
    Title: pytech_insert.py
    Author: Isaac Jakubo
    Date: 5 December 2021
    Description: A Test program for inserting new documents 
                 into the students collection 
"""

#Importing the Required modules
from pymongo import MongoClient

#Creating the variable containing the MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.xfhf4.mongodb.net/pytech?retryWrites=true&w=majority"

#Creating the variable to connect to MongoDB cluster
client = MongoClient(url)

#Creating the variable to for connecting to the Pytech database
db = client.pytech


#Creating the variable for villtris with student information
villtris = {
      "student_id": "1007",
      "first_name": "Isaac",
      "last_name": "Villtris",
      "enrollments": [
        {
          "term": "Session 1",
          "gpa": "3.0",
          "start_date": "1/1/2021",
          "end_date": "3/30/2021",
          "courses": [
            {
              "course_id": "250",
              "desciption": "Intro To java",
              "instructor": "Mrs Growal",
              "grade": "A-"
            },
            {
              "course_id": "175",
              "desciption": "Introduction to Databases",
              "instructor": "Mr Green",
              "grade": "A-"
            }
            ]
        },
        {
          "term": "Session 2",
          "gpa": "3.9",
          "start_date": "4/1/2021",
          "end_date": "6/30/2021",
          "courses": [
            {
              "course_id": "275",
              "desciption": "Advanced Java",
              "instructor": "Mrs Growal",
              "grade": "A"
            },
            {
              "course_id": "190",
              "desciption": "Databases in Web Applications",
              "instructor": "Mr Green",
              "grade": "A+"
            }
            ]
        }
        ]
}
#Creating the variable for sapphire with student information
sapphire = {
      "student_id": "1118",
      "first_name": "Gareld",
      "last_name": "Sapphire",
      "enrollments": [
        {
          "term": "Session 1",
          "gpa": "3.2",
          "start_date": "1/1/2021",
          "end_date": "3/31/2021",
          "courses": [
            {
              "course_id": "250",
              "desciption": "intro to java",
              "instructor": "Mrs Growal",
              "grade": "B+"
            },
            {
              "course_id": "175",
              "desciption": "Introduction to Databases",
              "instructor": "Mr Green",
              "grade": "B+"
            }
            ]
        },
        {
          "term": "Session 2",
          "gpa": "2.9",
          "start_date": "4/1/2021",
          "end_date": "6/30/2021",
          "courses": [
            {
              "course_id": "275",
              "desciption": "Advanced Java",
              "instructor": "Mrs Growal",
              "grade": "C+"
            },
            {
              "course_id": "190",
              "desciption": "Databases in Web Applications",
              "instructor": "Mr Blue",
              "grade": "B-"
            }
            ]
        }
        ]
}
#Creating the variable for Liechtenstein with student information
liechtenstein = {
      "student_id": "1993",
      "first_name": "Von",
      "last_name": "Liechtenstein",
      "enrollments": [
        {
          "term": "Session 1",
          "gpa": "3.0",
          "start_date": "1/1/2021",
          "end_date": "3/31/2021",
          "courses": [
            {
              "course_id": "250",
              "desciption": "Intro to Java",
              "instructor": "Mrs Growal ",
              "grade": "C+"
            },
            {
              "course_id": "175",
              "desciption": "Introduction to Databases",
              "instructor": "Mr Green",
              "grade": "C+"
            }
            ]
        },
        {
          "term": "Session 2",
          "gpa": "3.0",
          "start_date": "4/1/2021",
          "end_date": "6/30/2021",
          "courses": [
            {
              "course_id": "275",
              "desciption": "Advanced Java",
              "instructor": "Mrs Brown",
              "grade": "B"
            },
            {
              "course_id": "190",
              "desciption": "Databases in Web Applications",
              "instructor": "Mr Blue",
              "grade": "B"
            }
            ]
        }
        ]
}

#Creating the variable for the students collections
students = db.students


print("\n -- INSERT STATEMENTS --")

#Insert the  statement with output for the student Isaac Viltris
villtris_student_id = students.insert_one(villtris).inserted_id
print(" Inserted student record Isaac Villtris into the students collection with document_id " + str(villtris_student_id))

#Insert the statement with output for Gareld Saphire 
saphire_student_id = students.insert_one(sapphire).inserted_id
print(" Inserted student record Sam Turner into the students collection with document_id " + str(saphire_student_id))

#Insert the statement with output for Von Liechtenstein 
liechtenstein_student_id = students.insert_one(Liechtenstein).inserted_id
print(" Inserted student record Von Liechtenstein into the students collection with document_id " + str(liechtenstein_student_id))

#The Final the statement for informing the user the program has finished
input("\n\n End of program, press any ket to exit... ")