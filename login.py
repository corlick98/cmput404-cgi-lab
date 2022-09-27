#!/usr/bin/env python3

import cgi
import os
from templates import login_page, secret_page
from secret import username, password
import sys

def parse_cookies(cookie_string):
    cookies = cookie_string.split(';')
    result = {}
    for cookie in cookies:
        split_cookie = cookie.split('=')
        result[split_cookie[0]] = split_cookie[1]
    return result

cookies = parse_cookies(os.environ['HTTP_COOKIE'])

form = cgi.FieldStorage()

form_username = form.getfirst('username')
form_password = form.getfirst('password')

header = ""
header += 'Content-Type: text/html\r\n'

body = ""


if (form_username == username and form_password == password) or ('logged' in cookies and cookies['logged'] == 'true'):
    body += secret_page(form_username, form_password)
    header += "Set-Cookie: logged=true; Max-Age=60\r\n"
    header += "Set-Cookie: cookie=nom\r\n"
    body += "<h1>A terrible secret</h1>"

else:
    body += login_page()


print(header)
print()
print(body)