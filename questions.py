class question:
    def __init__(self, image, task, correct_answer_index):
        self.image = image
        self.task = task
        self.answer = correct_answer_index


question1 = question('https://iceforge.ru/wp-content/uploads/2020/09/fairy-tail-dragon-cry-11.png', 'Какое аниме на картинке?', 1)
question2 = question('https://avatars.mds.yandex.net/get-zen_doc/1704910/pub_5fc69f1ef29188080e6922db_5fc6db1ba093e94902c026f7/scale_1200', 'Из какого аниме этот великолепный мужчина?', 4)
questMas = [question1, question2]


wrongAnswers = ['Яре яре дазе', 'Бака', 'Сраный гайдзин🤡', 'Ксо-о!', 'Подучи эту тему', 'Нееееееет!!!', 'Это знать надо!!!']


answerPack = ['Стальной алхимик',
    'Хвост феи',
    'Тетрадь смерти',
    'Ковбой Бибоп',
    'Невероятные приключения Джо Джо',
    'Унесенные призраками',
    'Эльфийская песнь',
    'Меланхолия Харухи Судзумии',
    'Принцесса Мононоке',
    'Евангелион',
    'Код Гиас: Восставший Лелуш',
    'Блич']