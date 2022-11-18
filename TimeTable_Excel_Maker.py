import openpyxl

time_excel_coordinates = {
    'Mon_9_10' : ['B',7],
    'Mon_10_11' : ['B',10],
    'Mon_11_12' : ['B',13],
    'Mon_12_13': ['B',16],
    'Mon_13_14':['B',19],
    'Mon_14_15': ['B',22],
    'Mon_15_16': ['B',25],
    'Mon_16_17' : ['B',28],
    'Mon_17_18' : ['B',31],
    'Tue_9_10' : ['C',7],
    'Tue_10_11' : ['C',10],
    'Tue_11_12' : ['C',13],
    'Tue_12_13': ['C',16],
    'Tue_13_14':['C',19],
    'Tue_14_15': ['C',22],
    'Tue_15_16': ['C',25],
    'Tue_16_17' : ['C',28],
    'Tue_17_18' : ['C',31],
    'Wed_9_10' : ['D',7],
    'Wed_10_11' : ['D',10],
    'Wed_11_12' : ['D',13],
    'Wed_12_13': ['D',16],
    'Wed_13_14':['D',19],
    'Wed_14_15': ['D',22],
    'Wed_15_16': ['D',25],
    'Wed_16_17' : ['D',28],
    'Wed_17_18' : ['D',31],
    'Thu_9_10' : ['E',7],
    'Thu_10_11' : ['E',10],
    'Thu_11_12' : ['E',13],
    'Thu_12_13': ['E',16],
    'Thu_13_14':['E',19],
    'Thu_14_15': ['E',22],
    'Thu_15_16': ['E',25],
    'Thu_16_17' : ['E',28],
    'Thu_17_18' : ['E',31],
    'Fri_9_10' : ['F',7],
    'Fri_10_11' : ['F',10],
    'Fri_11_12' : ['F',13],
    'Fri_12_13': ['F',16],
    'Fri_13_14':['F',19],
    'Fri_14_15': ['F',22],
    'Fri_15_16': ['F',25],
    'Fri_16_17' : ['F',28],
    'Fri_17_18' : ['F',31]

}

def excel_maker(courses, period_dict, department, semester):
    print(f"Dept is {department}, sem is {semester} ")
    filename = f"{department}_Sem_{str(semester)}"
    wb = openpyxl.load_workbook(f'TimeTables/{filename}.xlsx')   
    sheet = wb.get_sheet_by_name('Sheet1')
    # if(department == "CSE" and semester == 5):
    #     wb = openpyxl.load_workbook('TimeTables/CSE_Sem_5.xlsx')   
    #     sheet = wb.get_sheet_by_name('Sheet1')

    # if(department == "CSE" and semester == 6):
    #     wb = openpyxl.load_workbook('TimeTables/CSE_Sem_6.xlsx')   
    #     sheet = wb.get_sheet_by_name('Sheet1')

    # if(department == "MECH" and semester == 5):
    #     wb = openpyxl.load_workbook('TimeTables/MECH_Sem_5.xlsx')   
    #     sheet = wb.get_sheet_by_name('Sheet1')

    # if(department == "MECH" and semester == 6):
    #     wb = openpyxl.load_workbook('TimeTables/MECH_Sem_6.xlsx')   
    #     sheet = wb.get_sheet_by_name('Sheet1')

    # if(department == "ENTC" and semester == 5):
    #     wb = openpyxl.load_workbook('TimeTables/ENTC_Sem_5.xlsx')   
    #     sheet = wb.get_sheet_by_name('Sheet1')

    # if(department == "ENTC" and semester == 6):
    #     wb = openpyxl.load_workbook('TimeTables/ENTC_Sem_6.xlsx')   
    #     sheet = wb.get_sheet_by_name('Sheet1')
    
    for key in period_dict:
        course = list(key.split('_'))
        course.pop(-1)
        course = '_'.join(course)
        course_short_name = courses[course][-1]
        day_time = period_dict[key]
        if(day_time in time_excel_coordinates):
            col = time_excel_coordinates[day_time][0]
            row = time_excel_coordinates[day_time][1]
            sheet[col + str(row)].value = course_short_name

        else:
            lab = list(day_time.split('_'))
            if(lab[1]=='10' and lab[2]=='12'):
                lab_1 = lab[0] + "_" + lab[1] + "_11"
                if(lab_1 in time_excel_coordinates):
                    col = time_excel_coordinates[lab_1][0]
                    row = time_excel_coordinates[lab_1][1]
                    sheet[col + str(row)].value = course_short_name
                lab_2 = lab[0] + "_11_" + lab[2]
                if(lab_2 in time_excel_coordinates):
                    col = time_excel_coordinates[lab_2][0]
                    row = time_excel_coordinates[lab_2][1]
                    sheet[col + str(row)].value = course_short_name

    wb.save(f'TimeTables/{filename}.xlsx')