py_secret = '98f00->B@R[1, ..99]$'
py_secret_hashed = 'd291fe57d697831e67ba4954472eed51'
yr_password = ''
tries = 0
while yr_password  != py_secret:
    if(tries % 3 == 0):
        print('...')
    yr_password = input('show me')
    tries +=1
print('ok')
