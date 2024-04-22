import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_books_genre_empty_dictionary_true(self):
        collector1 = BooksCollector()
        assert collector1.get_books_genre() == {}

    def test_favorites_empty_list_true(self):
        collector2 = BooksCollector()
        assert collector2.get_list_of_favorites_books() == []

    def test_genre_list_with_five_genres_true(self):
        collector3 = BooksCollector()
        five_genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector3.genre == five_genre

    def test_genre_age_rating_list_with_two_genres_true(self):
        collector4 = BooksCollector()
        two_genre = ['Ужасы', 'Детективы']
        assert collector4.genre_age_rating == two_genre

    def test_add_new_book_add_two_new_books_positive_result(self):
        collector5 = BooksCollector()
        collector5.add_new_book('Коллекционер')
        collector5.add_new_book('Трагедия счастья')
        assert len(collector5.get_books_genre()) == 2

    def test_add_new_book_add_exist_book_not_added(self):
        collector6 = BooksCollector()
        collector6.add_new_book('Коллекционер')
        collector6.add_new_book('Коллекционер')
        assert len(collector6.get_books_genre()) == 1

    def test_add_new_book_length_of_name_is_more_than_40_simbols_not_added(self):
        collector7 = BooksCollector()
        collector7.add_new_book('Бабушка велела кланяться и передать, что просит прощения')
        assert len(collector7.get_books_genre()) == 0

    def test_set_book_genre_with_exist_name_and_exist_genre_positive_result(self):
        collector8 = BooksCollector()
        collector8.add_new_book('Человек-амфибия')
        collector8.set_book_genre('Человек-амфибия', 'Фантастика')
        assert collector8.get_book_genre('Человек-амфибия') == 'Фантастика'

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Коллекционер', 'Ужасы']
        ]
    )
    def test_get_books_with_specific_genre_with_exist_genre_positive_result(self, name, genre):
        collector9 = BooksCollector()
        collector9.add_new_book(name)
        collector9.set_book_genre(name, genre)
        assert collector9.get_books_with_specific_genre('Ужасы') == ['Коллекционер']

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Трагедия счастья', 'Комедии']
        ]
    )
    def test_get_books_for_children_with_genre_is_not_age_rating_positive_result(self, name, genre):
        collector10 = BooksCollector()
        collector10.add_new_book(name)
        collector10.set_book_genre(name, genre)
        assert collector10.get_books_for_children() == ['Трагедия счастья']

    def test_add_book_in_favorites_with_new_favorite_name_positive_result(self):
        collector11 = BooksCollector()
        collector11.add_new_book('Трагедия счастья')
        collector11.add_book_in_favorites('Трагедия счастья')
        assert collector11.get_list_of_favorites_books() == ['Трагедия счастья']

    def test_delete_book_from_favorites_with_exist_name_positive_result(self):
        collector12 = BooksCollector()
        collector12.add_new_book('Трагедия счастья')
        collector12.add_book_in_favorites('Трагедия счастья')
        collector12.delete_book_from_favorites('Трагедия счастья')
        assert collector12.get_list_of_favorites_books() == []
