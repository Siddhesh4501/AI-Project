import pandas as pd
import CSP

def function(branch, semester):
 
    facultyDataFrame = pd.read_excel('AI - Timetable.xlsx', sheet_name = 'Faculty')
    coursesDataFrame = pd.read_excel('AI - Timetable.xlsx', sheet_name = 'Courses')
    
    compDepartment = dict()
    entcDepartment = dict()
    mechDepartment = dict()

    final_list = [facultyDataFrame['Teacher_id'].tolist(), facultyDataFrame['Teacher_name'].tolist(), facultyDataFrame['Department'].tolist(), facultyDataFrame['Time_from'].tolist(), facultyDataFrame['Time_to'].tolist()]

    for id in facultyDataFrame['Teacher_id'].tolist():
        dept = list(id.split('_'))[0]
        if(dept == 'CS'):
            compDepartment[id] = []
        if(dept == 'ENTC'):
            entcDepartment[id] = []
        if(dept == 'MECH'):
            mechDepartment[id] = []

    for i in range(len(facultyDataFrame['Teacher_id'].tolist())):
        dept = list(final_list[0][i].split('_'))[0]
        if(dept == 'CS'):
            compDepartment[final_list[0][i]] += [facultyDataFrame['Department'].tolist()[i], facultyDataFrame['Teacher_name'].tolist()[i], facultyDataFrame['Time_from'].tolist()[i], facultyDataFrame['Time_to'].tolist()[i], []]
        if(dept == 'ENTC'):
            entcDepartment[final_list[0][i]] += [facultyDataFrame['Department'].tolist()[i], facultyDataFrame['Teacher_name'].tolist()[i], facultyDataFrame['Time_from'].tolist()[i], facultyDataFrame['Time_to'].tolist()[i], []]
        if(dept == 'MECH'):
            mechDepartment[final_list[0][i]] += [facultyDataFrame['Department'].tolist()[i], facultyDataFrame['Teacher_name'].tolist()[i], facultyDataFrame['Time_from'].tolist()[i], facultyDataFrame['Time_to'].tolist()[i], []]

    final_list_2 = [coursesDataFrame['Teacher_id'].tolist(), coursesDataFrame['Course_id'].tolist(), coursesDataFrame['Course_name'].tolist(), coursesDataFrame['Semester'].tolist(), coursesDataFrame['Duration'].tolist(), coursesDataFrame['Credits'].tolist()]

    for i in range(len(coursesDataFrame['Teacher_id'].tolist())):
        dept = list(final_list_2[0][i].split('_'))[0]
        if(dept == 'CS'):
            compDepartment[final_list_2[0][i]][-1] += [[coursesDataFrame['Course_id'].tolist()[i]]]
        if(dept == 'ENTC'):
            entcDepartment[final_list_2[0][i]][-1] += [[coursesDataFrame['Course_id'].tolist()[i]]]
        if(dept == 'MECH'):
            mechDepartment[final_list_2[0][i]][-1] += [[coursesDataFrame['Course_id'].tolist()[i]]]

    # Each department is a dictionary with key being the Teacher_id and value is a list of - 
    # Department, Teacher name, time from, time to, courses list
    """print("Computer Department Faculty : ",compDepartment)
    print()
    print("ENTC Department Faculty : ", entcDepartment)
    print()
    print("Mechanical Department Faculty : ",mechDepartment)
    print()"""

    courses_dict = dict()

    for i in range(len(coursesDataFrame['Teacher_id'].tolist())):
        if(coursesDataFrame['Course_id'].tolist()[i] not in courses_dict):
            courses_dict[coursesDataFrame['Course_id'].tolist()[i]] = [coursesDataFrame['Course_name'].tolist()[i], coursesDataFrame['Credits'].tolist()[i], coursesDataFrame['Duration'].tolist()[i], coursesDataFrame['Semester'].tolist()[i]]

    # Courses Dictionary contains course ID as key and value is a list of course name, credits, duration, semester

    # print("Courses Dictionary : ",courses_dict)

    if(branch == 1):
        comp_courses_acc_sem = dict()

        for key in courses_dict:
            dept = list(key.split('_'))[0]
            if(dept == 'CSE'):
                if(courses_dict[key][3] == semester):
                    comp_courses_acc_sem[key] = courses_dict[key]

        CSP.generator_fn(compDepartment, comp_courses_acc_sem)

    elif(branch == 2):
        entc_courses_acc_sem = dict()

        for key in courses_dict:

            dept = list(key.split('_'))[0]
            if(dept == 'ENTC'):
                if(courses_dict[key][3] == semester):
                    entc_courses_acc_sem[key] = courses_dict[key]

        CSP.generator_fn(entcDepartment, entc_courses_acc_sem)

    else:
        mech_courses_acc_sem = dict()

        for key in courses_dict:

            dept = list(key.split('_'))[0]
            if(dept == 'MECH'):
                if(courses_dict[key][3] == semester):
                    mech_courses_acc_sem[key] = courses_dict[key]

        CSP.generator_fn(mechDepartment, mech_courses_acc_sem)

