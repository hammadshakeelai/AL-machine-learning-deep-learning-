from time import time
def measureTime(func):
    def wrapper(a):
        start_time = time()
        result = func(a)
        end_time = time()
        print("execution time", end_time - start_time)
        return result
    return wrapper
passwords = ["a", "abc", "ab", "alsdkfj", "a;sldkjf;laksdjfklj", "alsdkjfkjwer"]
@measureTime
def filterPassword(passwords):
    filtered_passwords = []
    for password in passwords:
        if len(password) >= 8:
            filtered_passwords.append(password)
    return filtered_passwords

result = filterPassword(passwords)
print(result)
