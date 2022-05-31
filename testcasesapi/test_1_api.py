import pytest
import requests
from utilities import utils

# https://demoqa.com/swagger/None
url = 'https://demoqa.com/BookStore/v1/Books'

def test_get_employee_details_check_status_code_equals_200():
    response = requests.get(url)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

def test_negative_test_case():
    varResponse = requests.get(url)
    newVar = varResponse.json()
    assert 'books' in newVar

def test_print_elements_from_dict():
    varResponse = requests.get(url)
    newVar = varResponse.json()
    print(newVar)

def test_print_elements_from_dict3():
    varResponse = requests.get(url)
    newVar = varResponse.json()
    for key, value in newVar.items():
        print(key, value)
        dict1el = (value[0])
        print(dict1el)
        for eleme in dict1el.values():
            print(eleme)
            if 'Richard E. Silverman' in dict1el.values():
                print("Imame takova choveche")
            else:
                print("Nemame takova choveche")

def test_checkingSum():
    assert 4+4==8

def test_checkingSum1():
    assert 4+4==8

def test_checkingSum2():
    assert 4+4==8

def test_checkingSum3():
    assert 4+4==8

def test_checkingSum4():
    assert 4+4==8

def test_checkingSum5():
    assert 4+4==8

def test_checkingSum6():
    assert 4+4==8

def test_checkingSum7():
    assert 4+4==8

def test_checkingSum8():
    assert 4+4==8

def test_checkingSum9():
    assert 4+4==8

def test_checkingSum10():
    assert 4+4==8
