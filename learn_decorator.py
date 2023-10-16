import time
import random


# Define a decorator
def say_hello_decorator(func):
    # Define a wrapper function that modifies func
    def wrapper(*args, **kwargs):
        print("Hello!")
        func(*args, **kwargs)
        print("Bye!")

    # Return the wrapper function
    return wrapper


# Use @ syntax to decorate greet() with say_hello_decorator()
@say_hello_decorator
def greet(name="Jack"):
    print("Nice to meet you!", name)


# Call the decorated function
greet(name="cool")


def retry(max_tries, delay):
    """
    A decorator that retries a function if it raises an exception.
    :param max_tries: The maximum number of tries
    :param delay: The time interval between tries in seconds
    """

    def inner_decorator(func):
        """
        The implementation of the decorator.
        :param func: The function to retry
        """

        def wrapper(*args, **kwargs):
            tries = 0
            t_e = None
            while tries < max_tries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Exception {e} occurred, retrying in {delay} seconds...")
                    t_e = e
                    time.sleep(delay)
                    tries += 1
            # If the function still fails after max_tries, raise the last exception
            raise t_e

        return wrapper

    return inner_decorator


@retry(max_tries=3, delay=1)
def get_random_number(a, b):
    """
    A function that returns a random integer between a and b.
    It raises an exception if the result is 0.
    """
    result = random.randint(a, b)
    if result == 0:
        raise ValueError("Result cannot be zero")
    if result == 1:
        raise ValueError("Result cannot be zero")
    return result


random.seed(20)
#random.seed(3)
print(get_random_number(-1, 2))
