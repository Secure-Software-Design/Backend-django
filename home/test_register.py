from django.test import TestCase
import re

# coverage run -m pytest
# coverage report

def student_register(inputUsername, password, inputEmail):
    patternUsername = "^[a-zA-Z0-9_-]{3,15}$"
    patternEmail = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
    
    username = re.findall(patternUsername, inputUsername)
    email = re.findall(patternEmail, inputEmail)

    print(username, email, password)
    if len(password) > 20 or len(password) < 5 or len(email) == 0 or len(username) == 0 :
        return False

    return True


def student_login(error):
    
    print("Mock call to DB to search for student login information")
    if error:
        return True
    else:
        return False


# Create your tests here.

def test_register_good_data():
    assert student_register('semaphore', 'StrongPassw0rd*', "good@email.com") == True


def test_register_bad_username():
    assert student_register('Ju', 'StrongPassw0rd*', "good@email.com") == False


def test_register_bad_password():
    assert student_register('semaphore', 'ok*', "good@email.com") == False


def test_register_bad_email():
    assert student_register('semaphore', 'StrongPassw0rd*', "bad") == False


def test_login():
    assert student_login(True) == True


def test_login_failure():
    assert student_login(False) == False
