# ===============================
# 1️⃣ Check Even or Odd
# ===============================
def is_even(num):
    """
    Return True if number is even, otherwise False.
    Example:
    is_even(4) -> True
    is_even(3) -> False
    """
    if num % 2 == 0:
        return True
    else:
        return False



# ===============================
# 2️⃣ Add Two Numbers
# ===============================
def add_numbers(a, b):
    """
    Return the sum of two numbers.
    Example:
    add_numbers(2,3) -> 5
    """
    return a+b



# ===============================
# 3️⃣ Find Largest of Two Numbers
# ===============================
def larger_number(a, b):
    """
    Return the larger of two numbers.
    Example:
    larger_number(5,3) -> 5
    """
    if a > b:
        return a
    else:
        return b


# ===============================
# 4️⃣ Count From 1 to n
# ===============================
def count_to_n(n):
    """
    Return a list of numbers from 1 to n.
    Example:
    count_to_n(4) -> [1,2,3,4]
    """
    return [i for i in range(1, n+1)]




# ===============================
# 5️⃣ Count Characters in String
# ===============================
def count_chars(text):
    """
    Return number of characters in a string.
    Example:
    count_chars("hello") -> 5
    """
    char_count = 0
    for i in text:
        for x in i:
            char_count += 1
    return char_count



# ===============================
# 6️⃣ Sum of List
# ===============================
def sum_list(numbers):
    """
    Return the sum of numbers in a list.
    Example:
    sum_list([1,2,3]) -> 6
    """
    total = 0
    for i in numbers:
        total += i
    return total
print(sum_list([1,2,3]))


# ===============================
# 7️⃣ Find First Element
# ===============================
def first_element(lst):
    """
    Return the first element of a list.
    Example:
    first_element([5,6,7]) -> 5
    """
    return lst[0]
    


# ===============================
# 8️⃣ Convert String to Uppercase
# ===============================
def make_upper(text):
    """
    Return the string converted to uppercase.
    Example:
    make_upper("hello") -> "HELLO"
    """
    return text.upper()



# ===============================
# 9️⃣ Check if Number is Positive
# ===============================
def is_positive(num):
    """
    Return True if number is positive, otherwise False.
    Example:
    is_positive(3) -> True
    is_positive(-1) -> False
    """
    if num > 0:
        return True
    else:
        return False



# ===============================
# 🔟 Reverse a String
# ===============================
def reverse_string(text):
    """
    Return the reversed version of the string.
    Example:
    reverse_string("abc") -> "cba"
    """
    return text[::-1]