import unittest
from easy_revision import *

class TestEasyRevision(unittest.TestCase):

    # 1️⃣ Even check
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(3))

    # 2️⃣ Add numbers
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2,3), 5)
        self.assertEqual(add_numbers(-1,1), 0)

    # 3️⃣ Larger number
    def test_larger_number(self):
        self.assertEqual(larger_number(5,3), 5)
        self.assertEqual(larger_number(2,8), 8)

    # 4️⃣ Count to n
    def test_count_to_n(self):
        self.assertEqual(count_to_n(4), [1,2,3,4])

    # 5️⃣ Count characters
    def test_count_chars(self):
        self.assertEqual(count_chars("hello"), 5)

    # 6️⃣ Sum list
    def test_sum_list(self):
        self.assertEqual(sum_list([1,2,3]), 6)

    # 7️⃣ First element
    def test_first_element(self):
        self.assertEqual(first_element([5,6,7]), 5)

    # 8️⃣ Uppercase
    def test_make_upper(self):
        self.assertEqual(make_upper("hello"), "HELLO")

    # 9️⃣ Positive number
    def test_is_positive(self):
        self.assertTrue(is_positive(3))
        self.assertFalse(is_positive(-2))

    # 🔟 Reverse string
    def test_reverse_string(self):
        self.assertEqual(reverse_string("abc"), "cba")

if __name__ == "__main__":
    unittest.main()