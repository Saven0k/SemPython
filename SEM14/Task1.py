# Задание №1
# оздайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_letters


def clean_text(text: str) -> str:
    """A function that removes characters from text other than latin letters and spaces.
        >>> clean_text('Some text, текст')
        'some text '

        >>> clean_text('Some milk in dog, 12312awdawd')
        'some milk in dog awdawd'

        >>> clean_text('Мама я хочу быть пиратом, Eyyy lets go!')
        '     eyyy let go'
        """
    return "".join(i for i in text if i in ascii_letters + " ").lower()

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    print(clean_text(text="Some text, тесь"))