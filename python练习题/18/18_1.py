#!/usr/bin/python2
import os
from hashlib import sha256
from hmac import HMAC
def encrypt_password(password,salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8)
        print salt

    assert 8 == len(salt)
    assert isinstance(salt,str)

    if isinstance(password,unicode):
        password = password.encode('ascii')

    assert isinstance(password,str)

    result = password

    for i in xrange(10):
            result = HMAC(result,salt,sha256).digest()

    return salt + result

cache=encrypt_password("mo")
