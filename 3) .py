

from cgitb import reset


with open('questions.txt','r') as quesfile,open('answers.txt','r') as ansfile:
    questions=[question.strip() for question in quesfile.readlines()]
    answers=[answer.strip() for answer in ansfile.readlines()]
    print('hello in the quiz')
    print('you should solve 20 questions')
    print('if your answer is right you will earn one mark')
    print('if your answer is wrong you will lose one mark')
    print('good luck')
    name=input('enter your name please:')
    score=0
    for question,answer in zip(questions,answers):
        student_ans=input(question+'?')
        if student_ans.lower()==answer.lower():
            print('correct...good job')
            score+=1
        else:
            print('incorrect...sorry')
            score-=1
    result= score/len(questions)     
    print(f"final score: {result} ")    
    with open('names.txt','w')as l:
        l.writelines(name+':'+str(result))
        