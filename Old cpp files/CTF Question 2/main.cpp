#include <stdio.h>
#include <string.h>

#define MAX_QUESTIONS 3
#define MAX_QUESTION_LENGTH 100
#define MAX_ANSWER_LENGTH 100

struct QnA {
    char question[MAX_QUESTION_LENGTH];
    char answer[MAX_ANSWER_LENGTH];
};

void initializeQuestions(struct QnA questions[]) {
    strcpy(questions[0].question, "What is the capital of France?");
    strcpy(questions[0].answer, "Paris");

    strcpy(questions[1].question, "Who is the author of Romeo and Juliet?");
    strcpy(questions[1].answer, "William Shakespeare");

    strcpy(questions[2].question, "What is the largest planet in our solar system?");
    strcpy(questions[2].answer, "Jupiter");
}

int main() {
    struct QnA questions[MAX_QUESTIONS];
    initializeQuestions(questions);

    char userAnswer[MAX_ANSWER_LENGTH];
    int correctAnswers = 0;

    printf("Welcome to the Question-Answering AI!\n");

    for (int i = 0; i < MAX_QUESTIONS; ++i) {
        printf("\nQuestion %d: %s\nYour answer: ", i + 1, questions[i].question);
        scanf("%s", userAnswer);

        if (strcmp(userAnswer, questions[i].answer) == 0) {
            printf("Correct!\n");
            correctAnswers++;
        } else {
            printf("Incorrect. The correct answer is: %s\n", questions[i].answer);
        }
    }

    if (correctAnswers == MAX_QUESTIONS) {
        printf("\nCongratulations! You answered all questions correctly. You have unlocked the CTF answer.\n");
        printf("CTF Answer: [Insert CTF answer here]\n");
    } else {
        printf("\nSorry, you did not answer all questions correctly. Try again!\n");
    }

    return 0;
}
