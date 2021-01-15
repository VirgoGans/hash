#python 3.7.1


from __future__ import unicode_literals
import hashlib
import hmac
from base64 import b16encode
from base64 import b32encode
from base64 import b64encode
from binascii import hexlify
def b16_encode(item):
    """base16 encode"""
    try:
        return (b16encode(item.encode('utf-8'))).decode()
    except:
        return ''
def sha256(item):
    #sha256 hashing
    try:
        return (hashlib.sha256(item.encode("utf-8")).hexdigest())
    except:
        return ''
def sha516(item):
    #sha516 hashing
    try:
        return (hashlib.sha512(item.encode("utf-8")).hexdigest())
    except:
        return ''
def b32_encode(item):
    """base32 encode"""
    try:
        return (b32encode(item.encode('utf-8'))).decode()
    except:
        return ''
def b64_encode(item):
    """base64 encode"""
    try:
        return (b64encode(item.encode('utf-8'))).decode()
    except:
        return ''
def rsa_encode(item):
    """rsa algorithm and need modify code"""
    # replace your "n" and "e" hex value
    n_modulus_hex_string = 'd7190a042cd2db97ebc2ab4da366f2a7085556ed613b5a39c9fdd2bb2595d1dc'
    e_exponent_hex_string = '1091'

    if len(item) < 1:
        print("[!]exception item:[%s]" % item)
        return item
    public_modulus = int(n_modulus_hex_string, 16)
    public_exponent = int(e_exponent_hex_string, 16)
    item = int(hexlify(item[::-1].encode('utf-8')).decode(), 16)
    item = pow(item, public_exponent, public_modulus)
    return '%X' % item
def sha1_encode(item):
    """sha-1 message digest algorithm"""
    try:
        return hashlib.sha1(item.encode("utf-8")).hexdigest()
    except:
        return ''
def md516_encode(item):
    """md5 message digest algorithm output 16 char"""
    try:
        return hashlib.md5(item.encode("utf-8")).hexdigest()[8:-8]
    except:
        return ''
def sha512_encode(item):
    """sha-512 message digest algorithm"""
    try:
        return hashlib.sha512(item.encode("utf-8")).hexdigest()
    except:
        return ''
def hmac_encode(item):
    """hmac message digest algorithm"""
    key = "random_key_in_html_js_or_other_place_if_it_is_not_changed"
    item = md5_encode(item)
    return hmac.new(key.encode("utf-8"), item.encode("utf-8"), hashlib.md5).hexdigest()
a=input('Enter Text:')
print('\n sha1:',sha1_encode(a),'\n sha256:',sha256(a),'\n sha516:',sha516(a),'\n sha512_encode',sha512_encode(a))
print('\n b32_encode:',b32_encode(a),'\n b64_encode:',b64_encode(a),'\n rsa_encode:',rsa_encode(a),'\n sha1_encode:',sha1_encode(a),'\n md516_encode:',md516_encode(a))
