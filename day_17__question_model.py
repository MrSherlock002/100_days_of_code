##########################################################################
##
##  Prasad R. Bhosale
##  Saturday (23/04/2022)
##  day_17__question_model
##
##########################################################################

question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


class Question:
    def __init__(self,q_text,q_ans):
        self.text = q_text
        self.answer = q_ans
        
        
class quiz_brain:
    
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    def still_has_q(self):
        return self.question_number < len(self.question_list)
            
            
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1 
        user_ans=input(f"Q.{self.question_number} : {current_question.text} (TRUE/FALSE) ?")
        self.check_answer(user_ans,current_question.answer)
    
    def check_answer(self,user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score +=1
            print("You got it right .!")
            
        else:
            print("That's wrong !!")
        print(f"Your current score is : {self.score}/{self.question_number}")
        
    
    
def main():
    question_bank = []
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text,question_answer)
        question_bank.append(new_question)
    # print(question_bank[0].answer)
    
    quiz = quiz_brain(question_bank)
    while quiz.still_has_q():
        quiz.next_question()
    print(" You've completed the quiz")
    print(f"Your final score was : {quiz.score}/{quiz.question_number}")
    
if __name__ =="__main__":
    main()
