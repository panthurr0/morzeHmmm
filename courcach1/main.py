import random

morze_alphabet = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

words = ['code', 'bit', 'window', 'soul', 'next']

answers = []  # сюда программа будет вписывать правильность ответов в виде булевых переменных


def get_word():
    """
    получаем случаенное слово
    """

    return random.choice(words)


def morze_encode(right_answer):
    """
    переводим слово в морзе
    """

    morze_word = ''
    for i in right_answer:
        morze_word += morze_alphabet[i] + ' '
    return morze_word


def main():
    """
    общаемся с пользователем
    """

    user_enter = input('''Сегодня мы потренируемся расшифровывать азбуку Морзе
    Нажмите Enter и начнем ''')
    if user_enter == "":
        for i in range(1, 6):
            right_answer = get_word()
            user_input = input(f"\nСлово {i} - {morze_encode(right_answer)} ")
            if user_input.lower() == right_answer:
                print(f'\nВерно, {right_answer}!')
                answers.append(True)
            else:
                print(f'\nНеверно, {right_answer}!')
                answers.append(False)
        print_statistics(answers)
    else:
        print("Кажется, вы не хотите играть. Очень жаль.")


def print_statistics(answers):
    """
    выводим статистику вопросов и верных ответов
    """
    print(f'\nВсего задачек: {len(answers)}')
    print(f'Отвечено верно: {sum(answers)}')
    print(f'Отвечено неверно: {len(answers) - sum(answers)}')


main()
