""" Verify that make_full_name , extract_family_name, and extract_given_name work correctly """

from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """
    assert make_full_name("Francky", "Ntyam") == "Ntyam; Francky"
    assert make_full_name("Anna", "harrison") == "Harrison; Anna"
    assert make_full_name("george", "Washington") == "Washington; George"
    assert make_full_name("william", "harrison") == "Harrison; William"

def test_extract_family_name():
    """Verify that the extract_family_name function work correctly.
    Parameters: none
    Return: nothing
    """
    assert extract_family_name("Ntyam; Francky") == "Ntyam"
    assert extract_family_name("Harrison; Anna") == "Harrison"
    assert extract_family_name("Washington; ") == "Washington"
  

def test_extract_given_name():
    """Verify that the extract_given_name function work correctly.
    Parameters: none
    Return: nothing
    """
    assert extract_given_name("Ntyam; Francky") == "Francky"
    assert extract_given_name("Harrison; Anna") == "Anna"
    assert extract_given_name("Washington; ") == ""




# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])