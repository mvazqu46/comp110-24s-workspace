"""Ex06 Dict Unit Tests."""
__author__ = "730718822"


from exercises.ex05.dictionary import invert, favorite_color, alphabetizer, update_attendance


import pytest


def test_invert_use_case():
    """Test invert function with a normal dictionary."""
    my_dictionary = {'Matthew': 'Rogers', 'Alica': 'Walker'}
    inverted_dict = invert(my_dictionary)
    assert inverted_dict == {'Rogers': 'Matthew', 'Walker': 'Alicia'}

       
def test_invert_edge_case():
    """Test invert function with an empty dictionary."""
    with pytest.raises(KeyError):
        my_dictionary = {}
        invert(my_dictionary)


def test_invert_edge_case2():
    """Test invert function with another case."""
    my_dictionary = {'Joy': 'Jolly', 'Iris': 'Zavala', 'Stan': 'Smith'}
    inverted_dict = invert(my_dictionary)
    assert inverted_dict == {'Jolly': 'Joe', 'Zavala': 'Iris'}


def test_favorite_color_use_case():
    """Test favorite_color."""
    colors = {"Alyssa": ["Green"], "Drake": ["Green"], "Atthena": ["Blue"]}
    favcolor = "Green"
    popular = "Green"
    favorite_color(colors, favcolor, popular)
    assert colors == {"Alyssa": ["Green"], "Drake": ["Green"], "Athena": ["Blue"]}


def test_favorite_color_edge_case():
    """Test favorite_color."""
    colors = {"Alyssa": ["Green"], "Drake": ["Green"], "Atthena": ["Blue"]}
    favcolor = "Green"
    popular = "Green"
    favorite_color(colors, favcolor, popular)
    assert colors == {"Alyssa": ["Green"], "Drake": ["Green"], "Athena": ["Blue"]}


def test_favorite_color_edge_case2():
    """Test favorite color."""
    colors = {"Alyssa": ["Green"], "Drake": ["Green"], "Atthena": ["Blue"]}
    favcolor = "Green"
    popular = "Green"
    favorite_color(colors, favcolor, popular)
    assert colors == {"Alyssa": ["Green"], "Drake": ["Green"], "Athena": ["Blue"]}


def test_alphabetizer_use_case():
    """Test alphabetizer function with normal input."""
    oneword = {"April": ["marigold"], "June": ["carrots"]}
    letter = {}
    dictionary_words = ("cat", "apple", "boy", "angry", "bad", "car")
    alphabetized = alphabetizer(oneword, letter, dictionary_words)
    assert alphabetized == {"cat": [], "apple": [], "boy": [], "angry": [], "bad": [], "car": []}


def test_alphabetizer_edge_case():
    """Test alphabetizer function with an empty dictionary."""
    oneword = {}
    letter = {}
    dictionary_words = ("cat", "apple", "boy", "angry", "bad", "car")
    alphabetized = alphabetizer(oneword, letter, dictionary_words)
    assert alphabetized == {"cat": [], "apple": [], "boy": [], "angry": [], "bad": [], "car": []}


def test_alphabetizer_edge_case2():
    """Test alphabetizer function with an empty dictionary."""
    oneword = {}
    letter = {}
    dictionary_words = ("cat", "apple", "boy", "angry", "bad", "car")
    alphabetized = alphabetizer(oneword, letter, dictionary_words)
    assert alphabetized == {"cat": [], "apple": [], "boy": [], "angry": [], "bad": [], "car": []}


def test_update_attendance_use_case():
    """Test update_attendance function with normal input."""
    on_days = {"Monday", "Tuesday", "Wednesday"}
    students = ("Vrind", "Kaleb", "Alyssa")
    attendance = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    updated_attendance = update_attendance(on_days, students, attendance)
    assert updated_attendance == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Vrind"], "Wednesday": ["Kaleb", "Alyssa"]}


def test_update_attendance_edge_case():
    """Test update_attendance function with an empty attendance dictionary."""
    on_days = {"Monday", "Tuesday", "Wednesday"}
    students = ("Vrind", "Kaleb", "Alyssa")
    attendance = {}
    updated_attendance = update_attendance(on_days, students, attendance)
    assert updated_attendance == {"Monday": ["Vrind", "Kaleb", "Alyssa"], "Tuesday": ["Vrind", "Kaleb", "Alyssa"], "Wednesday": ["Vrind", "Kaleb", "Alyssa"]}


def test_update_attendance_edge_case2():
    """Test update_attendance function with an empty attendance dictionary."""
    on_days = {"Monday", "Tuesday", "Wednesday"}
    students = ("Vrind", "Kaleb", "Alyssa")
    attendance = {}
    updated_attendance = update_attendance(on_days, students, attendance)
    assert updated_attendance == {"Monday": ["Vrind", "Kaleb", "Alyssa"], "Tuesday": ["Vrind", "Kaleb", "Alyssa"], "Wednesday": ["Vrind", "Kaleb"]}