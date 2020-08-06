from re import search, compile

# pattern = compile("search")
# string = "Text to be search by regex search"

# matched = pattern.search(string)
# print(matched.group())
# print(pattern.findall(string))
# print(pattern.match(string))


# pattern = compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# string = "viking@gmail.com"

# print(pattern.search(string))

password = compile(r"([a-zA-Z0-9$%#@]{7,}[0-9]{1,}$)")
string = "1234567ssss1"

print(password.search(string))
