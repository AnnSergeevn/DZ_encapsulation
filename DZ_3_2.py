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


    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.srgr() < other.srgr()


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


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.srgr() < other.srgr()


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


best_lecturer_1 = Lecturer('Some', 'Buddy')
best_lecturer_1 .courses_in_progress += ['Python']
best_lecturer_1 .courses_attached += ['Python']


best_lecturer_2 = Lecturer('Petr', 'Petrov')
best_lecturer_2.courses_attached += ['Java']
best_lecturer_2 .courses_in_progress += ['Java']

best_lecturer_3 = Lecturer('Semen', 'Zarev')
best_lecturer_3.courses_attached += ['Python']
best_lecturer_3 .courses_in_progress += ['Python']

some_rewiewer= Reviewer('Some', 'Buddy')
some_rewiewer.courses_attached += ['Python']
some_rewiewer.courses_attached += ['Java']




student_1 = Student('Denis', 'Sviridov', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_attached += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Roman', 'Malikov', 'your_gender')
student_2.courses_in_progress += ['Java']
student_2.courses_attached += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Sidor', 'Petrov', 'your_gender')
student_3.courses_in_progress += ['Python']
student_3.courses_attached += ['Python']
student_3.finished_courses += ['Введение в программирование']


student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 9)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_2.rate_hw(best_lecturer_2, 'Java', 10)
student_2.rate_hw(best_lecturer_2, 'Java', 8)
student_2.rate_hw(best_lecturer_2, 'Java', 9)

student_3.rate_hw(best_lecturer_3, 'Python', 5)
student_3.rate_hw(best_lecturer_3, 'Python', 6)
student_3.rate_hw(best_lecturer_3, 'Python', 7)

some_rewiewer.rate_hw(student_1, 'Python', 8)
some_rewiewer.rate_hw(student_1, 'Python', 9)
some_rewiewer.rate_hw(student_1, 'Python', 10)


some_rewiewer.rate_hw(student_2, 'Java', 8)
some_rewiewer.rate_hw(student_2, 'Java', 7)
some_rewiewer.rate_hw(student_2, 'Java', 9)

some_rewiewer.rate_hw(student_3, 'Python', 8)
some_rewiewer.rate_hw(student_3, 'Python', 7)
some_rewiewer.rate_hw(student_3, 'Python', 9)
some_rewiewer.rate_hw(student_3, 'Python', 8)
some_rewiewer.rate_hw(student_3, 'Python', 7)
some_rewiewer.rate_hw(student_3, 'Python', 9)

student_list = [student_1, student_2, student_3]

lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]
print(f'У проверяющих:\n {some_rewiewer}\n')
print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}\n')
print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}\n')

for i in student_list:
    for j in student_list[1:]:
        print(f'Результат сравнения студентов(по средним оценкам за ДЗ): '
      f'{i.name} {i.surname} < {j.name} {j.surname} ={i > j}')



for i in lecturer_list:
    for j in lecturer_list[1:]:
        print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{i.name} {i.surname} < {j.name} {j.surname} = {i > j}')


