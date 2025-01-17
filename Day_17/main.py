from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_bank.append(Question(q['question'], q['correct_answer']))

#print(question_bank[0].text)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've Completed the quiz!")
print(f"Your final score was: {quiz.user_score}/{quiz.question_number}")