def generate_binary_strings(n):
    if n == 0:
        return ['']
    else:
        strings = generate_binary_strings(n-1)
        return [s+'0' for s in strings] + [s+'1' for s in strings]

generate_binary_strings(4)

def generate_strings(n):
  if n==0:
    return [""]
  else:
    strings = generate_strings(n-1)
    return [s+'a' for s in strings]+ [s +'b' for s in strings]

def generate_combinations(n,k):
  if k==0:
    return [[]]
  elif k==n:
    return [list(range(1,n+1))]
  else:
    combinations =[]
    for i in range(n ,k-1 , -1):
      for c in generate_combinations(i-1 , k-1):
        combinations.append(c+[i])
    return combinations