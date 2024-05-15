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

    def wordLearned(self, learnedWord):
        learnedWord = learnedWord.encode('utf-8').decode('utf-8')
        print(f"Приехало слово {learnedWord}")
        wordsToLearnPath = os.path.join(currentDir, "../Education/wordsToLearn.csv")
        learnedWordsPath = os.path.join(currentDir, "../Education/learned.csv")

        # Чтение файла со словами для изучения
        with open(wordsToLearnPath, 'r', encoding='utf-8', newline='') as words_file:
            reader = csv.reader(words_file)
            words_list = list(reader)

        # Поиск строки с выученным словом
        found_word = False
        for i, row in enumerate(words_list):
            print(i, row)
            if learnedWord == row[0]:  # Проверяем, есть ли слово в первом столбце строки
                learned_word_row = row
                words_list.pop(i)  # Удаляем строку из списка
                found_word = True
                break
        print(f"{found_word} нашло или нет по итогу")
        # Запись обновленного файла со словами для изучения
        with open(wordsToLearnPath, 'w', encoding='utf-8', newline='') as words_file:
            writer = csv.writer(words_file)
            writer.writerows(words_list)

        # Запись выученного слова в файл с выученными словами (только если слово найдено)
        if found_word:
            with open(learnedWordsPath, 'a', encoding='utf-8', newline='') as learned_file:
                writer = csv.writer(learned_file)
                writer.writerow(learned_word_row)
                print("готово")




