from re import search


class User:
    name = ""
    password = 0
    age = 0

    def __init__(self, name, password, age):
        self.name = name
        self.password = password
        self.age = age

    def __str__(self):
        return self.name

class Video:
    title = ""
    duration = 0
    time_now = 0
    adult_mode = False

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode



class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
           if(nickname == user.name):
            if(hash(password) == user.password):
                self.current_user = user

    def register(self, nickname, password, age):
        for user in self.users:
          if(nickname == user.name):
             print(f"Пользователь {nickname} уже существует")
             return
        NewUser = User(nickname, hash(password), age)
        self.users.append(NewUser)
        return self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *other):
        for i in other:
          if (i.title not in self.videos):
            self.videos.append(i)

    def get_videos(self, searchWord):
        found = []
        for value in self.videos:
            if (searchWord.lower() in value.title.lower()):
                found.append(value.title)
        return found


    def watch_video(self, nameVideo):
        if(self.current_user == None):
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        VideoForWatching = None

        #поиск фильма и его воспроизведение
        for value in self.videos:
            if(value.title == nameVideo):
                VideoForWatching = value

                #возрастное ограничение
                if (VideoForWatching.adult_mode == True and
                self.current_user.age < 18):
                    print("Вам нет 18 лет, пожалуйста, покиньте страницу")
                    return
                for time in range(VideoForWatching.time_now + 1, VideoForWatching.duration + 1):
                    print(time, end=" ", )
                    time += 1
                    if(time == VideoForWatching.duration + 1):
                        print("Конец видео")

       #если фильм не нашелся, ничего не делаем
        if (VideoForWatching == None):
            return



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')