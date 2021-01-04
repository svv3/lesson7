#questions1

with open("/root/python/lesson7/questions.txt", "r") as questions:
    str1 = questions.readline()
    print(str1, end="")
    str2 = questions.readline()
    print(str2, end="")
    str3 = questions.readline()
    print(str3, end="")
    str4 = questions.readline()
    print(str4)


with open("/root/python/lesson7/answers.txt", "a+") as answers:
    answers.write(str1)

user_answer = input("Please, input your number and press Enter:")
if user_answer == "1":
    print("CORRECT")
else:
    print("WRONG")

with open("/root/python/lesson7/answers.txt", "a+") as answers:
    if user_answer == "1":
        answers.write("answer 1 is CORRECT")
    else:
        answers.write("answer 1 is WRONG")

#questions2
with open("/root/python/lesson7/questions.txt", "r") as questions:
    for i in range(5):
        questions.readline()
    ques2 = questions.readline()
    print(ques2, end="")
    str1 = questions.readline()
    print(str1, end="")
    str2 = questions.readline()
    print(str2, end="")
    str3 = questions.readline()
    print(str3)


with open("/root/python/lesson7/answers.txt", "a+") as answers:
    answers.write("\n" + "\n" + ques2)

user_answer = input("Please, input your number and press Enter:")
if user_answer == "2":
    print("CORRECT")
else:
    print("WRONG")

with open("/root/python/lesson7/answers.txt", "a+") as answers:
    if user_answer == "2":
        answers.write("answer 2 is CORRECT")
    else:
        answers.write("answer 2 is WRONG")

#questions3
with open("/root/python/lesson7/questions.txt", "r") as questions:
    for i in range(10):
        questions.readline()
    ques3 = questions.readline()
    print(ques3, end="")
    str1 = questions.readline()
    print(str1, end="")
    str2 = questions.readline()
    print(str2, end="")
    str3 = questions.readline()
    print(str3)


with open("/root/python/lesson7/answers.txt", "a+") as answers:
    answers.write("\n" + "\n" + ques3)

user_answer = input("Please, input your number and press Enter:")
if user_answer == "1":
    print("CORRECT")
else:
    print("WRONG")

with open("/root/python/lesson7/answers.txt", "a+") as answers:
    if user_answer == "1":
        answers.write("answer 3 is CORRECT")
    else:
        answers.write("answer 3 is WRONG")

#questions4
with open("/root/python/lesson7/questions.txt", "r") as questions:
    for i in range(15):
        questions.readline()
    ques4 = questions.readline()
    print(ques4, end="")
    str1 = questions.readline()
    print(str1, end="")
    str2 = questions.readline()
    print(str2, end="")
    str3 = questions.readline()
    print(str3)


with open("/root/python/lesson7/answers.txt", "a+") as answers:
    answers.write("\n" + "\n" + ques4)

user_answer = input("Please, input your number and press Enter:")
if user_answer == "3":
    print("CORRECT")
else:
    print("WRONG")

with open("/root/python/lesson7/answers.txt", "a+") as answers:
    if user_answer == "3":
        answers.write("answer 4 is CORRECT")
    else:
        answers.write("answer 4 is WRONG")

#questions5
with open("/root/python/lesson7/questions.txt", "r") as questions:
    for i in range(20):
        questions.readline()
    ques5 = questions.readline()
    print(ques5, end="")
    str1 = questions.readline()
    print(str1, end="")
    str2 = questions.readline()
    print(str2, end="")
    str3 = questions.readline()
    print(str3)


with open("/root/python/lesson7/answers.txt", "a+") as answers:
    answers.write("\n" + "\n" + ques5)

user_answer = input("Please, input your number and press Enter:")
if user_answer == "2":
    print("CORRECT")
else:
    print("WRONG")

with open("/root/python/lesson7/answers.txt", "a+") as answers:
    if user_answer == "2":
        answers.write("answer 5 is CORRECT")
    else:
        answers.write("answer 5 is WRONG")

#questions6
with open("/root/python/lesson7/questions.txt", "r") as questions:
    for i in range(25):
        questions.readline()
    ques6 = questions.readline()
    print(ques6, end="")
    str1 = questions.readline()
    print(str1, end="")
    str2 = questions.readline()
    print(str2, end="")
    str3 = questions.readline()
    print(str3)


with open("/root/python/lesson7/answers.txt", "a+") as answers:
    answers.write("\n" + "\n" + ques6)

user_answer = input("Please, input your number and press Enter:")
if user_answer == "3":
    print("CORRECT")
else:
    print("WRONG")

with open("/root/python/lesson7/answers.txt", "a+") as answers:
    if user_answer == "3":
        answers.write("answer 6 is CORRECT")
    else:
        answers.write("answer 6 is WRONG")

#questions7
with open("/root/python/lesson7/questions.txt", "r") as questions:
    for i in range(30):
        questions.readline()
    ques7 = questions.readline()
    print(ques7, end="")
    str1 = questions.readline()
    print(str1, end="")
    str2 = questions.readline()
    print(str2, end="")
    str3 = questions.readline()
    print(str3)


with open("/root/python/lesson7/answers.txt", "a+") as answers:
    answers.write("\n" + "\n" + ques7)

user_answer = input("Please, input your number and press Enter:")
if user_answer == "2":
    print("CORRECT")
else:
    print("WRONG")

with open("/root/python/lesson7/answers.txt", "a+") as answers:
    if user_answer == "2":
        answers.write("answer 7 is CORRECT")
    else:
        answers.write("answer 7 is WRONG")

#questions8
with open("/root/python/lesson7/questions.txt", "r") as questions:
    for i in range(35):
        questions.readline()
    ques8 = questions.readline()
    print(ques8, end="")
    str1 = questions.readline()
    print(str1, end="")
    str2 = questions.readline()
    print(str2, end="")
    str3 = questions.readline()
    print(str3)


with open("/root/python/lesson7/answers.txt", "a+") as answers:
    answers.write("\n" + "\n" + ques8)

user_answer = input("Please, input your number and press Enter:")
if user_answer == "1":
    print("CORRECT")
else:
    print("WRONG")

with open("/root/python/lesson7/answers.txt", "a+") as answers:
    if user_answer == "1":
        answers.write("answer 8 is CORRECT")
    else:
        answers.write("answer 8 is WRONG")

#questions9
with open("/root/python/lesson7/questions.txt", "r") as questions:
    for i in range(40):
        questions.readline()
    ques9 = questions.readline()
    print(ques9, end="")
    str1 = questions.readline()
    print(str1, end="")
    str2 = questions.readline()
    print(str2, end="")
    str3 = questions.readline()
    print(str3)


with open("/root/python/lesson7/answers.txt", "a+") as answers:
    answers.write("\n" + "\n" + ques9)

user_answer = input("Please, input your number and press Enter:")
if user_answer == "3":
    print("CORRECT")
else:
    print("WRONG")

with open("/root/python/lesson7/answers.txt", "a+") as answers:
    if user_answer == "3":
        answers.write("answer 9 is CORRECT")
    else:
        answers.write("answer 9 is WRONG")

#questions10
with open("/root/python/lesson7/questions.txt", "r") as questions:
    for i in range(45):
        questions.readline()
    ques10 = questions.readline()
    print(ques10, end="")
    str1 = questions.readline()
    print(str1, end="")
    str2 = questions.readline()
    print(str2, end="")
    str3 = questions.readline()
    print(str3)


with open("/root/python/lesson7/answers.txt", "a+") as answers:
    answers.write("\n" + "\n" + ques10)

user_answer = input("Please, input your number and press Enter:")
if user_answer == "2":
    print("CORRECT")
else:
    print("WRONG")

with open("/root/python/lesson7/answers.txt", "a+") as answers:
    if user_answer == "2":
        answers.write("answer 10 is CORRECT")
    else:
        answers.write("answer 10 is WRONG")



