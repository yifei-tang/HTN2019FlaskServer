import difflib

varA = 'SLICED TURKEY'
varB = 'TURKEY SLICED'
varC = 'banana'
varS = ['SLICE','TURK']

#it parse varB by letters
best = difflib.get_close_matches(varA, varB)
print(best) #this does not work

best = difflib.get_close_matches(varA, [varB])
print(best)
seq = difflib.SequenceMatcher(None,best[0],varA)
d = seq.ratio()*100
print(d)
print(best) #this works!

best = difflib.get_close_matches(varA, [varB,varC])
print(best)

best = difflib.get_close_matches(varA, varS)
print(best)
seq = difflib.SequenceMatcher(None,best[0],varA)
d = seq.ratio()*100
print(d)
print(best)
