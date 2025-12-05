from lib.diary_entry import *

'''
Format returns:
A formatted diary entry, for example:
"My Title: These are the contents"

'''

def test_format_function_returns_formatted_entry():
    entry = DiaryEntry("Stardate 20251205", "These are the voyages")
    actual = entry.format()
    expected = "Stardate 20251205: These are the voyages"
    assert actual == expected


'''
count_words
Returns:
int: the number of words in the diary entry

'''

def test_count_words_returns_number_of_words_in_entry():
    entry = DiaryEntry("Stardate 20251205", "These are the voyages")
    actual = entry.count_words()
    expected = 6
    assert actual == expected   