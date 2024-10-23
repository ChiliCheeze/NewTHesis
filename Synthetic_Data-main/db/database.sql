use datacoll;

create table StudyHbtsSurvey(
 student_id INT NOT NULL,
    survey_question VARCHAR(255) NOT NULL,
    response TEXT NOT NULL,
    PRIMARY KEY (student_id, survey_question)

);