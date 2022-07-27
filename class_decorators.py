from functools import partial

class AddOneFunction():
    """Decorator to add one to a functions output
    """
    def __init__(self, func) -> None:
        """
        Decorators are essentially just the function being decorated passed
        into the decorator class. eg -> AddOneFunc(add).
        So we store the function in a variable aptly named ``func``
        """
        self.func = func

    def __call__(self, *args, **kwargs):
        """
        This dunder method will now be called whenever our decorated function
        is called. We simply want to grab the output and add 1
        """
        output = self.func(*args, **kwargs)
        return output + 1

@AddOneFunction
def add(a: int, b: int) -> int:
    return a+b

### But lets say that you want to add this decorator to some methods of a
### class with the same decorator, you'll notice that python complains
### about an argument missing, this is because we need to pass the Class
### Instance to the method call.
### Typically we name this ``self`` and don't need to explicitly pass it when
### calling methods that are attatched to instances. In our case, the decorator
### is not calling that method with the knowledge of the calling instance.
class AddOneMethod(AddOneFunction):
    """
    We already have a working decorator, lets just extend it to
    add the method we need to make it work for a method
    """
    def __get__(self, instance, owner):
        """
        Having this dunder now makes this a ``descriptor`` and is important
        to make this work. In short, this adds in the methods Class Instance
        as the first argument to the *args in the above __call__ method.
        Effectively adding in the ``self`` param to the methods call as
        the first arg.
        """
        return partial(self.__call__, instance)

class Caclulator():

    @AddOneMethod
    def add(self, a: int, b: int) -> int:
        return a+b

if __name__=='__main__':
    print(add(1, 2)) # => 4
    print(Caclulator().add(1, 2)) # => 4



