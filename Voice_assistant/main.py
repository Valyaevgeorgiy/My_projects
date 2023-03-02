import textblob, pyttsx3, datetime, time, pywhatkit, requests
import bs4, random, vk_api, traceback, pyowm, os
import config
import speech_recognition as sr

# создание объекта, который будет слушать голос пользователя
listener = sr.Recognizer()

# инициализация движка для дальнейшей озвучки текста
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty("voice", voices[2].id)

# удаление шума у аудиодорожки через секундное создание профиля шума со спец свойствами
with sr.Microphone() as source:  # указываем микрофон как источник звука
    listener.adjust_for_ambient_noise(source)


def talk(text):
    engine.say(text)  # занесение текста в голосовой движок
    engine.runAndWait()  # запуск голоса


text = "Привет! Я - твой голосовой помощник Джарвис. Чем могу быть полезен?"
talk(text)
print("[Джарвис]: " + text)


def tell_time():
    time = datetime.datetime.now()
    time = time.strftime("%H:%M").split(":")

    ost = {"first": [2, 3, 4], "second": [1], "not": [11, 12, 13, 14]}

    if (int(time[0]) % 10) in ost["first"] and int(time[0]) not in ost["not"]:
        full_time = time[0] + " часа "
    elif (int(time[0]) % 10) in ost["second"] and int(time[0]) not in ost["not"]:
        full_time = time[0] + " час "
    else:
        full_time = time[0] + " часов "

    if (int(time[1]) % 10) in ost["first"] and (int(time[1]) % 10) not in ost["not"]:
        full_time += time[1] + " минуты"
    elif (int(time[1]) % 10) in ost["second"] and (int(time[1]) % 10) not in ost["not"]:
        full_time += time[1] + " минута"
    else:
        full_time += time[1] + " минут"
    talk(full_time)
    print("[Джарвис]: " + full_time)


def tell_date():

    day = int(datetime.datetime.now().strftime("%d"))
    month = int(datetime.datetime.now().strftime("%m"))
    year = int(datetime.datetime.now().strftime("%Y"))

    date = f"{day} {config.months[month - 1]} {year} года"
    talk(date)
    print("[Джарвис]: " + date)


def play_on_youtube(song):
    song = " ".join(song.split(" ")[1:])
    print(f"[Джарвис]: Включаю {song}.")
    talk(f"Включаю {song}")
    pywhatkit.playonyt(song)


def google_search(text):
    text = " ".join(text.split(' ')[1:])
    print(
        f"[Джарвис]: {text}... хмм, посмотрим, что ответит на этот счёт гугл.")
    talk("Хммм, посмотрим, что ответит на этот счёт гугл.")
    pywhatkit.search(text)


def get_jokes():
    joke = requests.get(config.jokes_url)
    soup = bs4.BeautifulSoup(joke.text, 'html.parser')

    jokes = soup.select(".anekdot_text")
    index = [random.randrange(len(jokes)) for _ in range(3)]

    jokes_text = [jokes[index[i]].get_text().strip() for i in range(3)]
    return jokes_text


def tell_jokes():

    jokes_text = get_jokes()

    j_speech = ["Я тут подготовил для вас троечку анекдотов... ",
                "...поехали... " + "\n\n".join(jokes_text),
                f"... Надеюсь, вам зашло, {config.user_name}!"]

    print(f"[Джарвис]: {j_speech[0]}")
    print(f"[Джарвис]: {j_speech[1]}")
    print(f"[Джарвис]: {j_speech[2]}")
    talk(j_speech[0] + j_speech[1] + j_speech[2])


def vk_init():
    token = config.vk_token
    vk_session = vk_api.VkApi(token=token)
    return vk_session.get_api()

# ВАЖНО (https://vkhost.github.io/) получить для начала работы с API токен VK
# НИКОМУ (и злоумышленникам) НЕЛЬЗЯ ПОКАЗЫВАТЬ ТОКЕН, ИНАЧЕ можно потерять свой аккаунт


def get_vk_messages():
    answers = []
    vk = vk_init()
    conversations = vk.messages.getConversations(offset=0, count=15)
    ost = {"first": [2, 3, 4], "second": [1], "not": [11, 12, 13, 14]}
    is_group = False
    for item in conversations["items"]:
        try:
            unread_count = item["conversation"]["unread_count"]

            unread_text = ""

            if_un_coun = int(str(unread_count)[-1])
            if unread_count > 100:
                if_2_un_coun = int(str(unread_count)[-2])
            else:
                if_2_un_coun = unread_count

            if if_un_coun in ost["second"] and if_2_un_coun not in ost["not"]:
                unread_text += "непрочитанное сообщение"
            elif if_un_coun in ost["first"] and if_2_un_coun not in ost["not"]:
                unread_text += "непрочитанных сообщения"
            else:
                unread_text += "непрочитанных сообщений"

            if item["conversation"]["can_send_money"] != True:
                is_group = True
            else:
                is_group = False

            if is_group:
                dialog_id = item["conversation"]["peer"]["id"]

                history = vk.messages.getHistory(
                    peer_id=dialog_id,
                    count=unread_count,
                    extended=True
                )

                name_chat = history["conversations"][0]["chat_settings"]["title"]

                msgs = history["items"]
                msgs.reverse()

                ms_txt = []

                for message in msgs:
                    name_user_ms = ""
                    id_user_message = message["from_id"]
                    try:
                        for users in history["profiles"]:
                            if users["id"] == id_user_message:
                                name_user_ms = f"{users['first_name']} {users['last_name']}"
                                ms_txt.append(
                                    f"[{name_user_ms}]: " + message["text"])
                    except Exception as e:
                        try:
                            for groups in history["groups"]:
                                if groups["id"] == ((id_user_message) * (-1)):
                                    name_user_ms = f"{groups['name']}"
                                    ms_txt.append(
                                        f"[{name_user_ms}]: " + message["text"])
                        except Exception as e:
                            print("Ошибка: " + traceback.format_exc())
                            ms_txt.append(
                                f"[{name_user_ms}]: " + message["text"])
                    finally:
                        try:
                            for us_gr in history["groups"]:
                                if us_gr["id"] == ((id_user_message) * (-1)):
                                    name_user_ms = f"{us_gr['name']}"
                                    ms_txt.append(
                                        f"[{name_user_ms}]: " + message["text"])
                        except Exception as e:
                            pass

                full_ms = '\n'.join(ms_txt)
                print()
                print("[Джарвис]: ", end="")
                print(
                    f"{unread_count} {unread_text} в чате {name_chat}: \n{full_ms}")
                if len(ms_txt) >= 5:
                    answers.append(
                        f"Вот последние 5 сообщений из чата {name_chat}: \n{ms_txt[-5::1]}\n ......"
                    )
                else:
                    answers.append(
                        f"{unread_count} {unread_text} в чате {name_chat}: \n{ms_txt}"
                    )
                print()
            else:
                dialog_id = item["conversation"]["peer"]["local_id"]

                history = vk.messages.getHistory(
                    peer_id=dialog_id,
                    count=unread_count,
                    extended=True
                )

                profile = history["profiles"][0]
                user = f"{profile['first_name']} {profile['last_name']}"

                messages = history["items"]
                messages.reverse()

                ms_text = ""
                for message in messages:
                    ms_text += message["text"] + "\n"

                answers.append(
                    f"{unread_count} {unread_text} от пользователя {user}: \n{ms_text}")
        except Exception as e:
            pass

    return answers


def check_my_vk_messages():
    messages = get_vk_messages()
    j_speech = ""
    if len(messages) > 0:
        for msg in messages:
            print(f"[Джарвис]: {msg}")
            talk(msg)
            print()
    else:
        j_speech = f"{config.user_name}, у вас нет новых сообщений."
        print(f"[Джарвис]: {j_speech}")
        talk(j_speech)


def write_vk_message(user, text):
    vk = vk_init()
    try:
        friends = vk.friends.search(user_id=config.vk_id, q=user)
        friend_id = friends["items"][0]["id"]
        vk.messages.send(user_id=friend_id, message=text, random_id=0)
        print(
            f"[Джарвис]: {config.user_name}, ваше сообщение успешно отправлено.")
        talk(f"{config.user_name}, ваше сообщение успешно отправлено.")
    except Exception as e:
        talk(f"{config.user_name}, такого пользователя я не нашёл... грустный смайлик!")


def tell_weather(city_rus):

    # Токен из OpenWeatherMap API
    # Им можно пользоваться 60 раз за минуту => 1 000 000 раз в день

    token = config.weather_token

    owm = pyowm.OWM(token)
    manager = owm.weather_manager()

    blob = textblob.TextBlob(city_rus)
    final_en_str = str(blob.translate(to="en"))

    observation = manager.weather_at_place(final_en_str)

    weather = observation.weather

    ost = {"first": [2, 3, 4], "second": [1], "not": [11, 12, 13, 14]}
    temp_city = round(weather.temperature('celsius')['temp'])
    temp = abs(temp_city) % 10

    if temp in ost["first"] and temp not in ost["not"]:
        cels = "градуса"
    elif temp in ost["second"] and temp not in ost["not"]:
        cels = "градус"
    else:
        cels = "градусов"

    speed_city = round(weather.wind()['speed'], 1)
    final_str = f"{config.user_name}, на улице города {city_rus} сейчас {temp_city} {cels}, ветер {speed_city} метра в секунду."
    print("[Джарвис]: " + final_str)
    talk(final_str)


def turn_radio():
    print(f"[Джарвис]: Включаю радио, {config.user_name}!")
    talk(f"Включаю радио, {config.user_name}!")

    path = config.project_path
    os.chdir(path)

    os.system('radio.m3u')


def alarm():
    time = datetime.datetime.now()
    now_hour = time.hour
    now_minute = time.minute

    alarm_hour = int(config.alarm_time[:2])
    alarm_minute = int(config.alarm_time[2:])

    if now_hour == alarm_hour and now_minute == alarm_minute:
        config.alarm_status = False
        talk(f"{config.user_name} Георгий, время подниматься и покорять мир!")

        path = config.project_path
        os.chdir(path)

        os.system('moscow_calling.mp3')


def take_command(count):
    try:
        with sr.Microphone() as source:
            print(f"...... Запускается {count} процесс прослушки ......")
            print(f"[Джарвис]: ...... Слушаю вас, {config.user_name} ......")

            # запуск процесса прослушки
            voice = listener.listen(source, timeout=2, phrase_time_limit=4)
            # timeout - разрыв между настоящим и следующим циклами запуска микрофона
            # phrase_time_limit - ограничение длины записи самой фразы

            # перевод голосовой команды в текстовую
            # работа движка по умолчанию с английским языком

            command = listener.recognize_google(voice, language="ru-RU")
            # for name in config.names:
            if command.lower() in config.names:
                print(f"[Вы]: {command}")
                print(
                    f"[Джарвис]: Приветствую, {config.user_name}. С чего начнём?")
                talk(f"Приветствую, {config.user_name}. С чего начнём?")
                return take_voice()
    except:
        pass

    return ''


def take_voice():
    command = ""
    try:
        with sr.Microphone() as source:
            print("...... Запускается процесс внимательной прослушки ......")
            print(f"[Джарвис]: ...... Слушаю вас, {config.user_name} ......")

            voice = listener.listen(source, timeout=2, phrase_time_limit=4)
            command = listener.recognize_google(voice, language="ru-RU")
            return command
    except:
        pass
    return ""


def run(count, begin_work):
    try:
        command = take_command(count)
        if "привет" in command.lower():
            begin_work = time.time()
            print(f"[Джарвис]: Приветствую вас, {config.user_name} Георгий")
            talk(f"Приветствую вас, {config.user_name} Георгий!")
            return begin_work
        elif "спасибо" in command.lower():
            begin_work = time.time()
            thx = random.choice(config.thanks_lst)
            print(f"[Джарвис]: {thx}")
            talk(thx)
            return begin_work
        elif "время" in command.lower():
            begin_work = time.time()
            tell_time()
            return begin_work
        elif "число" in command.lower() or "дата" in command.lower() or "дате" in command.lower() or "дату" in command.lower():
            begin_work = time.time()
            tell_date()
            return begin_work
        elif "включи" in command.lower():
            begin_work = time.time()
            play_on_youtube(command)
            return begin_work
        elif "джарвис" in command.lower():
            begin_work = time.time()
            search = command.replace("джарвис ", "")
            google_search(search)
            return begin_work
        elif "анекдот" in command.lower():
            begin_work = time.time()
            tell_jokes()
            return begin_work
        elif "вк" in command.lower() or "vk" in command.lower():
            begin_work = time.time()
            check_my_vk_messages()
            return begin_work
        elif "напиши" in command.lower():
            begin_work = time.time()
            print("[Джарвис]: Кому желаете отправить сообщение?")
            talk("Кому желаете отправить сообщение?")
            user = take_voice()
            print("[Джарвис]: Что хотите написать?")
            talk("Что хотите написать?")
            text = take_voice()
            write_vk_message(user, text)
            return begin_work
        elif "погода" in command.lower() or "погоде" in command.lower():
            begin_work = time.time()
            print("[Джарвис]: В какую точку отправимся?")
            talk("В какую точку отправимся?")
            city_rus = take_voice()
            tell_weather(city_rus)
            return begin_work
        elif "запусти радио" in command.lower():
            begin_work = time.time()
            turn_radio()
            return begin_work
        elif "будильник" in command.lower():
            begin_work = time.time()
            print("[Джарвис]: На какое время поставить будильник?")
            talk("На какое время поставить будильник?")

            config.alarm_time = take_voice().replace(":", "")
            config.alarm_status = True
            return begin_work

        if config.alarm_status:
            alarm()

    except Exception as e:
        print(f"[Джарвис]: {config.user_name}, вас очень плохо слышно!")
        talk(f"{config.user_name}, вас очень плохо слышно!")
        return ""
    return ""


if __name__ == "__main__":
    counter = 0
    begin_work = time.time()
    time_end = 120
    final_phrase = config.user_name + \
        " Георгий, прошло уже 2 минуты, а тут тишина. Я с вами прощаюсь. До скорого!"
    while True:
        if time.time() - begin_work < time_end:
            print(
                f"[Джарвис]: Прошло {round(time.time() - begin_work, 2)} секунды молчания...")
            counter += 1
            work_now = run(counter, begin_work)
            if work_now != "":
                begin_work = work_now
        else:
            print(
                f"[Джарвис]: Прошло {round(time.time() - begin_work, 2)} секунды молчания...")
            print(f"[Джарвис]: {final_phrase}")
            talk(final_phrase)
            break
