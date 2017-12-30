# IOSRestrictionCracker
A bruteforce attack script to find the IOS restriction password from PBKDF2-hmac-sha1 algorithm and salt.

## Working Mechanism
IOS stores their restriction password using a strong PBKDF2-hmac-sha1 method which is strong. However the key space (the possible passwords) is within the range [0000,9999]. This script hashes each possible password using the salt and compares it to the  key extracted from the ios backup file. The script takes a maximum of about 10 seconds to crack the password for worst-case scenario (when password is 9999).

## Usage Documentation
This is a python script which means that you will need to install python on your machine to run this script. You will also need to access the file from ios backup which stores the hashed key and base64 encoded salt. For a step by step instruction on getting the files you can go [here](http://ios7hash.derson.us/).
Run the script and follow the instructions and the password should be cracked pretty fast.

## Credits
Thanks to Magnum and philsmd who identified the hashing mechanism. You can read about it [here](https://hashcat.net/forum/thread-2892.html)
Thanks to creator of http://ios7hash.derson.us/ for providing details on getting the required file. The website , although slow and time consuming , can crack the password through a webbrowser!
