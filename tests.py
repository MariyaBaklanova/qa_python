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

    # Тест, что у добавленной книги пустой жанр
    def test_add_new_book_added_book_genre_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    # Тест на проверку, что книги с названием длиной из 0,41,42 не добавляются в словарь
    @pytest.mark.parametrize('book', ['',
                                      "Гордость и предубеждение и зомби. Продолж",
                                      "Гордость и предубеждение и зомби. Продолже"])
    def test_add_new_book_add_book_len_more_0_41_42_symbols_is_None(self, book):

        collector = BooksCollector()
        collector.add_new_book(book)
        assert collector.get_book_genre(book) is None

    # Тест на установку жанра из списка жанров книге, которая была добавлена
    def test_set_book_genre_existing_book_valid_genre_genre_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    # Тест на установку добавленной книге жанра, которого нет в списке жанров
    def test_set_book_genre_existing_book_invalid_genre_genre_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Семейный')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''


    # Проверяем получение словаря с книгами и жанрами
    def test_get_books_genre_have_got_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

    # Проверяем получение книг по жанру из существующих жанров
    def test_get_books_with_specific_genre_add_dict_success(self, collector):
        books = {
            'Гордость и предубеждение и зомби': 'Ужасы',
            'Созвездие': 'Фантастика',
            'Мизери': 'Ужасы',
            'Король и лев': 'Мультфильмы',
            'Нетопырь': 'Детективы'
        }
        for name, genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert ['Гордость и предубеждение и зомби', 'Мизери'] == collector.get_books_with_specific_genre('Ужасы')

    # Проверяем получение книг по некорреткному жанру
    def test_get_books_with_specific_genre_invalid_genre_failed(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert len(collector.get_books_with_specific_genre('Лирика')) == 0

    # Проверяем получение всей коллекции книг с жанрами
    def test_get_books_genre_success(self, collector):
        books = {
            'Гордость и предубеждение и зомби': 'Ужасы',
            'Созвездие': 'Фантастика',
            'Мизери': 'Ужасы'
        }
        for name, genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert books == collector.get_books_genre()

    # Проверяем, что метод get_book_genre возвращает ожидаемый жанр для книги
    @pytest.mark.parametrize('book, genre', [
        ('Гордость и предубеждение и зомби', 'Ужасы'),
        ('Нетопырь', 'Детективы'),
        ('Созвездие', 'Фантастика'),
    ])
    def test_get_book_genre_returns_expected_genre(self, book, genre):

        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == genre

    # Проверяем получение детских книг
    def test_get_books_for_children_success(self, collector):
        books = {'Гордость и предубеждение и зомби': 'Ужасы',
                 'Нетопырь': 'Детективы',
                 'Король и лев': 'Мультфильмы'}
        for name, genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == ['Король и лев']

    # Проверяем добавление книг в избранное
    def test_add_book_in_favorites_correct_name_success(self, collector):
        collector.add_new_book('Нетопырь')
        collector.add_book_in_favorites('Нетопырь')

        assert len(collector.get_list_of_favorites_books()) == 1

    # Проверяем удаление книги из избранного
    def test_delete_book_from_favorites_one_book_success(self, collector):
        collector.add_new_book('Нетопырь')
        collector.add_book_in_favorites('Нетопырь')
        collector.delete_book_from_favorites('Нетопырь')
        assert len(collector.get_list_of_favorites_books()) == 0


    # Проверяем получение списка избранных книг
    def test_get_list_of_favorites_books_success(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_new_book('Созвездие')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']


