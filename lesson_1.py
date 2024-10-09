class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, мне {self.age} лет.")


class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def show_marks(self):
        print(f"Оценки студента {self.name}:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")

    def calculate_average(self):
        return sum(self.marks.values()) / len(self.marks)


class Teacher(Person):
    base_salary = 30000

    def __init__(self, name, age, experience):
        super().__init__(name, age)
        self.experience = experience

    def calculate_salary(self):
        if self.experience > 3:
            bonus = (self.experience - 3) * 0.05 * Teacher.base_salary
        else:
            bonus = 0
        return Teacher.base_salary + bonus

    def show_info(self):
        print(f"Имя учителя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Опыт работы: {self.experience} лет")
        print(f"Зарплата: {self.calculate_salary():} рублей")


def create_students():
    student1 = Student("Алихан", 18, {"Математика": 4, "Физика": 5, "Обж": 3})
    student2 = Student("Бекжан", 15, {"Физра": 2, "Физика": 4, "Химия": 3})
    student3 = Student("Артур", 19, {"Истрория": 3, "Информатика": 4, "Геометрия": 5})
    student4 = Student("Kerimkazy", 16, {"Биалогия": 3, "Русский-язык": 4, "Черчения": 5})
    student5 = Student("Берк", 16, {"Секс-практика": 5, "География": 4, "Химия": 4})
    student6 = Student("Берк", 16, {"Алнебра": 3, "Английский-язык": 2, "Математика": 5})
    return [student1, student2, student3, student4, student5, student6]

teacher = Teacher("Алексей", 43, 13)
teacher.show_info()

print("\nИнформация об учениках:")

students_list = create_students()

for student in students_list:
    student.introduce()
    student.show_marks()

    average_mark = student.calculate_average()
    print(f"Средняя оценка: {average_mark:}")
    print("-" * 30)
