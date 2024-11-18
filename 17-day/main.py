from question_model import QuestionMode
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for i in range(0,len(question_data)):
    ques=QuestionMode(question_data[i]['text'],question_data[i]['answer'])
    question_bank.append(ques)

quiz=QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number} ")