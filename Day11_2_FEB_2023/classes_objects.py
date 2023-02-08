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

#dunder
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
# class Movie:
#     year = 2018

#     def __init__(self, name, rating):
#         self.name = name
#         self.rating = rating


#     def movie_binder(self, splitc='|'):
#         return self.name + splitc + str(self.rating)

# movie_1 = Movie('shutter island', 8.0)
# movie_2 = Movie('avatar, 8.1')

# Movie.year = 2020 # updates the global year value, 
#                     #   all objects after this line will have the new value 2020

# movie_1.year = 2019


# print(Movie.__dict__)
# print(movie_1.__dict__)

# print(movie_1.year)
# print(movie_2.year)

# sample 4 - class variable / class methods --------------

# class Movie:
#     year = 2018

#     def __init__(self, name, rating):
#         self.name = name
#         self.rating = rating

#     @classmethod
#     def fromstring(cls, string):
#         name,rating = string.split('-')
#         return cls(name, rating) #Movie(name,rating)
    
#     @staticmethod
#     def simple_method(home):
#         return 'not called with object'


# movie_1 = Movie.fromstring('avatar-8.7')
# print(movie_1.name)

# print(movie_1.simple_method())
# print(Movie.simple_method())


# sample 5 ----- inheritance

# class Movie:
#     def __init__(self, name, rating):
#         self.name = name
#         self.rating = rating
    
#     def movie_binder(self):
#         print('movie')


# class Series(Movie):
#     def __init__(self, name,rating,seasons):
#         super().__init__(name,rating)
#         self.seasons = seasons


# house_of_dragons = Series('HOG','9.0','1')
# print(house_of_dragons.name)
# print(house_of_dragons.seasons)

# print(isinstance('house_of_dragons',str))
# print(isinstance(1,int))
# print(isinstance(house_of_dragons,Movie))

# print(issubclass(Movie,Series))


# sample 5 ----- inheritance
# special methods  __double__


class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __str__(self):
        return '*str*movie object where name - {}'.format(self.name)
    
    def __repr__(self):
        return '*repr*movie object where name - {}'.format(self.name)
    
    def __add__(obj1, obj2):
        average = (obj1.rating + obj2.rating) /2
        return average

    def __len__(obj1):          #Movie.__len__(s)
        return len(obj1.name)   #str.__len__(name)

    def __del__(obj):
        print(obj,'deleted')
        # print('obj - ',obj,' deleted')
        del obj

        

movie_1 = Movie('avatar', 8.0)
movie_2 = Movie('avatar2',7.5)
# print(movie_1.name)
# print(movie_1.rating)

# print(movie_1)

# print(movie_1 + movie_2) # Movie.__add__(obj,obj)

# print(len(movie_1))
del movie_1
print(movie_2)

