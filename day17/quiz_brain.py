class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f"Q.{self.question_number + 1}: {current_question.text} ('True'/'False'): ").lower()
        self.question_number += 1

    def still_has_questions(self):
        length = len(self.question_list)
        if self.question_number < length:
            return True      
        else:
            return False

