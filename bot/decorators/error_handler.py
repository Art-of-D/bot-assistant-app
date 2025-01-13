def input_error(func):
    """
    A decorator that wraps a function to catch and handle specific exceptions.

    This decorator intercepts exceptions such as KeyError, ValueError, IndexError,
    and AssertionError that occur during the execution of the decorated function.
    It returns the string representation of the exception instead of allowing it
    to propagate.

    Args:
        func (callable): The function to be wrapped by the decorator.

    Returns:
        callable: The wrapped function with error handling.
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError, AssertionError) as e:
            return str(e)
    return inner