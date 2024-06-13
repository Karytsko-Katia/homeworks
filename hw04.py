import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user_login = input("Введите ваш логин:")
        if user_login == "admin":
            return func(*args, **kwargs)
        else:
            print("Доступ запрещен!")
            return None
    return wrapper


@my_decorator
def get_sum_account():
    sum_account = 1100
    print(sum_account)


get_sum_account()