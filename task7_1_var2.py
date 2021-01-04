question_file = '/root/python/lesson7/questions.txt'
answer_file = '/root/python/lesson7/answers.txt'
list = []
list_question = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
list_right_answer = ['1', '2', '1', '3', '2', '3', '2', '1', '3', '2']
question_range = 1
while_range = 5

x_range = 2
y_range = 1

correct_answer = 0
incorrect_answer = 0


def first_question(filename):
    with open(filename, "r") as content:
        row_question = content.readline()
        row_answer1 = content.readline()
        row_answer2 = content.readline()
        row_answer3 = content.readline()
        print(row_question, row_answer1, row_answer2, row_answer3)
        list.append(row_question)



def another_question(filename, while_range):
    with open(filename, "r") as content:
        for i in range(while_range):
            content.readline()
        row_question = content.readline()
        row_answer1 = content.readline()
        row_answer2 = content.readline()
        row_answer3 = content.readline()
        print(row_question, row_answer1, row_answer2, row_answer3)
        list.append(row_question)



def check_if_answer_is_right(question_num, chosen_answer, num_range):
    if str(question_num) == list_question[num_range] and str(chosen_answer) == list_right_answer[num_range]:
        return 'CORRECT'
    else:
        return 'WRONG'


def write_to_answer_file(filename, row_question, chosen_answer, status_chosen_answer):
    with open(filename, "a+") as files:
        files.write('[-------------------------------------]\n')
        files.write('[QUESTION] - {}'.format(row_question))
        files.write('[CHOSEN ANSWER] - [{}]\n'.format(chosen_answer))
        files.write('[STATUS] - [{}]\n'.format(status_chosen_answer))
        files.close()


first_question(question_file)
answer = input('[Choose and type a right number and press enter]')
if check_if_answer_is_right(1, answer, 0) == 'CORRECT':
    write_to_answer_file(answer_file, list[0], answer, 'CORRECT')
    print('CORRECT')
if check_if_answer_is_right(1, answer, 0) == 'WRONG':
    write_to_answer_file(answer_file, list[0], answer, 'WRONG')
    print('WRONG')
while question_range <= len(list_question) - 1:
    another_question(question_file, while_range)
    answer = input('[Choose and type a right number and press enter]')
    if check_if_answer_is_right(x_range, answer, y_range) == 'CORRECT':
        write_to_answer_file(answer_file, list[y_range], answer, 'CORRECT')
        print('CORRECT')
    if check_if_answer_is_right(x_range, answer, y_range) == 'WRONG':
        write_to_answer_file(answer_file, list[y_range], answer, 'WRONG')
        print('WRONG')

    y_range += 1
    question_range += 1
    x_range += 1
    while_range += 5

open_file = open(answer_file, "r")
for line in open_file:
    if '[CORRECT]' in line:
        correct_answer += 1
    if '[WRONG]' in line:
        incorrect_answer += 1

print('[CORRECT_ANSWERS] - [{}]'.format(correct_answer))
print('[INCORRECT_ANSWERS] - [{}]'.format(incorrect_answer))
print('[FILE_ANSWER] - [{}]'.format(answer_file))
#with open(answer_file, "r") as result:
#    for line in
#    print(result.readline())
#    print(result.read())
