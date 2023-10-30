class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}


    def srgr(self):
        grades_count = 0
        if not self.grades:
            return 0
        for k in self.grades:
            grades_count += len(self.grades[k])
            self.average_rating = sum(map(sum, self.grades.values())) / grades_count

        return round(self.average_rating, 1)


    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)

        res = f'Имя:{self.name}\n' \
              f'Фамилия:{self.surname}\n' \
              f'Средняя оценка за домашнее задание:{self.srgr()}\n' \
              f'Курсы в процессе обучени:{courses_in_progress_string}\n' \
              f'Завершенные курсы:{finished_courses_string}'
        return res


    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):

        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}


class Lecturer(Mentor):
    def srgr(self):
        grades_count = 0
        if not self.grades:
            return 0
        for k in self.grades:
            grades_count += len(self.grades[k])
            self.average_rating = sum(map(sum, self.grades.values())) / grades_count

        return round(self.average_rating, 1)


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.srgr()}'
        return res


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_in_progress += ['Python']
some_lecturer.courses_attached += ['Python']


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.courses_attached += ['Python']
some_student.finished_courses += ['Введение в программирование']


some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(some_lecturer, 'Python', 9.6)
some_student.rate_hw(some_lecturer, 'Python', 10)

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9.6)
some_reviewer.rate_hw(some_student, 'Python', 10)



print(f'У проверяющих:\n {some_reviewer}\n')
print(f'У лекторов:\n {some_lecturer}\n')
print(f'У студентов: \n {some_student}\n')








