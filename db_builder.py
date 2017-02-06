# mongo1 assignment
# Team: The Russian Spy
# Misha Kotlik
# SoftDev, Pd. 6

from pymongo import MongoClient
import csv  # facilitates CSV I/O


def main():
    insert_students()


def insert_students():
    # Read students CSV file into a dict of student-dicts
    studentsDict = createStudentsDict()

    # Read coruses CSV file to append courses to respective student dicts
    appendCourses(studentsDict)

    # Convert studentsDict into list of studentsDict
    studentsList = studentsDict.values()

    print studentsList

    # Connect to mongo server and insert collection
    # Use localhost for testng (default), lisa for submission?
    client = MongoClient("lisa.stuy.edu")
    db = client["TheRussianSpy"]
    result = db.students.insert_many(studentsList)
    client.close()


def createStudentsDict():
    with open("data/peeps.csv", 'r') as csvFile:
        csvInfo = csv.DictReader(csvFile)
        studentsDict = {}
        for entry in csvInfo:
            sDict = entry
            sDict["courses"] = []
            studentsDict[sDict["id"]] = sDict
        return studentsDict


def appendCourses(studentsDict):
    with open("data/courses.csv", 'r') as csvFile:
        csvInfo = csv.DictReader(csvFile)
        for entry in csvInfo:
            courseDict = {"code": entry["code"], "mark": entry["mark"]}
            studentsDict[entry["id"]]["courses"].append(courseDict)
        # No need to return, should be mutated by reference

main()
