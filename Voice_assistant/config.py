import os

names = ["джарвис", "помощник", "брат", "дружище", "брателла", "кэп", "док"]
user_name = 'Сэр'
thanks_lst = [
    "Пожалуйста", "Рад был помочь", "Всегда к вашим услугам", "Обращайтесь ещё",
    "Не стоит благодарностей, мне было приятно помочь вам", "Рад заслужить ваше доверие",
    "Обращайтесь в любое время", "Сочтёмся!", "Всегда рад оказать вам поддержку",
    "Пожалуйста, мне это нетрудно", "С вами приятно иметь дело", "Для вас - не жалко!",
    "Подождите благодарить... Это было только начало!", "Это меньшее, что я мог для вас сделать",
    "И вам - всего хорошего", "И вам спасибо. Хорошего дня!", "На здоровье", "Рад что сумел быть полезным",
    "С вами всегда приятно работать. Желаю новых успехов!", "Буду стараться сохранить ваше искреннее доверие",
    "И вам спасибо. Приходите снова!", "Для меня это - пустяки... Не стоит так много внимания.",
    "Мне это в радость", "Спасибо, что уделили мне своё время!",
    "Это мелочи. Не стоит благодарностей. Помогать вам - моя обязанность.", "Вэлкам!",
    "Пусть вам будет во благо!", "Рад работать для вас!", "Без проблем.",
    "Пустяки. Для меня это не составляет труда", "Мне приятна ваша признательность!", "Я рад, что вы оценили",
    "Приятно слышать тёплые слова!", "Пожалуйста! Всего доброго!"
]

vk_token = "тут вк токен"
vk_id = 368424892

weather_token = "тут токен openweathermap"

months = [
    "Января", "Февраля", "Марта", "Апреля",
    "Мая", "Июня", "Июля", "Августа",
    "Сентября", "Октября", "Ноября", "Декабря"
]

jokes_url = "http://anekdotme.ru/random"
project_path = os.path.abspath(os.path.dirname(__file__))

alarm_status = False
alarm_time = ""
