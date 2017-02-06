# mongo1 assignment
# Team: The Russian Spy
# Misha Kotlik
# SoftDev, Pd. 6

from pymongo import MongoClient


def main():
    print_averages()


def print_averages():
    # Connect to mongo server and retrieve collecction
    # Use localhost for testng (default), and for now for sumission?
    client = MongoClient()
    cursor = client["TheRussianSpy"].students.find()
    for student in cursor:
        gradeSum = 0
        for course in student["courses"]:
            gradeSum += course["mark"]
        average = gradeSum / len(student["courses"])
        studStr = "Name: " + student["name"] + " | ID: " + student["id"]
        studStr += " | Average " + average
        print studStr
    client.close()


main()
