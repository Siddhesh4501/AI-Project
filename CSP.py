from constraint import *

def generator_fn(faculty, courses):

    timetable = Problem()

    # Assuming college timimgs are 9:00 AM - 6:00 PM, Mon - Fri

    # Mon_9 means lacture on Monday from 9:00 AM - 10:00 AM

    period_list = []

    for day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']:
        for time in range(9,18):
            a = day + "_" + str(time)
            period_list.append(a)

    print(period_list)
    timetable.addVariables(period_list, list(courses.keys()))

    # timetable_solutions = timetable.getSolutions()

    # print(courses, faculty)