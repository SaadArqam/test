# n=int(input())
# for _ in range(n):
#     p=input()
#     s=""
#     for i in p:
#         if i=="p":
#             s+="q"
#         elif i=="q":
#             s+="p"
#         else:
#             s+=i
#     print(s[::-1])




t =int(input())  # Number of test cases

results = []
for _ in range(t):
    m, a, b, c = map(int, input().split())
    
    # Fill row 1
    row1_filled = min(a, m) + min(c, max(0, m - a))
    
    # Update remaining "c" after filling row 1
    remaining_c = c - min(c, max(0, m - a))
    
    # Fill row 2
    row2_filled = min(b, m) + min(remaining_c, max(0, m - b))
    
    # Total seated monkeys
    total_seated = row1_filled + row2_filled
    results.append(total_seated)

# Print all results
for res in results:
    print(res)
