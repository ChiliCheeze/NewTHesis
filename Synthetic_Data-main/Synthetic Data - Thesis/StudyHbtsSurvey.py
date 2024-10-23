from stdInfo import Student
import random 
import pandas as pd

class S_H_Survey(Student):

    def __init__(self, name, year, Total_respondents, Respondents_ans):
        super().__init__(name, year)
        self.category = [
            "Homework",
            "Time Allocation",
            "Reading and Note Taking",
            "Study Period Procedures",
            "Written Works",
            "Examination"
        ]
        self.question = 3
        self.Total_respondents = Total_respondents
        self.Respondents_ans = Respondents_ans

    def answers(self):
        scale = ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"]

        all_total_respondents = [] #Storage
        for i in range(self.Total_respondents):
            respondents = {}
            #function na kung ilan lang yung value na binigay sa respondents_ans yun lang yung mag gegenerate
            if i <= self.Respondents_ans:
                for section in self.category: #Loop sa kada category
                    for q in range(1, self.question + 1):
                        response = random.choice(scale)
                        
                    respondents[f"{section}_Question_{q}"] = response
            else:
                #If hindi kasama sa mga sasagot 
                for q in range(1, self.question + 1):
                        respondents[f"{section}_Question_{q}"] = None

            all_total_respondents.append(respondents)

        df = pd.DataFrame(all_total_respondents)
        return df
    
    def std_info_and_survey(self):
        # Generate student info
        student_info = self.std_info_dt()

        # Generate survey responses
        survey_answers = self.answers()

        # Ensure both DataFrames have the same number of rows
        if len(student_info) < len(survey_answers):
            survey_answers = survey_answers.iloc[:len(student_info)]
        elif len(student_info) > len(survey_answers):
            survey_answers = pd.concat([survey_answers, pd.DataFrame([None] * (len(student_info) - len(survey_answers)))], ignore_index=True)

        # Combine student info and survey responses
        InfoXSurvey = pd.concat([student_info, survey_answers], axis=1)

        return InfoXSurvey