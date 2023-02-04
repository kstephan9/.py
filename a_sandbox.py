
astring = 'axxxxxxxxxxxxxxbcabcdefdef'
print(type(astring))

print(astring[1])

d = dict()
for c in astring:
    # if le not in let:
    #     let[le] = 1
    # else:
    #     let[le] = let[le] + 1
    d[c] = d.get(c, 0) + 1


for key in d:
    print(key, d[key])

txt = 'but soft what light in yonder window breaks'

words = txt.split()

r0 = list()
r1 = list()
for word in words:
    r0.append((len(word), word))  # this adds a tuple to list r
    r1.append([len(word), word])  # this adds a tuple to list r

for element in r0:
    print("r0: ", element)

for element in r1:
    print("r1: ", element)

r0.sort(reverse=True)

r0s = list()
for length, word in r0:
    r0s.append(word)

print("r0s: ", r0s)


r1.sort(reverse=True)
r1s = list()
for length, word in r1:
    r1s.append(word)

print("r1s: ", r1s)

#\
# use tuple to sort a dictionary by either key or value
#

d = {'a': 10, 'b': 1, 'c': 22}
print(d)

l_val = list()
l_key = list()

for key, val in d.items():
    l_key.append((key, val))
    l_val.append((val, key))

l_val.sort(reverse=True)

print("l_key: ", l_key)
print("l_val: ", l_val)

# %%
