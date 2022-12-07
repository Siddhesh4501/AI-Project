import Inputs

print("Enter Branch for which you wish to generate Timetable - ")
print("1 for Computer Engineering, 2 for ENTC, 3 for Mechanical")
branch = int(input())

print("Enter Semester - ")
sem = int(input())

timetable = Inputs.function(branch, sem)

b = ""
if(branch == 1):
    b = "CSE"

if(branch == 2):
    b = "ENTC"

if(branch == 3):
    b = "MECH"

filename = f"{b}_Sem_{str(sem)}"

if(timetable):
    print("Your Timetable has been successfully generated please check Timetables folder for file -", filename)

