from flask import session
import bcrypt
import hashlib
import base64


# generates random characters to use as salt default is 64
def generate_nonce(length: int=64) -> str:
    salt = ""
    while len(salt) < length:
        salt += hashlib.sha3_256(str(bcrypt.gensalt()).encode('utf-8')).hexdigest()
    return salt[0:length]


# checks the password vs the hashed password
def hash_password(password, as_string=True, gensalt_rounds=12):

    normalized = normalize_password(password).encode('utf-8')

    hashed = bcrypt.hashpw(normalized, bcrypt.gensalt(gensalt_rounds))
    if as_string:
        return str(hashed, 'utf-8')
    else:
        return hashed


def check_password_hash(pword, pw_hash):
    if type(pw_hash) == str:
        pw_hash = pw_hash.encode('utf-8')
    normalized = normalize_password(pword).encode('utf-8')
    return bcrypt.checkpw(normalized, pw_hash)


def normalize_password(password):
    if type(password) == bytes:
        password = str(password, 'utf-8')
    encoded_password = password.encode('utf-8')
    hashed_encoded = hashlib.sha256(encoded_password).digest()
    b64_encoded = base64.b64encode(hashed_encoded)
    return str(b64_encoded, 'utf-8')


def logged_in(route):
    # print(type(route))
    # print(session)
    pass
