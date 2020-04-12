def count(list):
  if list==[]:
    return 0;
  else:
    return count(list[1:])+1
