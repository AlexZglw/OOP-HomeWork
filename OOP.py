
import random

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress= []
        self.finished_courses = []
        self.grades = {}

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.average_grade()}
Курсы в процессе изучения : {", ".join(str(i) for i in self.courses_in_progress)}
Завершенные курсы : {", ".join(str(i) for i in self.finished_courses)}
"""

    def average_grade(self):
        if len(self.grades) > 0:
            count = 0
            for grades_list in self.grades.values():
                count += sum(grades_list) / len(grades_list)
            return round(count / len(self.grades), 1)
        else:
            return 'У студента пока нет оценок'

    def __lt__(self, other):
       print(f'Значения: {self.name} - {self.average_grade()}, {other.name} - {other.average_grade()}')

       if self.average_grade() < other.average_grade():
            answer = 'Нет!'
       else:
            answer = 'Да!'
       return f'Ответ: {answer}\n'


    def rate_hw(self, lecturer, course, grade):
       if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
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

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
     def __init__(self,name,surname):
       super().__init__(name,surname)
       self.grades = {}

     def __str__(self):
         print(f'Имя: {self.name}')
         print(f'Фамилия: {self.surname}')
         return f'Средняя оценка за лекции: {self.average_grade()}\n'

     def __lt__(self, other):

        print(f'Значения: {self.name} - {self.average_grade()}, {other.name} - {other.average_grade()}.')

        if self.average_grade() < other.average_grade():
            answer = 'Нет!'
        else:
            answer = 'Да!'
        return f'Ответ: {answer}\n'


     def average_grade(self):
         if len(self.grades) > 0:
             count = 0
             for grades_list in self.grades.values():
                 count += sum(grades_list) / len(grades_list)
             return round(count / len(self.grades), 1)
         else:
             return 'У лектора пока нет оценок'



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
    return f"""Имя:{self.name}
Фамилия:{self.surname}
"""




def avg_student_course(self, check_course, sum_grades=0, amount_grades=0):
    stud = all_student
    for i in range(len(all_student)):
        if check_course in all_student[i].courses_in_progress:
            amount_grades += len(all_student[i].grades.get(check_course))
            for grades in all_student[i].grades.get(check_course):
                sum_grades += grades
    return print(f'Средняя оценка студентов по предмету {check_course}: {round(sum_grades / amount_grades, 2)}')



def avg_lecturer_course(self, check_course, sum_grades=0, amount_grades=0):
    stud = all_lecturer
    for i in range(len(all_lecturer)):
        if check_course in all_lecturer[i].courses_attached:
            amount_grades += len(all_lecturer[i].grades.get(check_course))
            for grades in all_lecturer[i].grades.get(check_course):
                sum_grades += grades
    return print(f'Средняя оценка преподавателей по предмету {check_course}: {round(sum_grades / amount_grades, 2)}')




student_1 = Student('Alex', 'Tsiglov', 'Male')
student_2 = Student('Tim', 'Z', 'Male')
lector_1 = Lecturer('Some', 'Lector')
lector_2 = Lecturer('Oleg', 'Bulygin')
reviewer_1 = Reviewer('SomeRev', 'Number One')
reviewer_2 = Reviewer('SomeRev', 'Number Two')


student_1.finished_courses = ['Assembler']
student_2.finished_courses = ['GameDev', 'DevOps']
student_1.courses_in_progress = ['Git', 'Python', 'Telegram Bot']
student_2.courses_in_progress = ['Python', 'JS', 'React']
lector_1.courses_attached = ['Git', 'Python', 'JS']
lector_2.courses_attached = ['Python', 'Java']
reviewer_1.courses_attached = ['Git', 'Python']
reviewer_2.courses_attached = ['Python', 'Java']

student_1.rate_hw(lector_1, 'Python', random.randint(1, 5))
student_1.rate_hw(lector_2, 'Python', random.randint(1, 5))
student_2.rate_hw(lector_1, 'Python', random.randint(1, 5))
student_2.rate_hw(lector_2, 'JS', random.randint(1, 5))

reviewer_1.rate_hw(student_1, 'Python', random.randint(1, 5))
reviewer_1.rate_hw(student_2, 'Python', random.randint(1, 5))
reviewer_2.rate_hw(student_1, 'Python', random.randint(1, 5))
reviewer_2.rate_hw(student_2, 'JS', random.randint(1, 5))
print(student_1.__lt__(lector_1))
print(student_2.__lt__(lector_2))


all_student = [student_1, student_2]
all_lecturer = [lector_1, lector_2]

avg_lecturer_course(all_lecturer,"Python")
avg_student_course(all_student,"Python")



