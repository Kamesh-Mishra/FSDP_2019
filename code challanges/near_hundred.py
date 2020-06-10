"""
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""
"""
Solution:

def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
  """
  
def near_hundred(n):
  diff = 100 - n
  diff1 = 200 - n
  if abs(diff) <= 10 or abs(diff1) <= 10:
    
    return True
  else:
    return False