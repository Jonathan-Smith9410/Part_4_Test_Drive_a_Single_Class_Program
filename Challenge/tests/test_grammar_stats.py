from lib.grammar_stats import *
import pytest

# Tests for check() function duplicated from Unit 3 exercise 2 (test_verify_text.py) 

"""
check() returns:
An error with an empty string:
"""

def test_throws_error_on_empty_string():
    document = GrammarStats()
    with pytest.raises(Exception) as e:
        document.check("")
    error_message = str(e.value)
    assert error_message == "Input text required."

"""
check() returns:
True if string beign with capital letter and ends in one of '.?")',
False in any other combination of those
"""

def test_string_starts_with_uppercase_and_ends_with_punctuation():
    document = GrammarStats()
    assert document.check("Hello this is a test.") == True

def test_string_starts_with_uppercase_and_does_not_end_with_punctuation():
    document = GrammarStats()
    assert document.check("Hello this is a test") == False

def test_string_starts_with_lowercase_and_ends_with_punctuation():
    document = GrammarStats()
    assert document.check("hello this is a test.") == False

def test_string_starts_with_lowercase_and_does_not_end_with_punctuation():
    document = GrammarStats()
    assert document.check("hello this is a test") == False


# percentage_good() returns:
# int: the percentage of texts checked so far that passed the check
# defined in the `check` method. The number 55 represents 55%.
"""
percentage_good()
Returns error if asked to return value with no tests run
"""

def test_throws_error_if_no_checks_performed():
    document = GrammarStats()
    with pytest.raises(Exception) as e:
        document.percentage_good()
    error_message = str(e.value)
    assert error_message == "Can't calculate percentage if no checks run."

"""
percentage_good()
Returns 100 if one test run correctly
"""
def test_returns_100_with_one_correct_check_out_of_one():
    document = GrammarStats()
    document.check("Hello this is a test.")
    assert document.percentage_good() == 100

"""
percentage_good()
Returns 100 if two tests run correctly
"""
def test_returns_100_with_two_correct_checks_out_of_two():
    document = GrammarStats()
    document.check("Hello this is a test.")
    document.check("Hello this is also a test.")
    assert document.percentage_good() == 100

"""
percentage_good()
Returns 50 if one test run correctly and one incorrectly
"""
def test_returns_50_with_one_correct_check_out_of_two():
    document = GrammarStats()
    document.check("Hello this is a test.")
    document.check("Hello this is also a test")
    assert document.percentage_good() == 50

"""
percentage_good()
Returns 33 if one test run correctly and two incorrectly
"""
def test_returns_33_with_one_correct_check_out_of_three():
    document = GrammarStats()
    document.check("Hello this is a test.")
    document.check("Hello this is also a test")
    document.check("Hello this is a third test")
    assert document.percentage_good() == 33

"""
percentage_good()
Returns 0 if one test run incorrectly
"""
def test_returns_0_with_one_correct_checks_out_of_one():
    document = GrammarStats()
    document.check("Hello this is a test")
    assert document.percentage_good() == 0
"""
percentage_good()
Returns 0 if two tests run incorrectly
"""
def test_returns_0_with_no_correct_checks_out_of_two():
    document = GrammarStats()
    document.check("Hello this is a test")
    document.check("Hello this is also a test")
    assert document.percentage_good() == 0