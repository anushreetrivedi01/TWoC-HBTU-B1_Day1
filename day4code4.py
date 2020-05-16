from collections import Counter
test_dictionary = {'Manjeet' : [1,4,5,6], 'Akash' : [1.8,9], 'Nikhil' : [10,22,4], 'Akshat' : [5,11,22]}
print("the original dictionary : " + str(test_dict))
cnt = Counter()
for idx in test_dict.values():
cnt.update(idx)
res = {idx: [key for key in j if cnt[key] == 1]
for idx, j in test_dict.items()}
print("uncommon elements records : " + str(res))
