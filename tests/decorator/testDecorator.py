from os.path import basename
from functools import wraps

class FOREGROUND:
    GREEN = "\u001b[32;1m"
    RED = "\u001b[31m;1m"
    WHITE = "\u001b[30;1m"

class BACKGROUND:
    BLACK = "\u001b[40m"
    WHITE = "\u001b[47;1m"

class SPECIAL:
    RESET_COLOR = "\u001b[0m"
    BOLD = "\u001b[1m"

def testing_function(file=None):
    def testing_decorator(func):
        @wraps(func)
        def testing_wrapper():
            # TODO (maybe) FIX
            # Function is first called, which could cause confusion in the case of an runtime error within the function, as the 'running' dialouge wouldn't have yet appeared.
            # Should be called between 'running' dialouge and result
            testPassed = func()

            # Test 'running' dialouge + name 
            print(f"{FOREGROUND.WHITE}Running {basename(file)}: ", end="")
            # Test result
            if testPassed:
                print(f"{FOREGROUND.GREEN}{SPECIAL.BOLD}Passed")
            else:
                print(f"{FOREGROUND.RED}{SPECIAL.BOLD}Failed")

            # Resets back to console's default values
            print(SPECIAL.RESET_COLOR, end="")    
        return testing_wrapper
    return testing_decorator
