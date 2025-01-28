i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
  user_inp = ''
  secret = 'stop'
  while user_inp.lower() != secret:
    user_inp = input('your choice!')

