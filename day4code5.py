from collections import Counter
def winner(input):
votes = Counter(input)
dict = {}
for values in votes.values():
dict[value] = []
for(key,value) in votes.iteritems():
dict[value].append(key)
maxVote = sorted(dict.keys(),reverse=True)[0]
if len(dict[maxVote])>1:
print sorted(dict[maxVote][0]
  
