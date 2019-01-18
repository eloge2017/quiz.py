from quizData import *
#added the feedback that shows when you get it incorrect
#INT global grade
global grade
grade = 0

#defining a function
    #name the function
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
            print("Please pick one of the number that your answer correspond to")


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

#score
print("you got a", grade * 10, "%")

if grade == 10:
    print("excellent!!!.")
elif grade == 9:
    print("you got my favorite color wrong didn't you, we not friends.")
elif grade == 8:
    print("you're almost there, keep trying.")
elif grade == 7:
    print("not bad.")
elif grade == 6:
    print("not passing.")
elif grade == 5:
    print("good job idiot.")
elif grade == 4:
    print("")
elif grade == 3:
    print("if this is your 2 time, please stop.")
elif grade == 2:
    print("ummm, i dont know what to tell you.")
elif grade == 1:
    print("drop out.")
elif grade == 0:
    print("your IQ is -32.")
