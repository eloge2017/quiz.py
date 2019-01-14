#added the feedback that shows when you get it incorrect
#INT variable
#defining a function
    #name the function
def run_qa_loop(qStr, qCheck, ansU, ansCor):
    print(qStr)

    while qCheck == False:
        try:
            ansU = int(input())
            if ansU == ansCor:
                print("good job")
                #score+=1
                qCheck = True
            elif 0 < ansU < 5:
                print("good job")
                qCheck = True
            else:
                print("wrong input, enter (1), (2), (3), or (4).")
        except ValueError:
            print("Please pick one of the number that your answer correspond to.")

#score= int(0)
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

#question 1
run_qa_loop(q1, a1, check1, q1Ans)
#question 2
run_qa_loop(q2, a2, check2, q2Ans)
