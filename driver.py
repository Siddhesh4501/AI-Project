import Inputs

print("Enter Branch for which you wish to generate Timetable - ")
print("1 for Computer Engineering, 2 for ENTC, 3 for Mechanical")
branch = int(input())

print("Enter Semester - ")
sem = int(input())

timetable = Inputs.function(branch, sem)
print(timetable)

