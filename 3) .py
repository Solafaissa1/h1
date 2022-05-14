statement=[]
statement.append(['you are fifth year','T'])
statement.append(['you are fourth year','f'])
print('your name is:')
score=0
for s in statement:
    print('true or false'+s[0])
    guess=input('enter T or F:')
    if guess==s[1]:
        print('correct')
        score=score+1
    else:
        print('incorrect')
print('your final score is:'+str(score))


