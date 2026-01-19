
from string_utils import StringUtils

utils = StringUtils()


def test_capitalize_first_letter():
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_already_capitalized():
    assert utils.capitalize("Skypro") == "Skypro"


def test_capitalize_empty_string():
    assert utils.capitalize("") == ""


def test_capitalize_only_symbol():
    assert utils.capitalize("1abc") == "1abc"


def test_trim_spaces():
    assert utils.trim("   skypro") == "skypro"


def test_trim_no_spaces():
    assert utils.trim("skypro") == "skypro"


def test_trim_only_spaces():
    assert utils.trim("   ") == ""


def test_trim_empty_string():
    assert utils.trim("") == ""


def test_contains_true():
    assert utils.contains("SkyPro", "S")


def test_contains_false():
    assert not utils.contains("SkyPro", "U")


def test_contains_empty_string():
    assert not utils.contains("", "a")


def test_contains_empty_symbol():
    assert utils.contains("SkyPro", "") is False


def test_delete_single_char():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_substring():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found():
    assert utils.delete_symbol("SkyPro", "X") == "SkyPro"


def test_delete_symbol_empty_string():
    assert utils.delete_symbol("", "a") == ""


def test_delete_symbol_empty_symbol():
    assert utils.delete_symbol("SkyPro", "") == "SkyPro"
