# import mod1 as m

# var = m.mod1_a

# print(var)
# print(dir())

#-------------------------------------------------
# scenario2
# from mod1 import mod1_a, mod1_magic
# print(dir())
# print(mod1_a)
# mod1_magic()

#--------------------------------------------------
# scenario3
# from mod1 import *
# print(dir())

# mod1_magic()
# mod1_ordinary()
# print(mod1_a)

# --------------------------
#scenario4 -> with __all__ added in mod1.py

# from mod1 import *

# print(dir())

# -------------------------------
# import my_package
# print(dir())

# print(my_package.A)


# --------------------------------
#scenario
# import my_package.inner1 as in1
# print(dir())

# print(in1.inner1_a)

# --------------------------------------------
#scenario
# import my_package
# print(dir())

# print(my_package.inner1.inner1_a)


# -----------------------------------------
#scenario
from my_package import *

print(dir())
print(inner1.inner1_a)







