def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("*" * 20)
        func(*args, **kwargs)
        print("*" * 20)
    return wrapper


@decorator_func
def print_ok():
    print("OK")


if __name__ == "__main__":
    print_ok()