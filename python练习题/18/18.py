#!/usr/bin/python2
import os
def set_password(self,raw_password):
    import random
    algo = 'sha1'
    salt = get_hexdigset(algo,str(random.random()),str(random.random()))[:5]
    hsh = get_hexdigset(algo,salt,raw_password)
    self.password = '%s$%s$%s' % (algo,salt,hsh)

def check_password(raw_password,enc_password):
    algo,salt,hsh = enc_password.split('$')
    return hsh == get_hexdigset(algo,slat,raw_password)



