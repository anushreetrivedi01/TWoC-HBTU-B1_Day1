def charCount(word):
dict = {}
for i in word:
dict[i] = dict.get(i, 0) + 1
return dict
def possible_words(1words, charSet):
for word in 1words:
flag = 1
chars = charCount(word)
for key in chars:
if key not in charSet:
flag = 0
else:
if charSet.count(key) != chars[key]:
flag = 0
if flag == 1:
print(word)

if _ _name_ _ == "main":
input = ['goo' , 'bat' , 'me' , 'eat' , 'goal' , 'boy' , 'run']
charSet = ['e' , 'o' , 'b' , 'a' , 'm' , 'g' , 'l']
possible_words(input, charSet)
