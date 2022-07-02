
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
