# qa_python
Тестирование метода __init__ (4 теста):
test_books_genre_empty_dictionary_true(self)                # проверяем, что books_genre это пустой словарь
test_favorites_empty_list_true(self)                        # проверяем, что favorites это пустой список
test_genre_list_with_five_genres_true(self)                 # проверяем, что genre_list это список с пятью жанрами
test_genre_age_rating_list_with_two_genres_true(self)       # проверяем, что genre_age_rating это список с двумя жанрами
Тестирование остальных методов класса (8 тестов):
test_add_new_book_add_two_new_books_positive_result(self)
test_add_new_book_add_exist_book_not_added(self)
test_add_new_book_length_of_name_is_more_than_40_simbols_not_added(self)
test_set_book_genre_with_exist_name_and_exist_genre_positive_result(self)
test_get_books_with_specific_genre_with_exist_genre_positive_result(self, name, genre)
test_get_books_for_children_with_genre_is_not_age_rating_positive_result(self, name, genre)
test_add_book_in_favorites_with_new_favorite_name_positive_result(self)
test_delete_book_from_favorites_with_exist_name_positive_result(self)
