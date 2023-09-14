# Задание. Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# - Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# - Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

class Student:
    """
    Class Student
    """

    def __init__(self, full_name: str):
        self.objects = []
        self.grades = []
        self.points = []
        if full_name.istitle():
            self.full_name = full_name
        else:
            raise ValueError("Not all words start with a capital letter")

        with open('Students.csv', 'r') as f:
            data = f.read().split('\n')[1:]
            for i in data:
                i = i.split(',')
                self.objects.append(i[0])
                self.grades.append(i[1])
                self.points.append(i[2])

    @property
    def get_grades(self):
        return self.grades

    @property
    def get_objects(self):
        return self.objects

    @property
    def get_points(self):
        return self.points

    @property
    def get_GPA(self):
        data = dict(zip(self.objects, self.grades))
        for k, v in data.items():
            d = []
            for i in v:
                if i.isnumeric():
                   d.append(int(i))
            data[k] = d
        for k, v in data.items():
            data[k] = round(sum(v) / len(v), 2)
        return data

    @property
    def get_average_points(self):
        data = dict(zip(self.objects, self.points))
        for k, v in data.items():
            d = []
            for i in v:
                if i.isnumeric():
                    d.append(int(i))
            data[k] = d
        for k, v in data.items():
            data[k] = round(sum(v) / len(v), 2)
        return data

if __name__ == '__main__':
    s = Student("Roman Gabriel Domov")
    print(s.get_GPA)
    print(s.get_average_points)
