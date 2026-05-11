name= input("Student name:")
marks= int(input(" Enter marks:"))
if (marks>=90):
    print("grade A++")
    print("excellent!")
    print("outstanding performance,keep up the greate work")
elif (marks<90 and marks>=80):
    print("grade A+")
    print("very good!")
    print("you have done a greate job")
    print("keep aiming higher")
elif(marks<80 and marks>=75):
    print("grade A")
    print("Good job")
    print("a good result,but there is still room for movement")
elif(marks<75 and marks>=70):
    print("Grade A-")
    print("Nice effort!")
    print("you did weel,but try to improve further")
elif(marks<70 and marks>=65):
    print("Grade B")
    print("Satisfactory performance.")
    print("keep working  hard for better results")
elif(marks<65 and marks>=60):
    print("Grade B-")
    print("Fair performance")
    print("more attention and practice are needed")
elif(marks<60 and marks>=55):
    print("Grade C")
    print("Need improvement.")
    print("you should work harder to achieve better result")
elif(marks<55 and marks>=50):
    print("Grade C-")
    print("unsatisfactory performance.")
    print("more focus and dedication are required")
elif(marks<50 and marks>=40):
    print("Grade D")
    print("poor performance.")
    print("significant improvement and effort are needed")
else:
    print("grade F")
    print("fail.")
    print("you need to work much harder and try again with ditermination")