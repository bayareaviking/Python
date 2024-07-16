from pprint import pprint
import json
import os

print("- os.name")
print(os.name)

print("- os.listdir")
# pprint(os.listdir("/users/xavier/Downloads"))
pprint(os.listdir("c:\\Users\\Marcus\\Downloads"))

print("- os.getcwd")
print(os.getcwd())

print("- os.environ")
environ = os.environ
pretty_env = json.dumps(dict(environ), indent=2)
print(pretty_env)

print(os.getenv("HOMEPATH"))
print(os.environ["HOMEPATH"])

#print(os.getenv("TMPDIR"))
#print(os.environ["TMPDIR"])

print()