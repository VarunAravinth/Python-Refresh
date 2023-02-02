# string='sample'

# string = str('sample')
# print(string)

# class Movie:
#     pass


# movie_1 = Movie()
# movie_1.name = 'Shutter Island'
# movie_1.rating = 8.0
# movie_1.director = 'Martin Scorsese'

# movie_2 = Movie()
# movie_2.name = 'Pulp Fiction'
# movie_2.rating = 8.7
# movie_2.director = 'QT'


# print(movie_1.rating)


# sample 2
# __init__ -> constructor

# class Movie:
#     def __init__(self, name, rating):
#         self.name = name
#         self.rating = rating

# movie_1 = Movie('shutter island', 8.0)
# movie_2 = Movie('avatar',8.1)

# print(movie_2.name)

# sample 3
# instance method
# instance attributes

# class Movie:
#     def __init__(self, name, rating):
#         self.name = name
#         self.rating = rating
    
#     def movie_binder(self, splitc='|'):
#         return self.name + splitc + str(self.rating)

# movie_1 = Movie('shutter island', 8.0)
# print(movie_1.movie_binder())



# sample 4
class Movie:
    year = 2018

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating


    def movie_binder(self, splitc='|'):
        return self.name + splitc + str(self.rating)

movie_1 = Movie('shutter island', 8.0)
movie_2 = Movie('avatar, 8.1')

Movie.year = 2020 # updates the global year value, 
                    #   all objects after this line will have the new value 2020

movie_1.year = 2019


print(Movie.__dict__)
print(movie_1.__dict__)

print(movie_1.year)
print(movie_2.year)















