import csv
import pandas as pd 
import geopy
from geopy.geocoders import Nominatim
import openpyxl
from openpyxl import load_workbook 
import users
import time
from users import Teacher, Student 

INF = 1e9
class Schedule: 
    """
    Models a schedule as a set of connected acyclic graphs 
    """
    def __init__(self, students, teachers, Session1, Session2, 
                       Session3, Session4, Session5, Session6): 
        self.Session1 = Session1 
        self.Session2 = Session2 
        self.Session3 = Session3 
        self.Session4 = Session4 
        self.Session5 = Session5 
        self.Session6 = Session6
        self.students = students 
        self.teachers = teachers 
    
    def build_graph(self): 
        """
        """
        schedule = [[INF]*len(students.keys())]


def get_teacher_data(survey_responses:str):
    """
    takes as input survey responses in csv file
    assumes survey responses are organized as follows: 
        ID | FirstName | LastName | EmailAddress | Address | Availability
    returns a dictionary mapping a teacher to sessions they can teach 
    """
    teachers = {}
    wb = load_workbook(filename = survey_responses, data_only=True) 
    ws = wb['teacher']
    for row in ws.iter_rows(ws.min_row+1, 4):
        time.sleep(1)
        ID = row[0].value
        First = row[1].value
        Last = row[2].value
        ClinicName = row[3].value
        ClinicAddress = row[4].value
        AvailabilityData = row[5].value
        teacher = Teacher(ID, First, Last, ClinicName, ClinicAddress, AvailabilityData)
        teachers[ID] = teacher 
    
    return teachers

def get_student_data(survey_responses:str):
    """
    takes as input survey responses in csv file
    assumes survey responses are organized as follows
        ID | FirstName | LastName | Address |TravelMethods | Session#
    """
    students = {}
    wb = load_workbook(filename = survey_responses, data_only=True) 
    ws = wb['student']
    for row in ws.iter_rows(ws.min_row+1, 4):
        time.sleep(1)
        ID = row[0].value
        First = row[1].value
        Last = row[2].value
        Address = row[3].value
        TravelMethod = row[4].value
        Session = row[5].value
        student = Student(ID, First, Last, Address, TravelMethod, Session)
        students[ID] = student
    return students
    
def make_student_schedules(survey_responses:dict): 
    """
    takes as input geocoded survey responses in dict 
    returns a student schedule  
    """
    pass 

def main():
    file1 = "test_teacher_data.xlsx"
    file2 = "test_student_data.xlsx"

    teacher_records = get_teacher_data(file1)
    student_records = get_student_data(file2)
    for teacher in teacher_records:
        teacher_records[teacher].print_teacher()

if __name__=="__main__": 
    main()

