new_dict + {"google":12, "amazon":9, "flipkart":4, "facebook":13}
max = max(new_dict.values())
max2 = 0
for v in new_dict.values():
if(v>max2 and v<max):
max2 = v
print(max2)
