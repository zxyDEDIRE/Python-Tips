import re

pattern = re.compile("a(.*?)a",re.S)
test = "asdfsdfsda"
all = re.findall(pattern,test)
print(all)