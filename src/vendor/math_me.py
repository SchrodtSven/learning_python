# SEE: https://www.nachhilfe-team.net/lernen-leicht-gemacht/lineare-gleichungen/
#      https://en.wikipedia.org/wiki/Zero_of_a_function
# 

def square_sum(x, y):
    """(x,y)=x^{2}+y^{2}}"""
    return x**2 + y**2
#    

def factorial_iter(n: int):
    """ Factorial iterative """
    rslt = 1
    for i in range(1, n + 1):
        rslt *= i
    return rslt

def factorial_rec(n: int):
   """ Factorial recursive """
   if n < 1:   # def. <1 --> 1
       return 1
   else:
       return  n * factorial_rec(n - 1)

def moo(a: int, b: int) -> int:
    print(a + b)
    return False

def my_list_avg(numbers: list) ->float:
    return sum(numbers) / len(numbers)
    
def my_avg(*numbers)->float:
    return sum(numbers) /len(numbers)

def my_kw_avg(**numbers)->float:
    return sum(numbers.values()) /len(numbers)


print(square_sum(2.2,3.4))
print(factorial_iter(4))
print(factorial_rec(6))
print(moo(1, 2))

print(my_avg(1,2,4,77))
print(my_list_avg([1,2,4,77]))

print(my_kw_avg(a=1,b=2, c=4, d= 77))


