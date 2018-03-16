# Importing hand-made modules.
# The name of the module corresponds to the 'mymodule.py' file in current directory.

import mymodule

mymodule.myfunc()
print(mymodule.s(8, 9))

# __name__ gives you the name of the current package. For the main script, it will be set to '__main__'.
# Inside a module, it will keep the name of a module (which is its namespace).
print(__name__)
