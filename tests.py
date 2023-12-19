import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def test_add_new_book_and_genre_true(self):
        collector = BooksCollector()
        book_name = "Морской бой"
        genre = "Фантастика"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.get_book_genre(book_name) == genre


    def test_init_genre_true(self):
        collector = BooksCollector()
        expected_genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre == expected_genre


    def test_init_genre_age_rating_true(self):
        collector = BooksCollector()
        expected_genre_age_rating = ['Ужасы', 'Детективы']
        assert collector.genre_age_rating == expected_genre_age_rating


    @pytest.mark.parametrize('book_name, expected_result', [("", False), ("Первому игроку приготовиться", True), ("Клуб любителей книг и пирогов из картофельных очистков", False)])
    def test_add_new_book_different_lengths_of_names_adding_that_meets_the_conditions_true(self,book_name, expected_result):
        collector = BooksCollector()
        result = collector.add_new_book(book_name)
        assert (book_name in collector.get_books_genre()) == expected_result


    def test_get_book_genre_true(self):
        collector = BooksCollector()
        book_name = "Слово пацана"
        genre = "Детективы"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre


    def test_get_books_with_specific_genre_returns_only_the_requested_books_in_genre(self):
        collector = BooksCollector()
        genre = "Комедии"
        books = ["1+1", "Горе от ума", "Ревизор"]
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        specific_books = collector.get_books_with_specific_genre(genre)
        assert specific_books == books


    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        books_genre = collector.get_books_genre()
        assert isinstance(books_genre, dict)


    def test_get_books_for_children_true(self):
        collector = BooksCollector()
        collector.add_new_book("Красная шапочка")
        collector.set_book_genre("Красная шапочка", "Мультфильмы")
        collector.add_new_book("Горе от ума")
        collector.set_book_genre("Горе от ума", "Комедии")
        collector.add_new_book("Загадочный сад")
        collector.set_book_genre("Загадочный сад", "Детективы")
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Ужасы")

        books_for_children = collector.get_books_for_children()

        expected_result = ["Красная шапочка", "Горе от ума"]

        assert books_for_children == expected_result


    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()

        collector.add_new_book("Красная шапочка")
        collector.set_book_genre("Красная шапочка", "Мультфильмы")
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Ужасы")

        collector.add_book_in_favorites("Красная шапочка")
        collector.add_book_in_favorites("1984")

        expected_result = ["Красная шапочка", "1984"]
        favorites = collector.get_list_of_favorites_books()

        assert favorites == expected_result

    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()

        collector.add_new_book("Красная шапочка")
        collector.set_book_genre("Красная шапочка", "Мультфильмы")
        collector.add_new_book("Горе от ума")
        collector.set_book_genre("Горе от ума", "Комедии")
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Ужасы")

        collector.add_book_in_favorites("Красная шапочка")
        collector.add_book_in_favorites("Горе от ума")
        collector.add_book_in_favorites("1984")

        collector.delete_book_from_favorites("Горе от ума")

        expected_result = ["Красная шапочка", "1984"]
        favorites = collector.get_list_of_favorites_books()

        assert favorites == expected_result


    def test_get_list_of_favorites_books_true(self):
        collector = BooksCollector()

        collector.add_new_book("Горе от ума")
        collector.set_book_genre("Горе от ума", "Комедии")
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Ужасы")

        collector.add_book_in_favorites("Горе от ума")
        collector.add_book_in_favorites("1984")

        favorites = collector.get_list_of_favorites_books()

        expected_result = ["Горе от ума", "1984"]

        assert favorites == expected_result