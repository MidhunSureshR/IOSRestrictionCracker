"""
R Midhun Suresh
2017

version 0.1

A short python script to crack restriction password of IOS.
Much faster than using a browser.
To use this code, you will need to obtain the hash of the password and salt from your ios backup file.
This process is described in detail on http://ios7hash.derson.us
"""
import hashlib
import binascii
import base64
import threading


def get_hash(password_string, salt):
    """Function returns the PBKDF2-hmac-SHA1 result as a base 64 string.
    Args:
        password_string: The password to hash as string.
        salt: The salt to be used for hashing in base64 i.e as found on the backup file.
    Returns:
        The hash generated using the supplied salt as base64 encoded string along with a newline \n character
        at the end.
    """
    decoded_salt = base64.b64decode(bytes(salt))
    # print "Decoded salt is ", decoded_salt
    dk = hashlib.pbkdf2_hmac('sha1', bytes(password_string), decoded_salt, 1000)
    hash_to_string = binascii.b2a_base64(dk)
    return hash_to_string


def brute_force(known_hash, salt, start_index, end_index):
    """Function does the brute forcing by considering all possible passwords between start_index and end_index
       including them both. For each password it generates a hash using the supplied salt and compares the hash
       with the known_hash.
       Args:
            known_hash: The hash of the actual password as found on the backup file (viz the key).
            salt: The salt as found on the backup file.
            start_index: The lower bound of password to test.
            end_index: The upper bound of the password to test.
    """
    for i in range(start_index, end_index+1):
        pass_string = str(i)
        while len(pass_string) < 4:
            pass_string = "0" + pass_string
        generated_hash = get_hash(pass_string, salt)
        if generated_hash == known_hash:
            print "Password Found As ", pass_string
            break


def main():
        # The hash generated using get_hash function returns the hash with a newline character(\n) at the end.
        # Therefore \n character has been added to the input variable known_hash to enable string comparison.

        known_hash = raw_input("Enter the known hash:") + '\n'
        salt = raw_input("Enter the salt :")

        # Threading to increase brute force speed

        t = threading.Thread(target=brute_force, args=(known_hash, salt, 0, 5000))
        a = threading.Thread(target=brute_force, args=(known_hash, salt, 5001, 9999))
        t.start()
        a.start()


if __name__ == "__main__":
    main()



