import csv
import os
import random
import pygame

currentDir = os.path.dirname(__file__)
fileCsv = os.path.join(currentDir, "../Education/wordsToLearn.csv")
words = []
iteration = 0
class Learn:
    def wordChoose(self):
        global iteration
        if iteration == 0:  # для первого входа
            iteration += 1
            with open(fileCsv, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                data = list(reader)

                strings = random.sample(data, 3)  # сразу три рандомных выбираем

                for string in strings:
                    words.append(string)

        if iteration >= 1:
            word, meaning = self.giveWord()
            return word, meaning



            # мб сделать csv с изученными словами и выводить его пока в окно "настройки"
            # есть идея вообще сначала выбрать строку и вырезать её сразу чтоб не попадался повтор и добавить в words
            # и можно записывать не в words а тоже в .csv файл
    def giveWord(self): #
        global iteration
        if iteration > 3:
            iteration = 1
        string = words[iteration-1]
        iteration += 1
        return string

    def exam(self, i):
        print("exam")
        answers = []
        word, meaning = words[i]
        answers.append(meaning)
        with open(fileCsv, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = [row for row in reader]

            allTargets = [row[1] for row in data]

            while len(answers) < 3:
                randomWord = random.choice(allTargets)
                if randomWord not in answers:
                    answers.append(randomWord)

        random.shuffle(answers)
        return answers



