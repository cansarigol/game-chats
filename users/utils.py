# coding=utf-8
import hashlib
import random
import datetime

def generate_new_activation_key(email):
    salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
    return hashlib.sha1((salt + email).encode('utf-8')).hexdigest()