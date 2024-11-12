#100DaysOfPythonChallenge video no.118
"""class User:
    pass
user_1 = User()
user_1.id = "001"
user_1.name = "Smruti"
print(user_1.name)
#this method is same for every object, attribute
user_2 =User()
user_2.id = "002"
user_2.name ="Charlien"
print(user_2.id)"""

#To reduce the code like the above, the constructor thing came:-initialising an object
#contructor is a part of the blueprint that allows us to specify what should happen when an object is being constructed
"""class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.nm = name
        self.followers = 0
user_1 = User("001", "Smruti", )
print(user_1.id)
print(user_1.nm)
print(user_1.followers)"""
#using method in class

## The __init__ method in Python is a special method called a constructor.
## __init__ method in Python is used to initialize objects of a class.
# It is automatically invoked when a new instance (object) of a class is created.
# The purpose of the __init__ method is to initialize the object’s attributes and perform any other setup necessary when an object is instantiated.
class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.nm = name
        self.followers = 0
        self.following =  0
    def follow(self, user):
        user.followers += 1#followers followed
        self.following += 1#self following to other users
user_1 = User("001", "Smruti")
user_2 = User("002", "Shanvi")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)






