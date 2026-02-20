import os
print("os module file location:")
print(os.__file__)

print("All available names in os module:")
for name in dir(os):
    print(name)