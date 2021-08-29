#This program finds phone numbers in strings that contain any

import re

phoneNumRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegEx.findall('Call me at 615-555-1010 tomorrow, or at 615-444-5566.'))
