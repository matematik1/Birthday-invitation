from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import datetime
import time
import webbrowser
import tkinter as tk
import random
import pygame
import threading
from itertools import count, cycle
import os


def on_closing():
    """Функція, яка викликається при закритті вікна та імітує "виліт"."""
    print("Програма зараз імітуватиме виліт...")
    choice = random.randint(0, 2)
    if choice == 0:
        os._exit(1)
    elif choice == 1:
        os._exit(1)  # Негайно завершуємо процес без очищення (як при помилці)
    else:
        os._exit(1)



class RandomImage:
    def __init__(self, app):
        self.app = app
        self.images = [ImageTk.PhotoImage(Image.open(f"png/({i}).png")) for i in range(1, 21)]
        self.image_label = tk.Label(app)
        self.image_label.place(x=175.75, y=216.21) # Розміщення через place
        self.change_image()

    def change_image(self):
        random_image = random.choice(self.images)
        self.image_label.config(image=random_image)
        self.app.after(1333, self.change_image)


class ImageLabel(Label):
    def load(self, im):
        im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        self.frames = cycle(frames)
        self.deley = im.info['duration']

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.deley, self.next_frame)



class MusicPlayer:
    def __init__(self, master):
        self.master = master
        pygame.mixer.init()
        self.songs = [
            "music/(1).mp3",
            "music/(2).mp3",
            "music/(3).mp3",
            "music/(4).mp3",
            "music/(5).mp3",
            "music/(6).mp3",
            "music/(7).mp3",
            "music/(8).mp3"
        ]
        self.is_playing = False
        self.current_song = None
        self.volume = 0.8  # Початкова гучність
        self.played_songs = []  # Список відтворених пісень
        self.available_songs = self.songs[:]  # Копія для відстеження доступних

        self.status_text = tk.StringVar()
        self.status_text.set("")  # Прибрано початковий текст
        self.status_label = tk.Label(master, textvariable=self.status_text)

    def play_sound_async(self, song_path):
        """Асинхронно відтворює аудіофайл."""
        try:
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.play()
            # self.status_text.set(f"Відтворення: {self.current_song}, Гучність: {self.volume:.1f}") # Прибрано виведення тексту
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            self.play_next_song()
        except pygame.error as e:
            self.status_text.set(f"")
            self.is_playing = False
            self.current_song = None

    def play_random_song(self):
        """Вибирає випадкову пісню та відтворює її."""
        if not self.is_playing and self.available_songs:
            self.current_song = random.choice(self.available_songs)
            self.available_songs.remove(self.current_song)  # Видалити з доступних
            self.played_songs.append(self.current_song)  # Додати до відтворених
            # self.status_text.set(f"Запуск відтворення...") # Прибрано виведення тексту
            self.is_playing = True
            threading.Thread(target=self.play_sound_async, args=(self.current_song,)).start()

            if not self.available_songs:  # Якщо всі пісні відтворено
                self.available_songs = self.songs[:]  # Відновити список
                self.played_songs = []  # Очистити відтворені
                self.status_text.set("")  # Повідомлення (можна прибрати)

        elif not threading.main_thread().is_alive():
            self.is_playing = False
            self.current_song = None
        elif not self.songs:
            self.status_text.set("Список пісень порожній.")

    def play_next_song(self):
        """Викликається після закінчення поточної пісні для відтворення наступної."""
        self.is_playing = False
        self.current_song = None
        self.play_random_song()

    def decrease_volume(self):
        """Зменшує гучність на 0.1."""
        if self.is_playing:
            self.volume = max(0.0, self.volume - 0.1)
            pygame.mixer.music.set_volume(self.volume)
            # self.status_text.set(f"Відтворення: {self.current_song}, Гучність: {self.volume:.1f}") # Прибрано виведення тексту
        else:
            self.status_text.set("")

    def increase_volume(self):
        """Збільшує гучність на 0.1."""
        if self.is_playing:
            self.volume = min(1.0, self.volume + 0.1)
            pygame.mixer.music.set_volume(self.volume)
            # self.status_text.set(f"Відтворення: {self.current_song}, Гучність: {self.volume:.1f}") # Прибрано виведення тексту
        else:
            self.status_text.set("")

    def skip_song(self):
        """Перериває поточну пісню та запускає наступну."""
        if self.is_playing:
            pygame.mixer.music.stop()
            self.is_playing = False
            self.current_song = None
            # self.status_text.set("Пісню пропущено.") # Прибрано виведення тексту
            self.play_random_song()
        else:
            self.status_text.set("")

def update_countdown():
    """Обновляет виджет обратного отсчета."""
    target_date = datetime.datetime(2025, 5, 6, 0, 0, 0)  # 6 мая 2025, 00:00:00
    now = datetime.datetime.now()
    time_difference = target_date - now

    if time_difference.total_seconds() <= 0:
        countdown_label.config(text="Время истекло!")
    else:
        days = time_difference.days
        seconds = time_difference.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        remaining_seconds = seconds % 60

        countdown_text = f"День народження через: {days} днів, {hours} годин, {minutes} минут, {remaining_seconds} секунд"
        countdown_label.config(text=countdown_text)

    # Обновляем виджет каждую секунду
    main_frame.after(1000, update_countdown)


def close_tab(event):
    if notebook.select() != notebook.tabs()[0]: # Проверяем, что выбрана не первая вкладка
        notebook.forget(notebook.select())

def open_tg():
    """Открывает ссылку на Google в браузере по умолчанию."""
    webbrowser.open_new("https://t.me/yurch1ks")

def open_git():
    """Открывает ссылку на Google в браузере по умолчанию."""
    webbrowser.open_new("https://github.com/matematik1")

def open_instagram():
    """Открывает ссылку на Google в браузере по умолчанию."""
    webbrowser.open_new("https://www.instagram.com/matemch1k?igsh=dDN5NjM5MmFybHU=")

def open_mail():
    """Открывает ссылку на Google в браузере по умолчанию."""
    webbrowser.open_new("mailto:shmitayura@gmail.com")


def open_invitation_lara(name):
    new_tab_lara = ttk.Frame(notebook)
    new_tab_lara.pack(fill="both", expand=True)
    notebook.add(new_tab_lara, text=f"Запрошення для {name}")
    notebook.select(new_tab_lara) # Переключитись на нову вкладку

    image = Image.open("png/lara_begraynd.png")
    background_image2 = ImageTk.PhotoImage(image)
    background_label2 = tk.Label(new_tab_lara, image = background_image2)
    background_label2.place(x=-2, y=-2)
    background_label2.image = background_image2  # Збережіть посилання!

    style_global = ttk.Style()
    style_global.configure("style_global.TLabel", font=("Arial", 21, "bold"), borderwidth=0, relief="flat")

    style_2 = ttk.Style()
    style_2.configure("style_2.TLabel", font=("Arial", 18, "bold"), borderwidth=0, relief="flat")

    lable_global_text = ttk.Label(new_tab_lara, text=f"Дякую що відкрими моє запрошення Ларисо!", style="style_global.TLabel")
    lable_global_text.place(x=123, y=100)

    lable_invait = ttk.Label(new_tab_lara, text="Запрошую вас на свій день народження,", style="style_2.TLabel")
    lable_invait.place(x=137, y= 515)
    lable_invait = ttk.Label(new_tab_lara, text="Яке буде 6 травня о 17:00 по в.Соборна", style="style_2.TLabel")
    lable_invait.place(x=137, y= 565)
    lable_invait = ttk.Label(new_tab_lara, text="Якщо ви прийдете то звяжіться з нами", style="style_2.TLabel")
    lable_invait.place(x=137, y= 615)
    lable_invait = ttk.Label(new_tab_lara, text="По контактах на головній сторінці", style="style_2.TLabel")
    lable_invait.place(x=137, y= 665)
    lable_invait = ttk.Label(new_tab_lara, text="!!!Дякую за увагу!!!", style="style_2.TLabel")
    lable_invait.place(x=137, y= 715)

    lable_close = ttk.Label(new_tab_lara, text="Для того щоб закрити відкриту вкладку натисніть на неї правою кнопкою миші!")
    lable_close.place(x=134, y=765)

    image_list1 = ["png/lara (1).png", "png/lara (2).png", "png/lara (3).png", "png/lara (4).png", "png/lara (5).png"]
    images = [ImageTk.PhotoImage(Image.open(path)) for path in image_list1]
    current_image = images[0]  # Start with the first image

    image_label = tk.Label(new_tab_lara, image=current_image)
    image_label.image = current_image
    image_label.place(x=346.86, y=153.79)

    def on_enter(event):
        nonlocal current_image
        current_image = random.choice(images)
        image_label.config(image=current_image)
        image_label.image = current_image  # Update the reference

    image_label.bind("<Enter>", on_enter)


def open_invitation_others(name):
    new_tab_others = ttk.Frame(notebook)
    new_tab_others.pack(fill="both", expand=True)
    notebook.add(new_tab_others, text=f"Запрошення для {name}")
    notebook.select(new_tab_others) # Переключитись на нову вкладку

    image = Image.open("png/others_begraynd.png")
    background_image2 = ImageTk.PhotoImage(image)
    background_label2 = tk.Label(new_tab_others, image = background_image2)
    background_label2.place(x=-2, y=-2)
    background_label2.image = background_image2  # Збережіть посилання!

    style_global = ttk.Style()
    style_global.configure("style_global.TLabel", font=("Arial", 20, "bold"), borderwidth=0, relief="flat")

    style_2 = ttk.Style()
    style_2.configure("style_2.TLabel", font=("Arial", 16, "bold"), borderwidth=0, relief="flat")

    lable_global_text = ttk.Label(new_tab_others, text=f"Дякую що відкрими моє запрошення!", style="style_global.TLabel")
    lable_global_text.place(x=157, y=168)

    lable_invait = ttk.Label(new_tab_others, text="Запрошую вас на свій день народження,", style="style_2.TLabel")
    lable_invait.place(x=147, y= 475)
    lable_invait = ttk.Label(new_tab_others, text="Яке буде 6 травня о 17:00 по в.Соборна", style="style_2.TLabel")
    lable_invait.place(x=147, y= 525)
    lable_invait = ttk.Label(new_tab_others, text="Якщо ви прийдете то звяжіться з нами", style="style_2.TLabel")
    lable_invait.place(x=147, y= 575)
    lable_invait = ttk.Label(new_tab_others, text="По контактах на головній сторінці", style="style_2.TLabel")
    lable_invait.place(x=147, y= 625)
    lable_invait = ttk.Label(new_tab_others, text="!!!Дякую за увагу!!!", style="style_2.TLabel")
    lable_invait.place(x=217, y= 675)

    lable_close = ttk.Label(new_tab_others, text="Для того щоб закрити відкриту вкладку натисніть на неї правою кнопкою миші!")
    lable_close.place(x=307, y=715)

    # Створення та запуск RandomImage для цієї вкладки
    random_image_instance = RandomImage(new_tab_others)

def open_invitation_alla(name):
    new_tab_alla = ttk.Frame(notebook)
    new_tab_alla.pack(fill="both", expand=True)
    notebook.add(new_tab_alla, text=f"Запрошення для {name}")
    notebook.select(new_tab_alla) # Переключитись на нову вкладку


    image = Image.open("png/alla_begraynd.png")
    background_image2 = ImageTk.PhotoImage(image)
    background_label2 = tk.Label(new_tab_alla, image = background_image2)
    background_label2.place(x=-2, y=-2)
    background_label2.image = background_image2  # Збережіть посилання!

    style_global = ttk.Style()
    style_global.configure("style_global.TLabel", font=("Arial", 18, "bold"), borderwidth=0, relief="flat")

    style_2 = ttk.Style()
    style_2.configure("style_2.TLabel", font=("Arial", 18, "bold"), borderwidth=0, relief="flat")

    lable_global_text = ttk.Label(new_tab_alla, text=f"Дякую що відкрими моє запрошення Алла!", style="style_global.TLabel")
    lable_global_text.place(x=177, y=76)

    lable_invait = ttk.Label(new_tab_alla, text="Запрошую вас на свій день народження,", style="style_2.TLabel")
    lable_invait.place(x=187, y= 515)
    lable_invait = ttk.Label(new_tab_alla, text="Яке буде 6 травня о 17:00 по в.Соборна", style="style_2.TLabel")
    lable_invait.place(x=187, y= 565)
    lable_invait = ttk.Label(new_tab_alla, text="Якщо ви прийдете то звяжіться з нами", style="style_2.TLabel")
    lable_invait.place(x=187, y= 615)
    lable_invait = ttk.Label(new_tab_alla, text="По контактах на головній сторінці", style="style_2.TLabel")
    lable_invait.place(x=187, y= 665)
    lable_invait = ttk.Label(new_tab_alla, text="!!!Дякую за увагу!!!", style="style_2.TLabel")
    lable_invait.place(x=187, y= 715)

    lable_close = ttk.Label(new_tab_alla, text="Для того щоб закрити відкриту вкладку натисніть на неї правою кнопкою миші!")
    lable_close.place(x=187, y=765)

    image_list1 = ["png/alla (1).png", "png/alla (2).png", "png/alla (3).png", "png/alla (4).png"]
    images = [ImageTk.PhotoImage(Image.open(path)) for path in image_list1]
    current_image = images[0]  # Start with the first image

    image_label = tk.Label(new_tab_alla, image=current_image)
    image_label.image = current_image
    image_label.place(x=193.56, y=134.38)

    def on_enter(event):
        nonlocal current_image
        current_image = random.choice(images)
        image_label.config(image=current_image)
        image_label.image = current_image  # Update the reference

    image_label.bind("<Enter>", on_enter)


def lara():
    progress_bar = ttk.Progressbar(main_frame, orient="horizontal", length=250, maximum=150, mode="determinate")
    progress_bar.place(x=328.79, y=427.41)
    for i in range(151):
        time.sleep(0.03)  # Імітація завантаження
        progress_bar["value"] = i
        app.update_idletasks()
    progress_bar.destroy()
    open_invitation_lara("Лари")

def others():
    progress_bar = ttk.Progressbar(main_frame, orient="horizontal", length=300, maximum=200 , mode="determinate")  # Збільшено length в 4 рази
    progress_bar.place(x=288.79, y=427.41)
    for i in range(201):
        time.sleep(0.035)  # Залишаємо той самий час
        progress_bar["value"] = i
        app.update_idletasks()
    progress_bar.destroy()
    open_invitation_others("Інших")

#Вкладка для 3 вітання

def alla():
    progress_bar = ttk.Progressbar(main_frame, orient="horizontal", length=200, maximum=125, mode="determinate")
    progress_bar.place(x=348.79, y=427.41)
    for i in range(126):
        time.sleep(0.025)  # Імітація завантаження
        progress_bar["value"] = i
        app.update_idletasks()
    progress_bar.destroy()
    open_invitation_alla("Алли")

#Вкладка для 3 вітання

# вікно

app = Tk()
app.geometry("880x880") # розмір вікна
app.resizable(False, False) # відключення зміни розміру
app.title("Birthday Invitation") # назва вікна
app.iconbitmap(default="png/app.ico") # іконка вікна
app.attributes("-alpha", 0.89) # прозорість вікна
app.config(cursor="center_ptr") # заміна курсора

# вікно

#основна вкладка

notebook = ttk.Notebook(app)
notebook.pack(expand=True, fill="both")

main_frame = ttk.Frame(notebook)
main_frame.pack(fill="both", expand=True)
notebook.add(main_frame, text="Вибір запрошення")

canvas = Canvas(main_frame, bg="white", width=880, height=880)
canvas.pack(anchor=CENTER, expand=1)

image = Image.open("png/envelope.png")
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(main_frame, image=background_image)
background_label.place(x=-2, y=-2)
background_label.image = background_image  # Збережіть посилання!

label_text = tk.Label(main_frame, text="")
label_text.pack(anchor=NW, padx=500, pady=500)

# вибір привітання

def selected(event):
    # отримуємо виділений елемент
    selection = combobox.get()
    print(selection)
    label["text"] = f"Ви вибрали запрошення для: {selection} (нажміть на кнопку щоб відкрити його)"

    style2 = ttk.Style()
    style2.configure("BoldLarge1.TButton", font=("Arial", 12, "bold"), borderwidth=2, relief="flat", background="#A9203E")
    style2.configure("BoldLarge2.TButton", font=("Arial", 12, "bold"), borderwidth=2, relief="flat",background="#54FF9F")
    style2.configure("BoldLarge3.TButton", font=("Arial", 12, "bold"), borderwidth=2, relief="flat",background="#9932CC")

    selection2 = combobox.get()
    if selection2 == "Лари":
        bat = ttk.Button(main_frame, text="Відкрити запрошення", style="BoldLarge1.TButton", command=lara)
        bat.place(x=23, y=94)
    elif selection2 == "Інших":
        bat2 = ttk.Button(main_frame, text="Відкрити запрошення", style="BoldLarge2.TButton", command=others)
        bat2.place(x=23, y=94)
    elif selection2 == "Алли":
        bat3 = ttk.Button(main_frame, text="Відкрити запрошення", style="BoldLarge3.TButton", command=alla)
        bat3.place(x=23, y=94)
    else:
        print("обновленно")


languages = ["Лари", "Алли", "Інших"]
# Створюємо стиль для label
style = ttk.Style()
style.configure("BoldLarge.TLabel", font=("Arial", 16, "bold"), borderwidth=0, relief="flat")

# Застосовуємо стиль до label
label = ttk.Label(main_frame, style="BoldLarge.TLabel")
label.place(x=23, y=749)

combobox = ttk.Combobox(main_frame, values=languages, state="readonly")
combobox.place(x=543, y=56)
combobox.bind("<<ComboboxSelected>>", selected)

combox_txt = tk.Label(main_frame,text="Виберить для кого хочите відкрити запрошення")
combox_txt.configure(font=("Arial", 16, "bold"), borderwidth=0, relief="flat")
combox_txt.place(x=23, y=53)
#Основна вкладка

tg = Image.open("png/tg.png").resize((50, 50))  # Измените размер по желанию
photo_tg = ImageTk.PhotoImage(tg)

# Создайте кнопку с изображением
button_tg = tk.Button(main_frame, image=photo_tg, command=open_tg,  borderwidth=0, highlightthickness=0, padx=0, pady=0)
button_tg.image = photo_tg  # Сохраняем ссылку на изображение
button_tg.place(x=603, y=792)

git = Image.open("png/git.png").resize((50, 50))  # Измените размер по желанию
photo_git = ImageTk.PhotoImage(git)

# Создайте кнопку с изображением
button_git = tk.Button(main_frame, image=photo_git, command=open_git,  borderwidth=0, highlightthickness=0, padx=0, pady=0)
button_git.image = photo_git  # Сохраняем ссылку на изображение
button_git.place(x=673, y=792)

ins = Image.open("png/ins.png").resize((50, 50))  # Измените размер по желанию
photo_ins = ImageTk.PhotoImage(ins)

# Создайте кнопку с изображением
button_ins = tk.Button(main_frame, image=photo_ins, command=open_instagram,  borderwidth=0, highlightthickness=0, padx=0, pady=0)
button_ins.image = photo_ins  # Сохраняем ссылку на изображение
button_ins.place(x=743, y=792)

mail = Image.open("png/mail.png").resize((50, 50))  # Измените размер по желанию
photo_mail = ImageTk.PhotoImage(mail)

# Создайте кнопку с изображением
button_mail = tk.Button(main_frame, image=photo_mail, command=open_mail,  borderwidth=0, highlightthickness=0, padx=0, pady=0)
button_mail.image = photo_mail  # Сохраняем ссылку на изображение
button_mail.place(x=813, y=792)
#70


global countdown_label
countdown_label = tk.Label(main_frame, text="", font=("Arial", 15))
countdown_label.place(x=303, y=819, anchor=tk.CENTER)

update_countdown()  # Запускаем обратный отсчет

# --- Додавання кнопок музичного плеєра на main_frame ---
player = MusicPlayer(main_frame)

play_music_button = tk.Button(main_frame, text="Запустити музику", command=player.play_random_song)
play_music_button.place(x=23, y=12)

volume_down_button = tk.Button(main_frame, text="- Гучність", command=player.decrease_volume)
volume_down_button.place(x=143, y=12)

volume_up_button = tk.Button(main_frame, text="+ Гучність", command=player.increase_volume)
volume_up_button.place(x=223, y=12)

skip_button = tk.Button(main_frame, text="Пропустити пісню", command=player.skip_song)
skip_button.place(x=303, y=12)
# --- Кінець додавання кнопок музичного плеєра ---


notebook.bind("<Button-2>", close_tab) # Закрытие вкладки по средней кнопке мыши (колесику)
notebook.bind("<Button-3>", close_tab) # Альтернативно: закрытие по правой кнопке мыши


app.protocol("WM_DELETE_WINDOW", on_closing)


tk.mainloop()
app.mainloop()