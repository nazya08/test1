import random


def game(list1):
    random_word = random.choice(list1)

    attempts = int(input("Введіть число спроб: "))

    guessed_letters = []

    while attempts > 0:
        print(f"Ваші спроби - {attempts}")

        print(f"Ваше слово: ")
        masked_word = ""
        for i in random_word:
            if i in guessed_letters:
                masked_word += i
            else:
                masked_word += '*'
        print(masked_word)
        print()

        guess = input("Введіть задумане слово або букву: ")

        if guess == random_word:
            print("Вітаю! Ви вгадали:)")
            break
        elif guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("Ви вже ввели цю літеру!")
            elif guess in random_word:
                guessed_letters.append(guess)
                print("Така літера є у слові!")
            else:
                print("Такої літери немає")
                attempts -= 1
        else:
            print("Це не правильне слово")
            attempts -= 1

        print()

    if attempts == 0:
        print("Ви програли! Слово було:", random_word)


game(['nike', 'adidas', 'puma', 'umbro', 'lotto'])
