from constraint import *
from math import ceil
import TimeTable_Excel_Maker

# Courses Dictionary contains course ID as key and value is a list of course name, credits, duration, semester
def parse(courses):
    final_lst = []
    # if three credits then do cse_101_0, cse_101_1, and cse_101_2
    for key in courses.keys():
        credits = courses[key][1]
        subject = key
        for i in range(credits):
            tmp = subject + "_" + str(i)
            final_lst.append(tmp)
    return final_lst

def is_lab(course,courses):
    if(int(courses[course[:-2]][-3])==2):
        return True
    return False

# lab should be only scheduled in the given time slot
def lab_constraint(slot,_):
    return slot[4:] == "10_12"

# i.e. only one lec of a subject per day
def unique_lec_per_day(slot1,slot2):
    return slot1[:3] != slot2[:3]

def new_period_list(faculty, course, course_faculty, period_list):
    time_slots_lst = []
    course_name = course[:-2]
    faculty_name = course_faculty[course_name]
    
    available_start = faculty[faculty_name][2]
    available_end = faculty[faculty_name][3]
    for slots in period_list:
        lst = slots.split("_")
        start = int(lst[1])
        end = int(lst[2])
        if(start >= available_start and end <= available_end):
            time_slots_lst.append(slots)
    return time_slots_lst
        
def generator_fn(faculty, courses,course_faculty, department, semester):
    # print("printing courses")
    # print(courses)
    # print()
    # print("printing faculty")
    # print(faculty)
    # print()
    # print("printing course_faculty")
    # print(course_faculty)
    
    # to handle number of classes in a week
    final_courses = parse(courses)
    # print(final_courses)
    # print(len(final_courses))
    left=10+ceil((len(final_courses) + 5)/5) + 1
    # To build a balanced timetable
    for maxTime in range(left,18):
        
        timetable = Problem()

        # Assuming college timimgs are 9:00 AM - 6:00 PM, Mon - Fri

        # Mon_9 means lacture on Monday from 9:00 AM - 10:00 AM

        period_list = []
        # defining values that is lecture slots in our case
        for day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']:
            for time in range(10,maxTime): 
                a = None
                if time == 10:
                    a = day + "_" + str(time) + "_" +str(time+2)
                else:
                    a = day + "_" + str(time) + "_" +str(time+1)
                # lunch break
                if(time != 11 and time != 12):
                    period_list.append(a)

        # print()
        # print("Slots")
        # print(period_list)
        # print()
        # print("final_course list")
        # print(final_courses)
        # creating pse_1, pse_2, pse_3 to handle 3 credits

        # (variable,values)
        # timetable.addVariables(final_courses, period_list)
        # faculty, course, course_faculty, period_list
        for course in final_courses:
            timetable.addVariable(course,new_period_list(faculty,course,course_faculty,period_list))
        
        timetable.addConstraint(AllDifferentConstraint())
        for course1 in final_courses:
            for course2 in final_courses:
                # checking if they are of same subject
                if(course1[:-2] == course2[:-2] ):
                    if(course1 < course2):
                        timetable.addConstraint(unique_lec_per_day,(course1,course2))
        
        for course in final_courses:
            if(is_lab(course,courses)):
                # print(course)
                # timetable.addConstraint(lambda slot1,slot2: slot1[4:]=="10_12",(course,course))
                timetable.addConstraint(lab_constraint,(course,course))                   
    # print(courses, faculty)

        timetable_solutions = timetable.getSolution()
        if(timetable_solutions != None):
            # print("Max time ",maxTime)
            print(timetable_solutions)
            TimeTable_Excel_Maker.excel_maker(courses,timetable_solutions, department, semester, course_faculty, faculty)
            return timetable_solutions
        # print(timetable_solutions)
        # print(courses, faculty)
