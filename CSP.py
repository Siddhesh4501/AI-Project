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

# checks if the course is a Lab course
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

# creating a time_slots considering faculty availability 
def new_time_slots_list(faculty, course, course_faculty, period_list):
    time_slots_lst = []
    course_name = course[:-2]
    faculty_name = course_faculty[course_name]
    
    available_start = faculty[faculty_name][2]
    available_end = faculty[faculty_name][3]
    for slots in period_list:
        lst = slots.split("_")
        start = int(lst[1])
        end = int(lst[2])
        # only appending if the teacher is available
        if(start >= available_start and end <= available_end):
            time_slots_lst.append(slots)
    return time_slots_lst
        
# function which adds Constraints
def generator_fn(faculty, courses,course_faculty, department, semester):
   
    # to handle number of classes in a week
    final_courses = parse(courses)
    left = 10 + ceil((len(final_courses) + 5)/5) + 1
    # To build a balanced timetable
    for max_time in range(left,18):
        
        timetable = Problem()

        # Assuming college timimgs are 10:00 AM - 6:00 PM, Mon - Fri

        # Mon_10_11 means lecture on Monday from 10:00 AM - 11:00 AM

        period_list = []
        # defining values that is lecture slots in our case
        for day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']:
            for time in range(10,max_time): 
                a = None
                if time == 10:
                    a = day + "_" + str(time) + "_" +str(time+2)
                else:
                    a = day + "_" + str(time) + "_" +str(time+1)
                # lunch break
                if(time != 11 and time != 12):
                    period_list.append(a)

        # (variable,values)
        for course in final_courses:
            timetable.addVariable(course,new_time_slots_list(faculty,course,course_faculty,period_list))
        
        timetable.addConstraint(AllDifferentConstraint())
        for course1 in final_courses:
            for course2 in final_courses:
                # checking if they are of same subject
                if(course1[:-2] == course2[:-2] ):
                    if(course1 < course2):
                        timetable.addConstraint(unique_lec_per_day,(course1,course2))
        
        for course in final_courses:
            if(is_lab(course,courses)):
                timetable.addConstraint(lab_constraint,(course,course))                   

        timetable_solutions = timetable.getSolution()
        if(timetable_solutions != None):
            # print("Max time ",max_time)
            # print(timetable_solutions)
            # outpting the obtained solution in excel sheet
            TimeTable_Excel_Maker.excel_maker(courses,timetable_solutions, department, semester, course_faculty, faculty)
            return timetable_solutions
    print("No solutions satisfying constraints exist")