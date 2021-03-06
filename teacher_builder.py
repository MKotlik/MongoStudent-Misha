# mongo1 assignment
# Team: The Russian Spy
# Misha Kotlik
# SoftDev, Pd. 6

from pymongo import MongoClient
import csv  # facilitates CSV I/O


def main():
    insert_teachers()


def insert_teachers():
    # Read list of teachers from teachers.csv
    teachersList = createTeachersList()
    
    # Connect to mongo server and retrieve collecction
    # Use localhost for testng (default), and for now for sumission?
    client = MongoClient()
    coll = client["TheRussianSpy"].students

    # Iterate over teachers lsit and add student lists
    for teacher in teachersList:
        students = []
        results = coll.find({"courses.code": teacher["code"]})
        for student in results:
            students.append(student["id"]) # Could also use _id
        teacher["students"] = students

    # Create and fill teachers collection
    result = client["TheRussianSpy"].teachers.insert_many(teachersList)
    
    # Close connection
    client.close()

def createTeachersList():
    with open("data/teachers.csv", 'r') as csvFile:
        csvInfo = csv.DictReader(csvFile)
        teachersList = []
        for entry in csvInfo:
            tDict = entry
            teachersList.append(tDict)
        return teachersList


main()

