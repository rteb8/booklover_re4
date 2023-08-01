import unittest
from booklover_pkg.booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        p1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        p1.add_book("War of the Worlds", 4)

        #Test
        testValue = "War of the Worlds" in p1.book_list['book_name'].values
         # error message in case if test case got failed
        message = "Test value is not true."
        # assetTrue() to check test value as true
        self.assertTrue(testValue, message)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        p1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        p1.add_book("War of the Worlds", 4)
        p1.add_book("War of the Worlds", 4)

        #Test
        testValue = p1.book_list[p1.book_list['book_name']=='War of the Worlds']['book_name'].value_counts()[0]
        actualValue = 1
         # error message in case if test case got failed
        message = "Test value is not 1"
        # assetEqual() to check test value as true
        self.assertEqual(testValue, actualValue, message)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        p1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        p1.add_book("War of the Worlds", 4)    

        #Test
        testValue = p1.has_read("War of the Worlds")
        # error message in case if test case got failed
        message = "Test value is not true."
        # assetTrue() to check test value as true
        self.assertTrue(testValue, message)
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        p1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        p1.add_book("War of the Worlds", 4)    

        #Test
        testValue = p1.has_read("Dune")
        # error message in case if test case got failed
        message = "Test value is not false."
        # assetFalse() to check test value as false
        self.assertFalse(testValue, message)
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        p1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        p1.add_book("War of the Worlds", 4) 
        p1.add_book("Dune", 2)
        p1.add_book("Dune Messiah", 3)

        #Test
        testValue = p1.num_books
        actualValue = 3
         # error message in case if test case got failed
        message = "Number of books doesn't actual number of books"
        # assetEqual() to check test value as true
        self.assertEqual(testValue, actualValue, message)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        p1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        p1.add_book("War of the Worlds", 4) 
        p1.add_book("Dune", 4)
        p1.add_book("Dune Messiah", 3)

        # Your test should check that the returned books have rating  > 3

        #Test
        testValue = all(p1.fav_books().book_rating > 3)
        # error message in case if test case got failed
        message = "Book ratings are not greater than 3."
        # assetTrue() to check test value as true
        self.assertTrue(testValue, message)
                
if __name__ == '__main__':
    unittest.main(verbosity=3)