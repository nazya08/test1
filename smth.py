import random


def game(list1):
    random_word = random.choice(list1)

    attempts = int(input("Введіть число спроб: "))
    guess = input("Введіть задумане слово або букву: ")
    guessed_letters = []

    masked_word = len(random_word) * '*'
    print(masked_word)

    for i in range(attempts):
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

    print("Ви програли! Слово було:", random_word)


game(['nike', 'adidas', 'puma', 'umbro', 'lotto'])
