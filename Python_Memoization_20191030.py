import time

cache = {}


def memoization(num):
    if num in cache:
        print(num, ' was cached.')
        return cache[num]
    print('computing ...', num)
    time.sleep(1)
    result = num*num
    cache[num] = result
    return result

print(memoization(4))
print(memoization(10))
print(memoization(4))
print(memoization(10))
