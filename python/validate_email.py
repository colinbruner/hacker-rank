# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
# COMPLETE

import re

username_match = "[\w|\d][a-z0-9_-]+$"
website_match = "[\w|\d][a-z0-9]+$"
extension_length = 3


def fun(s):
    if "@" not in s:
        return False
    else:
        try:
            username, website_and_ext = s.split("@")
            website, ext = website_and_ext.split(".")
            if not re.match(username_match, username):
                return False

            elif not re.match(website_match, website):
                return False

            elif len(ext) > extension_length:
                return False

            else:
                return True
        except ValueError:
            # split gone bad
            return False

    # return True if s is a valid email, else return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == "__main__":
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
