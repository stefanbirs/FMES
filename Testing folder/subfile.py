# Subfile

#Class from subfile
class Hi: # Notice that class is in CamelCase
    """__init__: special method in python classes (aka: constructor)
    First method called when when an object is created in this class
    instantiates variables in the class
    """
    def __init__(self, name):
        """self refers to the newly created object.
        By using the "self" keyword we can access
        the attributes and methods of the class in python
        """
        self.name = name
    # Method
    def helloWorld(self):
        print("Hello" + " " + self.name)

class SampleClass(object):
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""
