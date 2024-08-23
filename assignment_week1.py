quiz = [
    {
        "question": "Who developed Python Programming Language?",
        "options": ["A)Wick van Rossum", "B) Rasmus Lerdorf", "C) Guido van Rossum", "D) Niene Stom"],
        "correct_option": "C"
    },
    {
        "question": "What is the capital of India?",
        "options": ["A) New Delhi", "B) Mumbai", "C) Hyderabad", "D) Chennai"],
        "correct_option": "A"

    },
    {
        "question": "Which state released special postal covers in tribute to ‘Alluri Sitarama Raju'?",
        "options": ["A) Tamil Nadu", "B) Andhra Pradesh", "C) Kerala", "D) Telangana"],
        "correct_option": "B"
    },
    {
        "question": "Which of the given vitamin is a water-soluble vitamin?",
        "options": ["A) Vitamin A", "B) Vitamin B", "C) Vitamin C", "D) Vitamin D"],
        "correct_option": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "correct_option": "D"
    }
]

def user_ip():
    while True:
        answer = input("Please enter your choice: ").upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        else:
            print("Invalid input. Please select A, B, C, or D.")

def display_question(question):
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)



def check_answer(user_ans, correct_ans):
    if user_ans == correct_ans:
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The correct answer was {correct_ans}.")
        return False

def quiz_game(quiz_data):
    score = 0
    for question in quiz_data:
        display_question(question)
        user_ans = user_ip()
        if check_answer(user_ans, question["correct_option"]):
            score += 1
    print(f"\nYour final score is {score}/{len(quiz_data)}.")

if __name__ == "__main__":
    quiz_game(quiz)
