def generate_combinations(n, k):
    if k == 0:
        return [[]]
    elif k == n:
        return [list(range(1, n + 1))]
    else:
        combinations = []
        for i in range(n, k - 1, -1):
            for c in generate_combinations(i - 1, k - 1):
                combinations.append(c + [i])
        return combinations
generate_combinations(4,2)

students = ['Trang', 'Cong', 'Trung', 'Binh', 'Hoan']

combinations=[]

for i in range(len(students)):
  for j in range( i+1 ,len(students)):
    for k in range(j+1 ,len(students)):
      for l in range(k+1 ,len(students)):
        combinations=[students[i], students[j], students[k], students[l]]
        combinations.append(combinations)


print(combinations)

a=["he","she","we"]

''.join(a)

