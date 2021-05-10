class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.middle_grade = []
        self.middle_grade_course = []

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lc(self, lecturer, course, grade_lc):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_lc:
                lecturer.grades_lc[course] += [grade_lc]
            else:
                lecturer.grades_lc[course] = [grade_lc]
        else:
            return 'Ошибка'

    def mid_gr(self):
        a = 0
        grades = self.grades
        for value in grades.values():
            a += sum(value)
        self.middle_grade = round(a / (len(grades)), 1)
        return self.middle_grade

    def __lt__(self, other):
        return self.r > other.r

    def __eq__(self, other):
        return self.r == other.r

    def mid_gr_course(self, students, course):
        a = []
        for dict in students:
            a.append(sum(dict[course]))
        self.middle_grade_course = round(sum(a) / (len(students)), 1)
        return self.middle_grade_course

    def __str__(self):
        res = (f'СТУДЕНТ\nИмя: {self.name}\nФамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {self.middle_grade}\n'
               f'Курсы в процессе изучения: {self.courses_in_progress}\n'
               f'Завершенные курсы: {self.courses_in_progress}')
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lc = {}
        self.middle_grade_lc = []
        self.middle_grade_lectures = []

    def mid_gr(self):
        a = 0
        grades_lc = self.grades_lc
        for value in grades_lc.values():
            a += sum(value)
        self.middle_grade_lc = round(a / (len(grades_lc)), 1)
        return self.middle_grade_lc

    def __lt__(self, other):
        return self.r > other.r

    def __eq__(self, other):
        return self.r == other.r

    def mid_gr_lectures(self, lecturers, course):
        a = []
        for dict in lecturers:
            a.append(sum(dict[course]))
        self.middle_grade_lectures = round(sum(a) / (len(lecturers)), 1)
        return self.middle_grade_lectures

    def __str__(self):
        res = (f'ЛЕКТОР\nИмя: {self.name}\n'
              f'Фамилия: {self.surname}\n'
              f'Средняя оценка за лекции: {self.middle_grade_lc}')
        return res

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'ПРОВЕРЯЮЩИЙ\nИмя: {self.name}\nФамилия: {self.surname}'
        return res

some_student_1 = Student('Jason', 'Statham', 'male')
some_student_1.courses_in_progress += ['Python', 'Git', 'Java']

some_student_2 = Student('Vin', 'Diesel', 'male')
some_student_2.courses_in_progress += ['Python', 'Git', 'Java']

some_reviewer_1 = Reviewer('Brus', 'Willis')
some_reviewer_1.courses_attached += ['Python', 'Git', 'Java']

some_reviewer_2 = Reviewer('Dwayne', 'Johnson')
some_reviewer_2.courses_attached += ['Python', 'Git', 'Java']

some_lecturer_1 = Lecturer('Silvester', 'Stallone')
some_lecturer_1.courses_attached += ['Python', 'Git', 'Java']

some_lecturer_2 = Lecturer('Arnold', 'Schwarzenegger')
some_lecturer_2.courses_attached += ['Python', 'Git', 'Java']

some_reviewer_1.rate_hw(some_student_1, 'Python', 5)
some_reviewer_1.rate_hw(some_student_1, 'Git', 6)
some_reviewer_1.rate_hw(some_student_1, 'Java', 10)

some_reviewer_2.rate_hw(some_student_2, 'Python', 2)
some_reviewer_2.rate_hw(some_student_2, 'Git', 3)
some_reviewer_2.rate_hw(some_student_2, 'Java', 7)

some_student_1.rate_lc(some_lecturer_1, 'Python', 8)
some_student_1.rate_lc(some_lecturer_1, 'Git', 7)
some_student_1.rate_lc(some_lecturer_1, 'Java', 10)

some_student_2.rate_lc(some_lecturer_2, 'Python', 8)
some_student_2.rate_lc(some_lecturer_2, 'Git', 9)
some_student_2.rate_lc(some_lecturer_2, 'Java', 2)

some_student_1.mid_gr()
some_student_2.mid_gr()
some_lecturer_1.mid_gr()
some_lecturer_2.mid_gr()
some_student_1.mid_gr_course([some_student_1.grades, some_student_2.grades], 'Python')
some_lecturer_1.mid_gr_lectures([some_lecturer_1.grades_lc, some_lecturer_2.grades_lc], 'Python')

print('Сравним кто из студентов круче по среднему баллу: ')
compare_lt = (some_student_1.middle_grade > some_student_2.middle_grade)
compare_eq = (some_student_1.middle_grade == some_student_2.middle_grade)
if compare_eq == True:
    print(f'Бывает и такое - оба студента одинаково круты - {some_student_1.middle_grade} балла у обоих!\n')
elif compare_lt == True:
    print(f'Ого! {some_student_1.surname} ({some_student_1.middle_grade} балла) '
          f'круче {some_student_2.surname}({some_student_2.middle_grade} балла)!\n')
else:
    print(f'Ого! {some_student_2.surname} ({some_student_2.middle_grade} балла) '
          f'круче {some_student_1.surname} ({some_student_1.middle_grade} балла)!\n')

print('Сравним кто из лекторов круче по среднему баллу: ')
compare_lt = (some_lecturer_1.middle_grade_lc > some_lecturer_2.middle_grade_lc)
compare_eq = (some_lecturer_1.middle_grade_lc == some_lecturer_2.middle_grade_lc)
if compare_eq == True:
    print(f'Бывает и такое - оба лектора одинаково круты - {some_lecturer_1.middle_grade_lc} балла у обоих!\n')
elif compare_lt == True:
    print(f'Ого! {some_lecturer_1.surname} ({some_lecturer_1.middle_grade_lc} балла) '
          f'круче {some_lecturer_2.surname}({some_lecturer_2.middle_grade_lc} балла)!\n')
else:
    print(f'Ого! {some_lecturer_2.surname} ({some_lecturer_2.middle_grade_lc} балла) '
          f'круче {some_lecturer_1.surname} ({some_lecturer_1.middle_grade_lc} балла)!\n')

print(f'Оценки студента: {some_student_1.name} {some_student_1.surname} {some_student_1.grades}.')
print()
print(f'Оценки студента: {some_student_2.name} {some_student_2.surname} {some_student_2.grades}.')
print()
print(f'Оценки лектора: {some_lecturer_1.name} {some_lecturer_1.surname} {some_lecturer_1.grades_lc}.')
print()
print(f'Оценки лектора: {some_lecturer_2.name} {some_lecturer_2.surname} {some_lecturer_2.grades_lc}.')
print()
print(some_student_1)
print()
print(some_student_2)
print()
print(some_lecturer_1)
print()
print(some_lecturer_2)
print()
print(some_reviewer_1)
print()
print(some_reviewer_2)
print()
print(f'Средняя оценка за д/з по всем студентам одного курса:\n{some_student_1.middle_grade_course}')
print()
print(f'Средняя оценка за лекции по всем лекторам одного курса:\n{some_lecturer_1.middle_grade_lectures}')