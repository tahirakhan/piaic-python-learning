
name = input("Enter Student Name: ")

total = int(input("Enter total marks of each subject: "))

engMarks = int(input("Enter marks in english: "))
urduMarks = int(input("Enter marks in urdu: "))
mathsMarks = int(input("Enter marks in maths: "))
sciMarks = int(input("Enter marks in science: "))
artsMarks = int(input("Enter marks in arts: "))


print("**********MARKS SHEET************")
print("Student Name : ", name)
print("English", '*********************', engMarks)
print("Urdu", '************************', urduMarks)
print("Maths", '***********************', mathsMarks)
print("Science", '*********************', sciMarks)
print("Arts", '************************', artsMarks)
totalMarks = engMarks + urduMarks + mathsMarks + sciMarks + artsMarks

print("Total Marks", '*****************', (totalMarks))
print("Average Marks", '***************', totalMarks*100/(total * 5) + "%")


# Enter Student Name: Tahir
# Enter total marks of each subject: 100
# Enter marks in english: 67
# Enter marks in urdu: 87
# Enter marks in maths: 76
# Enter marks in science: 55
# Enter marks in arts: 67
# **********MARKS SHEET************
# Student Name :  Tahir
# English ********************* 67
# Urdu ************************ 87
# Maths *********************** 76
# Science ********************* 55
# Arts ************************ 67
# Total Marks ***************** 352
# Average Marks *************** 70.4
