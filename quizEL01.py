#added the feedback that shows when you get it incorrect
#INT variable
#defining a function
    #name the function
grade = 0
def run_qa_loop(qStr, qCheck, ansU, ansCor):
    print(qStr)

    while qCheck == False:
        try:
            ansU = int(input())
            if ansU == ansCor:
                print("good job")
                global grade
                grade+=1
                qCheck = True
            elif 0 < ansU < 5:
                print("good job")
                qCheck = True
            else:
                print("wrong input, enter (1), (2), (3), or (4).")
        except ValueError:
            print("Please pick one of the number that your answer correspond to.")

score= int(0)
q1 = """How many toes do you have on both feet?
(1) 7
(2) 5
(3) 9
(4) 10"""

a1 = int(0)
check1 = bool(False)
q1Ans = 4

q2 = """How many fingers do you have on one hand?
(1) 7
(2) 5
(3) 9
(4) 2"""

a2 = int(0)
check2 = bool(False)
q2Ans = 2

q3 = """How many arms do you have?
(1) 7
(2) 5
(3) 9
(4) 2"""

a3 = int(0)
check3 = bool(False)
q3Ans = 4

q4 = """How many colors are there in the rainbow?
(1) 7
(2) 5
(3) 9
(4) 2"""

a4 = int(0)
check4 = bool(False)
q4Ans = 1

q5 = """How many weekdays are in a week?
(1) 7
(2) 5
(3) 9
(4) 2"""

a5 = int(0)
check5 = bool(False)
q5Ans = 2

q6 = """How many weekends are in a week?
(1) 7
(2) 5
(3) 9
(4) 2"""

a6 = int(0)
check6 = bool(False)
q6Ans = 4

q7 = """How tall is Eloge?
(1) 7
(2) 6.1
(3) 10
(4) 8"""

a7 = int(0)
check7 = bool(False)
q7Ans = 2

q8 = """what is eloge's favorite color?
(1) purple
(2) blue
(3) red
(4) yellow"""

a8 = int(0)
check8 = bool(False)
q8Ans = 1

q9 = """what is the number of questions in this quiz?
(1) 5
(2) 8
(3) 10
(4) 12"""

a9 = int(0)
check9 = bool(False)
q9Ans = 3

q10 = """how many stars in the flag?
(1) 25
(2) 51
(3) 50
(4) 2"""

a10 = int(0)
check10 = bool(False)
q10Ans = 3

#question 1
run_qa_loop(q1, a1, check1, q1Ans)
#question 2
run_qa_loop(q2, a2, check2, q2Ans)
#question 3
run_qa_loop(q3, a3, check3, q3Ans)
#question 4
run_qa_loop(q4, a4, check4, q4Ans)
#question 5
run_qa_loop(q5, a5, check5, q5Ans)
#question 6
run_qa_loop(q6, a6, check6, q6Ans)
#question 7
run_qa_loop(q7, a7, check7, q7Ans)
#question 8
run_qa_loop(q8, a8, check8, q8Ans)
#question 9
run_qa_loop(q9, a9, check9, q9Ans)
#question 10
run_qa_loop(q10, a10, check10, q10Ans)

print("you got",grade *10,"%")

if grade == 10:
    print("excellent!!!")
elif grade == 9:
    print("you got my favorite color wrong didn't you, we not friends")
elif grade == 8:
    print("you're almost there, keep trying")
elif grade == 7:
    print("you're almost there, keep trying")
elif grade == 6:
    print("you're almost there, keep trying")
elif grade == 5:
    print("you're almost there, keep trying")
elif grade == 4:
    print("you're almost there, keep trying")
elif grade == 3:
    print("you're almost there, keep trying")
elif grade == 2:
    print("you're almost there, keep trying")
elif grade == 1:
    print("you're almost there, keep trying")
else:
    print("your IQ is -32")

