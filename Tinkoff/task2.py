s = input()
counter = 0;

if s.count('s') < s.count('h'):
    counter = s.count('s')
else:
    counter = s.count('h')

if s.count('e') < counter:
    counter = s.count('e')

if s.count('r') < counter:
    counter = s.count('r')

if s.count('i') < counter:
    counter = s.count('i')

if (s.count('f') // 2) < counter:
    counter = (s.count('f') // 2)

print(counter)