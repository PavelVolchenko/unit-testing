import unittest
from unittest.mock import Mock
from book_repository import BookRepository, Book
from book_service import BookService


class BookServiceTest(unittest.TestCase):

    def setUp(self):
        self.book_repository = Mock(BookRepository)
        self.book_service = BookService(self.book_repository)

    def test_find_book_by_id(self):
        id_book = 1
        book = Book(id_book, "Title", "Author")
        self.book_repository.find_by_id.return_value = book
        result = self.book_service.find_by_id(id_book)
        self.book_repository.find_by_id.assert_called_once_with(id_book)
        self.assertEqual(book, result)

    def test_find_all_books(self):
        books = [
            Book(1, "Title1", "Author1"),
            Book(2, "Title2", "Author2")
        ]
        self.book_repository.find_all.return_value = books
        result = self.book_service.find_all()
        self.book_repository.find_all.assert_called_once()
        self.assertEqual(books, result)


if __name__ == '__main__':
    unittest.main()
