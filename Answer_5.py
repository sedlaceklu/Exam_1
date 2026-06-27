from exam_lib import Book


class Ebook(Book):

    def __init__(self, title, author, pages, size, registration_code):
        super().__init__(title=title, author=author, pages=pages)

        self.size = size
        self._registration_code = registration_code if self.check_code(registration_code) else None

    @staticmethod
    def check_code(registration_code):
        return type(registration_code) == str and len(registration_code) == 16

    @property
    def registration_code(self):
        return self._registration_code

    @registration_code.setter
    def registration_code(self, registration_code):
        if self.check_code(registration_code):
            self._registration_code = registration_code


if __name__ == "__main__":
    ebook = Ebook(
        "Exam",
        "Lukas",
        100,
        10,
        "1234567890123456"
    )

    print(ebook.registration_code)

    ebook.registration_code = "1111222233334444"
    print(ebook.registration_code)

    ebook.registration_code = "123"
    print(ebook.registration_code)

    print(Ebook.check_code("1234567890123456"))
    print(Ebook.check_code("123"))

    ebook2 = Ebook(
        "Book",
        "Author",
        150,
        5,
        "123"
    )

    print(ebook2.registration_code)