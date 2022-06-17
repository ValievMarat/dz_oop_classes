class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        sum_rate = 0
        count_rate = 0
        for course_grade in self.grades.values():
            sum_rate += sum(course_grade)
            count_rate += len(course_grade)
        # если в списке ничего нет, чтобы не было деления на 0
        if count_rate == 0:
            count_rate = 1
        return round(sum_rate / count_rate, 1)

    def __str__(self):

        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.avg_grade()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            return (self.avg_grade() < other_student.avg_grade())
        else:
            return 'Error'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self):
        sum_rate = 0
        count_rate = 0
        for course_grade in self.grades.values():
            sum_rate += sum(course_grade)
            count_rate += len(course_grade)
        # если в списке ничего нет, чтобы не было деления на 0
        if count_rate == 0:
            count_rate = 1
        return round(sum_rate / count_rate, 1)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.avg_grade()}'

    def __lt__(self, other_lecture):
        if isinstance(other_lecture, Lecturer):
            return (self.avg_grade() < other_lecture.avg_grade())
        else:
            return 'Error'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'

#достаточно одной функции для средней оценки и лекторов, и студентов:
#и там, и там оценки хранятся в идентичном словаре grades
def avg_rate_course(mans, course):
    sum_rate = 0
    count_rate = 0

    for man in mans:
        if course in man.grades:
            sum_rate += sum(man.grades[course])
            count_rate += len(man.grades[course])

    if count_rate == 0:
        count_rate = 1

    return round(sum_rate / count_rate, 1)

#Ввод данных
#Студенты
best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['C++']

next_student = Student('John', 'Waltz', 'male')
next_student.courses_in_progress += ['Java']

#Менторы
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Java']

master_mentor = Mentor('Nikolay', 'Sokolov')
cool_mentor.courses_attached += ['Python']

#Ревьюеры
master_reviewer = Reviewer('Andy', 'Prohorov')
master_reviewer.courses_attached += ['Python']
master_reviewer.courses_attached += ['Java']

middle_reviewer = Reviewer('Jackie', 'Chan')
middle_reviewer.courses_attached += ['Java']

#Лекторы
senior_lecturer = Lecturer('Ivan', 'Abramov')
senior_lecturer.courses_attached += ['Python']
senior_lecturer.courses_attached += ['C++']
senior_lecturer.courses_attached += ['Java']

junior_lecturer = Lecturer('Stas', 'Pechkin')
junior_lecturer.courses_attached += ['Java']

#Оценки студентам
master_reviewer.rate_hw(best_student, 'Python', 10)
master_reviewer.rate_hw(best_student, 'Python', 9)
master_reviewer.rate_hw(best_student, 'Java', 9)

middle_reviewer.rate_hw(next_student, 'Java', 7)
middle_reviewer.rate_hw(next_student, 'Java', 6)

#Оценки лекторам от студенов
best_student.rate_lecturer(senior_lecturer, 'Python', 10)
best_student.rate_lecturer(junior_lecturer, 'Java', 4)

next_student.rate_lecturer(senior_lecturer, 'Java', 8)
next_student.rate_lecturer(junior_lecturer, 'Java', 5)

print(best_student)
print()

print(senior_lecturer)
print()

print(middle_reviewer)
print()

print('Сравнение')
print(best_student <  next_student) #False
print(junior_lecturer < senior_lecturer) #True
print()

print('Средняя оценка студентов по курсу Java:', avg_rate_course([best_student, next_student], 'Java'))
print('Средняя оценка лекторов по курсу Java:', avg_rate_course([senior_lecturer, junior_lecturer], 'Java'))