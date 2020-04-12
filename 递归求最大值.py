def max(list):
  sub_max=max(list[1:])
  if list == 0:
    return 0
  elif len(list)==2:
    return list[0] if list[0]>list[1] else list[1]
  else:
    return list[0] if list[0]>sub_max else sub_list
    
