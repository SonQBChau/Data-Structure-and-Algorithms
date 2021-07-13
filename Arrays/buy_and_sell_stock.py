# Time Complexity: O(n^2)
# Space Complexity: O(1)
def buy_and_sell_once(A):
  max_profit = 0
  for i in range(len(A)-1):
    for j in range(i+1, len(A)):
      if A[j] - A[i] > max_profit:
          max_profit = A[j] - A[i]
  return max_profit

# Time Complexity: O(n)
# Space Complexity: O(1)
def buy_and_sell_two(A):
  max_profit = 0
  min_buying_price = A[0]
  selling_price = 0
  for i in range(len(A)):
      selling_price = A[i]
      if selling_price < min_buying_price:
          min_buying_price = selling_price
      profit = selling_price - min_buying_price
      if max_profit < profit:
          max_profit = profit

    
  return max_profit

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_and_sell_once(A))
print(buy_and_sell_two(A))