import pandas as pd
import CSP
from datetime import *

# get input from driver and create various lists
def function(branch, semester):
 
    faculty_data_frame = pd.read_excel('AI - Timetable.xlsx', sheet_name = 'Faculty')
    courses_data_frame = pd.read_excel('AI - Timetable.xlsx', sheet_name = 'Courses')
    
    # mapping of teacher id to [branch,name,from,to,[list of courses they teach]]
    comp_department = dict()
    entc_department = dict()
    mech_department = dict()
    
    # this is mapping of course with faculty 
    course_faculty = dict() 
    
    # this is list of list where each element of list represents the column of the df
    final_list = [faculty_data_frame['Teacher_id'].tolist(), faculty_data_frame['Teacher_name'].tolist(), faculty_data_frame['Department'].tolist(), faculty_data_frame['Time_from'].tolist(), faculty_data_frame['Time_to'].tolist()]
    # print(final_list)
    # creating seperate lists for each department 
    for id in faculty_data_frame['Teacher_id'].tolist():
        dept = list(id.split('_'))[0]
        if(dept == 'CS'):
            comp_department[id] = []
        if(dept == 'ENTC'):
            entc_department[id] = []
        if(dept == 'MECH'):
            mech_department[id] = []

    for i in range(len(faculty_data_frame['Teacher_id'].tolist())):
        dept = list(final_list[0][i].split('_'))[0]
        if(dept == 'CS'):
            comp_department[final_list[0][i]] += [faculty_data_frame['Department'].tolist()[i], faculty_data_frame['Teacher_name'].tolist()[i], faculty_data_frame['Time_from'].tolist()[i].hour, faculty_data_frame['Time_to'].tolist()[i].hour, []]
        if(dept == 'ENTC'):
            entc_department[final_list[0][i]] += [faculty_data_frame['Department'].tolist()[i], faculty_data_frame['Teacher_name'].tolist()[i], faculty_data_frame['Time_from'].tolist()[i].hour, faculty_data_frame['Time_to'].tolist()[i].hour, []]
        if(dept == 'MECH'):
            mech_department[final_list[0][i]] += [faculty_data_frame['Department'].tolist()[i], faculty_data_frame['Teacher_name'].tolist()[i], faculty_data_frame['Time_from'].tolist()[i].hour, faculty_data_frame['Time_to'].tolist()[i].hour, []]


    final_list_2 = [courses_data_frame['Teacher_id'].tolist(), courses_data_frame['Course_id'].tolist(), courses_data_frame['Course_name'].tolist(), courses_data_frame['Semester'].tolist(), courses_data_frame['Duration'].tolist(), courses_data_frame['Credits'].tolist(), courses_data_frame['Course_short_name'].tolist()]
    for i in range(len(courses_data_frame['Teacher_id'].tolist())):
        course_faculty[final_list_2[1][i]] = final_list_2[0][i] 
    # print()
    # print("before comp_department",comp_department)
    # print()
    
    # this adds all the courses taught by that teacher taken from different sheet 
    for i in range(len(courses_data_frame['Teacher_id'].tolist())):
        dept = list(final_list_2[0][i].split('_'))[0]
        if(dept == 'CS'):
            comp_department[final_list_2[0][i]][-1] += [courses_data_frame['Course_id'].tolist()[i]]
        if(dept == 'ENTC'):
            entc_department[final_list_2[0][i]][-1] += [courses_data_frame['Course_id'].tolist()[i]]
        if(dept == 'MECH'):
            mech_department[final_list_2[0][i]][-1] += [courses_data_frame['Course_id'].tolist()[i]]

    # Each department is a dictionary with key being the Teacher_id and value is a list of - 
    # Department, Teacher name, time from, time to, courses list

    courses_dict = dict()

    for i in range(len(courses_data_frame['Teacher_id'].tolist())):
        if(courses_data_frame['Course_id'].tolist()[i] not in courses_dict):
            courses_dict[courses_data_frame['Course_id'].tolist()[i]] = [courses_data_frame['Course_name'].tolist()[i], courses_data_frame['Credits'].tolist()[i], courses_data_frame['Duration'].tolist()[i], courses_data_frame['Semester'].tolist()[i], courses_data_frame['Course_short_name'].tolist()[i]]

    # Courses Dictionary contains course ID as key and value is a list of course name, credits, duration, semester, course short name
    # print("printing dicts")
    # print()
    # print("comp_department",comp_department)
    # print()
    # print("entc_department",entc_department)
    # print()
    # print("mech_department",mech_department)
    # print()
    # print("course_faculty",course_faculty)

    if(branch == 1):
        comp_courses_acc_sem = dict()
        comp_course_faculty_acc_sem = dict()

        for key in courses_dict:
            dept = list(key.split('_'))[0]
            if(dept == 'CSE'):
                if(courses_dict[key][3] == semester):
                    comp_courses_acc_sem[key] = courses_dict[key]
                    comp_course_faculty_acc_sem[key] = course_faculty[key]
        # inputs filtered before giving to generator_fn
        return CSP.generator_fn(comp_department, comp_courses_acc_sem,comp_course_faculty_acc_sem, "CSE", semester)

    elif(branch == 2):
        entc_courses_acc_sem = dict()
        entc_course_faculty_acc_sem = dict()

        for key in courses_dict:

            dept = list(key.split('_'))[0]
            if(dept == 'ENTC'):
                if(courses_dict[key][3] == semester):
                    entc_courses_acc_sem[key] = courses_dict[key]
                    entc_course_faculty_acc_sem[key] = course_faculty[key]


        return CSP.generator_fn(entc_department, entc_courses_acc_sem,entc_course_faculty_acc_sem, "ENTC", semester)
    else:
        mech_courses_acc_sem = dict()
        mech_course_faculty_acc_sem = dict()
        
        for key in courses_dict:

            dept = list(key.split('_'))[0]
            if(dept == 'MECH'):
                if(courses_dict[key][3] == semester):
                    mech_courses_acc_sem[key] = courses_dict[key]
                    mech_course_faculty_acc_sem[key] = course_faculty[key]

        return CSP.generator_fn(mech_department, mech_courses_acc_sem, mech_course_faculty_acc_sem, "MECH", semester)