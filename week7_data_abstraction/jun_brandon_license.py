
# Brandon Jun // COMSC 078 // Sequences

CORRECT_ANSWERS = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                   'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

def get_student_answers():

    """
    Asks students 20 questions and returns all answers given

    Args:

    Returns:
        char[] answers: array of answers from the student
    """

    function_student_answers = []
    for i in range(1, 21):
        while True:
            answer = input(f"What is your answer for question {i}: ").strip().upper()
            if answer in['A', 'B', 'C', 'D']:
                break
        function_student_answers.append(answer)

    return function_student_answers

def find_incorrect_answers(function_correct_answers, function_student_answers):

    """
    Finds the score of the student's provided answers

    Args:
        char[] find_score_correct_answers: array of correct answers
        char[] find_score_student_answers: array of answers from the student

    Returns:
        function_incorrect_answers: array of incorrect question numbers
    """

    function_incorrect_answers = []
    for i in range(1, 20):
        if function_student_answers[i] != function_correct_answers[i]:
            function_incorrect_answers.append(i)

    return function_incorrect_answers

def main():

    student_answers = get_student_answers()
    incorrect_answers = find_incorrect_answers(CORRECT_ANSWERS, student_answers)
    score = 20 - len(incorrect_answers)

    print(f"Number of correct answers: {score}")
    print(f"Number of incorrect answers: {20 - score}")
    if score > 15 : print("You passed the test.")
    else : print("You did pass the test.")

    print("Questions answered incorrectly: ", end = "")
    for i in range(0, len(incorrect_answers)):
        print(incorrect_answers[i], end = " ")

main()
