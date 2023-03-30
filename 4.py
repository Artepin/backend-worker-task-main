import json
import sys


def get_questions(data: dict):
    questions = []
    game = list(data)
    lenght = len(game)
    game_dict = data[game[lenght - 1]]
    game_list = game_dict
    game_list = list(game_list)
    rounds = game_dict[game_list[2]]
    for i in rounds:
        if 'questions' in i:
            questions.append(i['questions'])
    return questions

def count_questions(data: dict):
    # вывести количество вопросов (questions)
    count = 0
    questions = get_questions(data)
    for i in questions:
        count+=1
    print(count)


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    questions = get_questions(data)
    answers = []
    for i in questions:
        for j in i:
            if 'correct_answer' in j:
                answers.append(j['correct_answer'])
    print(answers)


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    questions = get_questions(data)
    time_to_answer = 0
    for i in questions:
        for j in i:
            if 'time_to_answer' in j:
                if j['time_to_answer']>time_to_answer:
                    time_to_answer = j['time_to_answer']
    print(time_to_answer)
    print()
    pass


def main(args):
    with open(args,'r') as file:
        data = json.load(file)
    # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    var = sys.argv[1]
    # передать имя файла из аргументов командной строки
    # для передачи имени создаю конфигурацию запуска 4.py, где в аргументах записываю test.json
    main(var)
