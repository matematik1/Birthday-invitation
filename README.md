#Ukrainian language
# Birthday Invitation App

Ця програма на Python з використанням бібліотеки Tkinter являє собою інтерактивне вітання з днем народження. Користувач може вибрати, для кого саме він хоче відкрити персоналізоване запрошення, після чого відкривається нова вкладка з вітальним текстом та інтерактивними елементами.

## Основні можливості

* **Вибір одержувача:** На головній вкладці користувач може вибрати ім'я зі спадного списку ("Лари", "Сергія", "Алли", "Інших"), щоб відкрити відповідне персоналізоване запрошення.
* **Персоналізовані запрошення:** Для кожного обраного імені відкривається окрема вкладка з унікальним вітальним текстом та фоновим зображенням.
* **Інтерактивні елементи:** Деякі запрошення містять інтерактивні елементи, такі як випадкова зміна зображення при наведенні курсора.
* **Музичний плеєр:** На головній вкладці присутні кнопки для запуску випадкової фонової музики, регулювання гучності та пропуску поточної пісні.
* **Зворотний відлік до дня народження:** У нижній частині головної вкладки відображається зворотний відлік до визначеної дати (6 травня 2025 року).
* **Посилання на соціальні мережі та контактні дані:** На головній вкладці розміщені кнопки-іконки для швидкого переходу на Telegram, GitHub, Instagram та електронну пошту автора.
* **Імітація "вильоту":** При спробі закрити головне вікно програма імітує випадковий "виліт" з ймовірністю 100%.
* **Закриття вкладок:** Додаткові вкладки із запрошеннями можна закрити натисканням середньої або правої кнопки миші на вкладці.
* **Індикатор завантаження:** Перед відкриттям персоналізованого запрошення відображається індикатор прогресу, що імітує процес завантаження.

## Технології

* **Python:** Основна мова програмування.
* **Tkinter:** Стандартна бібліотека Python для створення графічних інтерфейсів користувача.
* **ttk (Themed Tkinter):** Набір віджетів Tkinter з підтримкою тем для більш сучасного вигляду.
* **PIL (Pillow):** Бібліотека для роботи з зображеннями (відкриття, зміна розміру, перетворення у формат, придатний для Tkinter).
* **pygame:** Бібліотека для роботи з мультимедіа, використовується для відтворення фонової музики.
* **webbrowser:** Модуль для відкриття веб-посилань у браузері за замовчуванням.
* **datetime:** Модуль для роботи з датою та часом, використовується для зворотного відліку.
* **time:** Модуль для роботи з часом, використовується для імітації завантаження та затримки.
* **random:** Модуль для генерації випадкових чисел, використовується для вибору випадкових зображень та імітації "вильоту".
* **threading:** Модуль для створення та керування потоками, використовується для асинхронного відтворення музики.
* **itertools:** Модуль, що надає інструменти для роботи з ітераторами, використовується для циклічного відтворення GIF-анімацій.
* **os:** Модуль для взаємодії з операційною системою, використовується для негайного завершення процесу при імітації "вильоту".

## Використання:

1.  Після запуску програми ви побачите головне вікно з випадаючим списком.
2.  Оберіть ім'я людини, для якої ви хочете відкрити запрошення.
3.  Натисніть на кнопку "Відкрити запрошення", що з'явиться.
4.  Відкриється нова вкладка з персоналізованим вітанням.
5.  На головній вкладці ви можете стежити за зворотним відліком до дня народження та використовувати кнопки для переходу на соціальні мережі або відправки електронного листа.
6.  Використовуйте кнопки внизу головної вкладки для керування музичним плеєром.
7.  Щоб закрити додаткову вкладку, натисніть на неї середньою або правою кнопкою миші.
8.  Для закриття всієї програми натисніть на кнопку закриття вікна. Будьте готові до несподіваної "помилки"!

## Встановлення
* Скачайте останю версію setup в релізах!!!

## Автор:

\[matematik1] ([GitHub профіль](https://github.com/matematik1))

## Контакти:

* Telegram: [https://t.me/yurch1ks](https://t.me/yurch1ks)
* Instagram: [https://www.instagram.com/matemch1k?igsh=dDN5NjM5MmFybHU=](https://www.instagram.com/matemch1k?igsh=dDN5NjM5MmFybHU=)
* Email: shmitayura@gmail.com

#English
# Birthday Invitation App

This Python application, built with the Tkinter library, is an interactive birthday greeting. Users can select who they want to open a personalized invitation for, which then opens a new tab with a greeting message and interactive elements.

---

## Key Features

* **Recipient Selection:** On the main tab, users can choose a name from a dropdown list ("Lary," "Serhiy," "Alla," "Others") to open the corresponding personalized invitation.
* **Personalized Invitations:** Each selected name opens a separate tab with a unique greeting message and background image.
* **Interactive Elements:** Some invitations include interactive elements, such as random image changes on hover.
* **Music Player:** The main tab features buttons to start random background music, adjust volume, and skip the current song.
* **Birthday Countdown:** The bottom of the main tab displays a countdown to a specified date (May 6, 2025).
* **Social Media and Contact Links:** The main tab includes icon buttons for quick access to the author's Telegram, GitHub, Instagram, and email.
* **"Crash" Simulation:** When attempting to close the main window, the application simulates a random "crash" with 100% probability.
* **Tab Closing:** Additional invitation tabs can be closed by clicking the middle or right mouse button on the tab.
* **Loading Indicator:** Before opening a personalized invitation, a progress indicator is displayed, simulating a loading process.

---

## Technologies

* **Python:** The primary programming language.
* **Tkinter:** Python's standard library for creating graphical user interfaces.
* **ttk (Themed Tkinter):** A set of Tkinter widgets with theme support for a more modern look.
* **PIL (Pillow):** A library for image processing (opening, resizing, converting to a Tkinter-compatible format).
* **pygame:** A library for multimedia, used for playing background music.
* **webbrowser:** A module for opening web links in the default browser.
* **datetime:** A module for working with dates and times, used for the countdown.
* **time:** A module for working with time, used for loading simulation and delays.
* **random:** A module for generating random numbers, used for selecting random images and simulating the "crash."
* **threading:** A module for creating and managing threads, used for asynchronous music playback.
* **itertools:** A module providing tools for working with iterators, used for looping GIF animations.
* **os:** A module for interacting with the operating system, used for immediate process termination during the "crash" simulation.

---

## Usage

1.  After launching the application, you'll see the main window with a dropdown list.
2.  Select the name of the person for whom you want to open an invitation.
3.  Click the "Open Invitation" button that appears.
4.  A new tab with a personalized greeting will open.
5.  On the main tab, you can monitor the birthday countdown and use the buttons to navigate to social media or send an email.
6.  Use the buttons at the bottom of the main tab for controlling the music player.
7.  To close an additional tab, click on it with the middle or right mouse button.
8.  To close the entire program, click the window's close button. Be prepared for an unexpected "error"!

---

## Installation

* Download the latest setup version from the [releases](https://github.com/matematik1/Birthday_invitation/releases)!

---

## Author

[matematik1](https://github.com/matematik1)

---

## Contact

* Telegram: [https://t.me/yurch1ks](https://t.me/yurch1ks)
* Instagram: [https://www.instagram.com/matemch1k?igsh=dDN5NjM5MmFybHU=](https://www.instagram.com/matemch1k?igsh=dDN5NjM5MmFybHU=)
* Email: shmitayura@gmail.com
