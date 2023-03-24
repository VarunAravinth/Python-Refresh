# why we need exception handling ?

# more specific except condition should be placed on top

# f = open('sample.txt')
# try:
#     #x = 10/0
#     f = open('sample.txt')

# except FileNotFoundError:
#     print('file not found...')

# except Exception:
#     print('Something went wrong, please try again...')



# --------- sample 2 ----------------------------------
# try:
#     # x = 10/0
#     f = open('sample.txt')

# except Exception as e:
#     print('Something went wrong, please try again...error = {}'.format(e))


# sample 3 -----------------------------
# try:
#     x = 0

# except Exception:
#     print('something went wrong..')

# else: # when you want send a notification for a successful try
#     print('runs only when try is successful.')

# finally:
#     print('always runs even if exception occurs or not..')


# # sample 4

# try:
#     x=10
#     if x == 10:
#         raise FileExistsError

# except FileExistsError:
#     print('file is already present')



    




