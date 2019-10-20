import json
import re

Days = ("Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat")
print(json.dumps(Days))

txt = "data is the new oil"
z = re.search("data", txt)
print(z)