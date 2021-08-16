lst = [5, 10, 15, 20, 25, 50, 20]

a = lst.index(20)
lst.pop(a)
lst.insert(a, 200)

print(lst)
