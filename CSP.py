from constraint import *

def generator_fn(faculty, courses):

    timetable = Problem()

    # Assuming college timimgs are 8:00 AM - 6:00 PM, Mon - Fri

    # Mon_8 means lacture on Monday from 8:00 AM - 9:00 AM

    period_list = []

    for day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']:
        for time in range(8,19):
            a = day + "_" + str(time)
            period_list.append(a)

    timetable.addVariables(period_list, list(courses.keys()))

    # timetable_solutions = timetable.getSolutions()

    print(courses, faculty)