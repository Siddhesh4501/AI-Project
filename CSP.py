from constraint import *

# Courses Dictionary contains course ID as key and value is a list of course name, credits, duration, semester
def parse(courses):
    final_lst = []
    for key in courses.keys():
        credits = courses[key][1]
        subject = key
        for i in range(credits):
            tmp = subject + "_" + str(i)
            final_lst.append(tmp)
    return final_lst

def is_lab(course,courses):
    if(int(courses[course[:-2]][-2])==2):
        return True
    return False

# lab should be only scheduled in the given time slot
def lab_constraint(slot,_):
    return slot[4:] == "10_12"

# i.e. only one lec of a subject per day
def unique_lec_per_day(slot1,slot2):
    return slot1[:3] != slot2[:3]

def generator_fn(faculty, courses,course_faculty):
    # print("printing courses")
    # print(courses)
    # print()
    # print("printing faculty")
    # print(faculty)
    # print()
    # print("printing course_faculty")
    # print(course_faculty)
    
    timetable = Problem()

    # Assuming college timimgs are 9:00 AM - 6:00 PM, Mon - Fri

    # Mon_9 means lacture on Monday from 9:00 AM - 10:00 AM

    period_list = []

    for day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']:
        for time in range(9,18):
            a = None
            if time == 10:
                a = day + "_" + str(time) + "_" +str(time+2)
            else:
                a = day + "_" + str(time) + "_" +str(time+1)
            
            if(time != 11 or time != 12):
                period_list.append(a)

    # print()
    # print("Slots")
    # print(period_list)
    final_courses = parse(courses)
    # print()
    # print("final_course list")
    # print(final_courses)
    # creating pse_1, pse_2, pse_3 to handle 3 credits

    # (variable,values)
    timetable.addVariables(final_courses, period_list)
    timetable.addConstraint(AllDifferentConstraint())
    for course1 in final_courses:
        for course2 in final_courses:
            if(course1[:7] == course2[:7] ):
                if(course1 < course2):
                    # timetable.addConstraint(lambda slot1,slot2: slot1[:3] != slot2[:3],(course1,course2))
                    timetable.addConstraint(unique_lec_per_day,(course1,course2))
    
    for course in final_courses:
        if(is_lab(course,courses)):
            # print(course)
            # timetable.addConstraint(lambda slot1,slot2: slot1[4:]=="10_12",(course,course))
            timetable.addConstraint(lab_constraint,(course,course))
                    
    
    timetable_solutions = timetable.getSolution()
    print(timetable_solutions)
    # print(courses, faculty)

# generator_fn("ffd","fd")