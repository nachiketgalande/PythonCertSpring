"""
Python decorator example

simple decorator that turns any function that returns a string
into one that returns that string wrapped in the html <p> tag:

@p_wrapper
def func():
    " simplest example possible"
    return "this is the returned string"

func()

"""

# the simple decorator

def p_wrapper(func):
    def function(*args, **kwargs):
        result = func(*args, **kwargs)
        return "<p>" + result + "</p>"
    return function


# fancy one using a class:
# this lets you make a decorator with some custom input
# the argument to the __init__ sets what tag you want
# this creates a custom decorator
# the __call__ method is the decorator itself.
class tag_wrapper(object):
    def __init__(self, tag='p' ):
        """
        inititilze the decorator class with the tag you want
        """
        self.open_tag = "<%s>"%tag
        self.close_tag = "</%s>"%tag

    def __call__(self, func, *args, **kwargs):
        """
        The actual decorator function.

        using lambda - 'cause why not?
        """
        return lambda *args, **kwargs: self.open_tag + func(*args, **kwargs) + self.close_tag


# give it a try:
if __name__ == "__main__":

    def func():
        " simplest example possible"
        return "this is the returned string"

    print "the raw version"

    print func()

    # now add the decorator:
    @p_wrapper
    def func():
        " simplest example possible"
        return "this is the returned string"

    print "the decorated version"

    print func()

    # try it with another function

    @p_wrapper
    def func2(x,y):
        return "the sum of %s and %s is %s"%(x, y, x+y)

    # call it:
    print func2(3,4)

    # and one with keyword arguments

    @p_wrapper
    def func2(x, y=4, z=2):
        return "the sum of %s and %s and %s is %s"%(x, y, z, x+y+z)

    # call it:
    print func2(3)
    print func2(3, 5)
    print func2(3, 5, 7)

    ## and try the class version:

    @tag_wrapper('h1')
    def func2(x, y=4, z=2):
        return "the sum of %s and %s and %s is %s"%(x, y, z, x+y+z)

    print func2(3,4)

    @tag_wrapper('div')
    def func2(x, y=4, z=2):
        return "the sum of %s and %s and %s is %s"%(x, y, z, x+y+z)

    print func2(5,6,7)


