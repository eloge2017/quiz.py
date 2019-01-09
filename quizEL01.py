#added the feedback that shows when you get it incorrect
#INT variable
c1 = False
score = int(0)
a1 = int(0)

print("""How many fingers do you have on one hand?
(1) 7
(2) 5
(3) 9
(4) 4""")
#while loop 
while c1 == False:
#question was asked and availabe options are shown 
    try:
        a1 = int(input())
        if 0 < a1 < 5:    # test for acceptable answers
            if a1 == 2:    # test for correct answer 
               score+=1   # given a plus one
               print("Good job.") # when feedback for when the input is correct
            else:
               print("Good job.")#when feedback for when the input is incorrect
            c1 = True 
        else:
            print("wrong input, enter (1), (2), (3), or (4).")
            #feedback for when the input is not an option
    except ValueError:
        print("Please pick one of the number that your answer correspond to.")
        #feedback for when the input is not a whole number
print("you got ", score * 100, "%.")

