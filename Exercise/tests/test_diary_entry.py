from lib.diary_entry import *

example_contents_3_to_200 = "3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200"


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

def test_count_words_returns_six_in_entry_of_six_words():
    entry = DiaryEntry("Stardate 20251205", "These are the voyages")
    actual = entry.count_words()
    expected = 6
    assert actual == expected

'''
reading_time
Returns:
int: an estimate of the reading time in minutes for the contents at
the given wpm.

'''

def test_reading_time_returns_zero_point_one_for_six_words_at_60_wpm():
    entry = DiaryEntry("Stardate 20251205", "These are the voyages")
    actual = entry.reading_time(60)
    expected = 0.1
    assert actual == expected

def test_reading_time_returns_one_for_six_words_at_6_wpm():
    entry = DiaryEntry("Stardate 20251205", "These are the voyages")
    actual = entry.reading_time(6)
    expected = 1
    assert actual == expected

"""
reading_chunk
Returns:
string: a chunk of the contents that the user could read in the
given number of minutes

If called again, `reading_chunk` should return the next chunk,
skipping what has already been read, until the contents is fully read.
The next call after that should restart from the beginning.}}

"""

def test_reading_chunk_returns_first_50_words_for_100_wpm_30_sec():
    entry = DiaryEntry("1, 2", example_contents_3_to_200)
    actual = entry.reading_chunk(100, 0.5)
    expected = "1, 2 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,"
    assert actual == expected

def test_reading_chunk_returns_second_50_words_for_100_wpm_30_sec_on_second_call():
    entry = DiaryEntry("1, 2", example_contents_3_to_200)
    actual = entry.reading_chunk(100, 0.5)
    actual = entry.reading_chunk(100, 0.5)
    expected = "51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,"
    assert actual == expected