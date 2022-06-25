from collections import Counter
string = 'fahjdfgasdhjfahk'
my_counter = Counter(string)
print(dir(my_counter))
print()
print(my_counter)
print(my_counter.items())
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))
