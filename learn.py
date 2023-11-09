# def main():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         n = int(input("What is n?"))
#         if n > 0:
#             break
#     return n

# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()

# students = {"Hermione" : "Gryffindor", 
#             "Harry" : "Gryffindor", 
#             "Ron" : "Gryffindor", 
#             "Draco" : "Slytherin"}

# for student in students:
#     print(student, students[student], sep=", ")

# students = [
#     {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
#     {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
#     {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Jack Russel terrier"},
#     {"name" : "Draco", "house" : "Slytherin", "patronus" : None}
# ]

# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep=", ")

# while True:
#     try:
#         x = int(input("What is x? "))

#     except ValueError:
#         print("x is not an integer")
#     else:
#         break

# print(f"x is {x}")

