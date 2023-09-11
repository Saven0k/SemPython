# Создайте класс Архив, который хранит пару свойств. Например, число и строку. При нового экземпляра класса,
# старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов, которые также являются свойствами экземпляра.

class Archiv:
    """
    class Archiv
    """
    instance = None

    def __init__(self, text: str, number: int) -> None:
        self.text = text
        self.number = number

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            cls.instance.old_text.append(cls.instance.text)
            cls.instance.old_number.append(cls.instance.number)
        else:
            cls.instance = super().__new__(cls)
            cls.instance.old_text = []
            cls.instance.old_number = []
        return cls.instance

    def __str__(self):
        """
        Function new
        :return: str
        """
        return f'text = {self.text}, number = {self.number}'

    def __repr__(self):
        """
        Function repr
        :return: str
        """
        return f'Archiv({self.text =}, {self.number} '


if __name__ == '__main__':
    a1 = Archiv('T', 1)
    a2 = Archiv('g', 2)
    a3 = Archiv('f', 3)

    print(a3.instance.old_text)
    print(a3.instance.old_number)
