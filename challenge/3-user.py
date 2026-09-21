#!/usr/bin/python3
"""
 User Model
"""
import hashlib
import uuid


class User():
    """
    User class:
    - id: public string unique (uuid)
    - password: private string hash in MD5
    """

    __password = None

    def __init__(self):
        """
        Initialize a new user:
        - assigned an unique `id`
        """
        self.id = str(uuid.uuid4())

    @property
    def password(self):
        """
        Password getter
        """
        return self.__password

    @password.setter
    def password(self, pwd):
        """
        Password setter
        """
        if pwd is None or type(pwd) is not str:
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest()

    def is_valid_password(self, pwd):
        """
        Valid password
        """
        if pwd is None or type(pwd) is not str:
            return False

        if self.__password is None:
            return False

        return hashlib.md5(pwd.encode()).hexdigest() == self.__password