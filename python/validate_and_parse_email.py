# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
# COMPLETE

import re
from email.utils import parseaddr

username_match = "[a-zA-Z|\d][a-zA-Z0-9._-]+$"
website_match = "[a-zA-Z]+$"
extension_match = "[a-zA-Z]+$"
extension_length = 3


def validate_email(email):
    pattern = "[\w|\d][a-z0-9_-]+$"

    if "@" not in email:
        return False
    else:
        try:
            username, website_and_ext = email.split("@")
            website, ext = website_and_ext.split(".")
            if not re.match(username_match, username):
                return False

            elif not re.match(website_match, website):
                return False

            elif len(ext) > extension_length or not re.match(extension_match, ext):
                return False

            else:
                return True
        except ValueError:
            # split gone bad
            return False


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        try:
            name, email = input().split()
        except ValueError:
            continue

        if validate_email(parseaddr(email)[1]):
            print("{} {}".format(name, email))
