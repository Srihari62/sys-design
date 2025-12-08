# Exception Rule:
# A subclass should throw fewer or narrower exceptions 
# (but not additional or broader exceptions) than the parent.
# Python does not enforce this either, similar to C++.

"""
Exception Hierarchy in Python (similar conceptually):

BaseException
 ├── Exception                     <-- Mostly used for app-level errors
 │   ├── ArithmeticError
 │   │   ├── OverflowError
 │   │   ├── ZeroDivisionError
 │   │   └── FloatingPointError
 │   ├── ValueError                <-- Comparable to logic_error family
 │   │   ├── IndexError            <-- Similar to out_of_range in C++
 │   └── RuntimeError              <-- Similar to runtime_error in C++
"""

class Parent:
    def getValue(self):
        # Parent throws logic error type equivalent → ValueError
        raise ValueError("Parent error")


class Child(Parent):
    def getValue(self):
        # Child throws narrower exception → IndexError (subtype of ValueError family)
        raise IndexError("Child error")
        # raise RuntimeError("Child Error")  # This would violate the rule


class Client:
    def __init__(self, p: Parent):
        self.p = p

    def takeValue(self):
        try:
            self.p.getValue()
        except ValueError as e:  # Catching logic-error-equivalent
            print("Logic error exception occurred:", e)


if __name__ == "__main__":
    
    parent = Parent()
    child = Child()

    client = Client(parent)
    # client = Client(child)

    client.takeValue()
