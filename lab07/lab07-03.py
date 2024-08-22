class ClassRoom:
    def __init__(self, 
        grade: int=0, 
        homeRoomTeacher: str="",
        studentList=[],
        numStudents: int=0
        ):

        self.grade = grade
        self.homeRoomTeacher = homeRoomTeacher
        self.studentList = studentList
        self.numStudents = numStudents

    def set_homeroom_teacher(self, homeRoomTeacher: str):
        self.homeRoomTeacher = homeRoomTeacher

    def set_grade(self, grade: int):
        self.grade = grade

    def set_student_list(self, std_ls):
        self.studentList = std_ls

    def set_num_student(self, n_std):
        self.numStudents = n_std

    def get_grade(self) -> int:
        return self.grade
    
    def get_homeroom_teacher(self) -> str:
        return self.homeRoomTeacher
    
    def get_student_list(self):
        return self.studentList
    
    def get_num_student(self) -> int:
        return self.numStudents

    def get_student_no(self, n) -> str:
        return self.studentList[n-1]
    
    def add_student(self, new_name) -> bool:
        if(self.numStudents==9):
            return False
        else:
            self.studentList.append(new_name)
            self.numStudents += 1
            return True
        
    def change_student(self, n: int, new_name: str) -> bool:
        if(0 < n <= len(self.studentList)):
            self.studentList[n-1] = new_name
            return True
        else:
            return False
        
    def remove_student(self, student_name: str) -> bool:
        if(student_name in self.studentList):
            self.numStudents -= 1
            self.studentList.remove(student_name)
            return True
        else:
            return False
        
    def remove_student_no(self, n: int) -> bool:
        if(0< n <= len(self.studentList)):
            self.studentList.pop(n-1)
            self.numStudents -= 1
            return True
        else:
            return False
        
    def __str__(self) -> str:
        txt = ", ".join(self.studentList)
        return f"Grade: {self.grade}\nHomeroom Teacher: {self.homeRoomTeacher}\nStudents: {txt}"
    
room1 = ClassRoom()
grade = int(input("Input grade: "))
homeRoomTeacher = input("Homeroom Teacher: ")
room1.set_grade(grade)
room1.set_homeroom_teacher(homeRoomTeacher)
print(room1)

noStudent = int(input("Number of students: "))
studentList = room1.get_student_list()
room1.set_student_list(studentList)
print(room1)

for i in range(noStudent):
    temp = input(f"Student No{i+1}: ")
    if not room1.add_student(temp):
        print("Exceed 10 students.")
print(room1)
print("Grade", room1.get_grade())
print("Homeroom Teacher", room1.get_homeroom_teacher())
for i in range(room1.get_num_student()):
    print(f"No.{i+1}: {room1.get_student_no(i+1)}")

# test change_student
print(">>>>>> Testing change student")
if room1.change_student(room1.get_num_student(), "Abby"):
    print(room1)
if not room1.change_student(room1.get_num_student() + 2, "Abby"):
    print(f"Cannot change {room1.get_num_student()+2}th student")
if not room1.change_student(13, "Abby"):
    print("Index out of bound. Cannot change 13th student.")
if not room1.change_student(-1, "Abby"):
    print("Index out of bound. Cannot change -1th student.")

# test remove_student(name)
print(">>>>>> Testing remove student (name)")
if room1.get_num_student() >= 1:
    room1.remove_student(room1.get_student_no(1))
    print(room1)
if room1.get_num_student() >= 1:
    room1.remove_student(room1.get_student_no(room1.get_num_student()))
    print(room1)
if room1.get_num_student() >= 3:
    room1.remove_student(room1.get_student_no(2))
    print(room1)

# test remove_student(int)
print(">>>>>> Testing remove student no.")
room1.add_student("Bob")
room1.add_student("Mary")
room1.add_student("Adam")
if room1.get_num_student() >= 1:
    if room1.remove_student_no(1):
        print(room1)
    if not room1.remove_student_no(8):
        print(f"8 is invalid student number. There are only {room1.get_num_student()} students.")
if room1.get_num_student() >= 1:
    room1.remove_student_no(room1.get_num_student())
    print(room1)
if room1.get_num_student() >= 3:
    room1.remove_student_no(2)
    print(room1)
if room1.get_num_student() >= 3:
    room1.remove_student_no(2)
    print(room1)
if not room1.remove_student_no(-2):
    print("Index out of bound. Cannot remove -2th student.")
if not room1.remove_student_no(12):
    print("Index out of bound. Cannot remove 12th student.")