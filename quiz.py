import datetime
import random

from questions import Add, Multiply


class Quiz:
    questions = []

    def __init__(self):
        # generate 10 radnom questions with numbers from 1 to 10
        # add these questions into self.questions

    def take_quiz(self):
        # log the start time
        # ask all of the questions
        # log if they got the question right
        # log the end time
        # show a summary

    def ask(self, question):
        # log the start time
        # capture the answer
        # log the end time
        # if the answer is right, send back True
        # otherise, send back False
        # send back the elapsed time, too

    def summary(self):
        # print how many you got right and the total # of questions. 5/10
        # print the total time for the quiz: 30 seconds!