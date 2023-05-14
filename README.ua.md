<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Neoikiru/ubiquitous-octo-assistant">
    <img src="GUI/Icons/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Віртуальний асистент</h3>

  <p align="center">
    Віртуальний асистент з багатьма можливостями
    <br />
    <a href="https://github.com/Neoikiru/ubiquitous-octo-assistant"><strong>Документація »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Neoikiru/ubiquitous-octo-assistant/blob/main/README.md">Англійська</a>
    ·
    <a href="https://github.com/Neoikiru/ubiquitous-octo-assistant/blob/main/README.ua.md">Українська</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Зміст</summary>
  <ol>
    <li>
      <a href="#Про-проєкт">Про проєкт</a>
      <ul>
        <li><a href="#Побудовано-з-використанням">Побудовано з використанням</a></li>
      </ul>
    </li>
    <li>
      <a href="#Початок-роботи">Початок роботи</a>
      <ul>
        <li><a href="#Передумови">Передумови</a></li>
        <li><a href="#Установка">Установка</a></li>
      </ul>
    </li>
    <li><a href="#Використання">Використання</a></li>
    <li><a href="#Додавання-користувацьких-команд">Додавання користувацьких команд</a></li>
    <li><a href="#План-розвитку">План розвитку</a></li>
    <li><a href="#Ліцензія">Ліцензія</a></li>
    <li><a href="#Контакти">Контакти</a></li>
    <li><a href="#Подяки">Подяки</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## Про проєкт
![product-screenshot](https://github.com/Neoikiru/ubiquitous-octo-assistant/assets/101185766/3b733a69-14e1-4cee-b584-fc419ded7b2d)

 Проектом є віртуальний AI-помічник, що має ряд функціональних можливостей. Він вміє розпізнавати голосові команди, такі як "відкрий YouTube", "програй музику", "розклад на завтра", "завдання в школі" та інші. Помічник також вміє відповідати на питання, використовуючи модель ChatGPT, розроблену OpenAI. Крім того, проект використовує камеру та технологію розпізнавання жестів для керування гучністю на комп'ютері користувача. Загалом, цей проект має на меті забезпечити комплексний та інтерактивний досвід з використанням AI-помічника з багатьма функціями.


<p align="right">(<a href="#readme-top">повернутися нагору</a>)</p>


### Побудовано з використанням
* [![Python][Python.com]][Python-url]
* [![MediaPipe][Mediapipe.com]][Mediapipe-url]
* [![OpenAI][OpenAI.com]][OpenAI-url]
* [![PyQt][PyQt.com]][PyQt-url]
* [![AutoHotKey][AutoHotKey.com]][AutoHotKey-url]
* 
<p align="right">(<a href="#readme-top">повернутися нагору</a>)</p>



<!-- GETTING STARTED -->
## Початок роботи

Щоб отримати локальну копію та розпочати роботу, слідувати цим простим інструкціям.

### Передумови
* ```sh
  python >= 3.10
  ```

### Установка

1. Отримайте безкоштовні API-ключі на [ChatGPT](https://platform.openai.com/account/api-keys), [ElevenLabs](https://docs.elevenlabs.io/authentication/01-xi-api-key), [PicoVoice](https://console.picovoice.ai/profile)
2. Клонуйте репозиторій
   ```cmd
   git clone https://github.com/Neoikiru/ubiquitous-octo-assistant.git
   ```
3. Встановіть всі необхідні компоненти
   ```cmd
    pip install -r requirements.txt
    ```
4. Введіть свої API-ключі в файлі `config.py`
   ```python
   GPT_TOKEN = 'ENTER YOUR API';
   PICOVOICE_ACCESS_KEY  = 'ENTER YOUR API';
   ELEVENLABS_API_KEY  = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">повернутися нагору</a>)</p>

<!-- USAGE EXAMPLES -->
## Використання

<!-- Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources. -->
Запустіть головний скрипт
*  ```cmd
   py main.py
   ```
 
Введіть ваш логін і пароль від edu.edu
*  ```
   Edu.edu login <---
   Edu.edu password <---
   ```
   + Вони будуть збережені у `config.py`
 
Ви можете встановити ключове слово у `config.py`, 
   'Хей, Еллі!' - за замовчуванням,
   'Старт' - інший варіант
*  ```python
   ACTIVATION_WORD = 'Hey, Elli'  # [Start; Hey, Elli]
   ```
   
Повертайте вказівний палець за або проти годинникової стрілки, щоб відповідно збільшити або зменшити гучність
  Тримайте руку закритою на кілька секунд, щоб вимкнути основну гучність
*  ```
   Як це виглядає можна побачити у вікні камера
   ```
Скажіть що-небудь, і якщо це не вбудована команда, асистент відповість вам, використовуючи модель GPT-3.5.
В іншому випадку буде виконана одна з наступних команд (повний список можна знайти в файлі `customCommands.yaml`):
*  ```
   Відкрий YouTube
   Прослухати музику
   ...
   ```
<p align="right">(<a href="#readme-top">повернутися нагору</a>)</p>


## Додавання користувацьких команд

По-перше, всі користувацькі команди є виконуваними файлами .exe, які скомпільовані за допомогою `AutoHotKey`.

Створіть скрипт AHK, скомпілюйте його в .exe та помістіть у папку "scripts".
*  ```cmd
   scripts/your_script.exe
   ```

Відкрийте файл `customCommands.yaml` і додайте свою команду, використовуючи наступну структуру:

*  ```yaml
     - command:
      action: ahk
      exe: ваш_файл.exe
      args: # Будь-які аргументи, необхідні для виконання вашого .exe (див. нижче)
      phrases:
        - ваша_фраза1
        - ваша_фраза2
        - ваша_фраза3
        - ваша_фраза4
   ```
   

* Приклад аргументів. Команда, яка буде виконуватися в командному рядку за допомогою цього блоку:
   ```yaml
     - command:
      action: ahk
      exe: web.exe
      args: 
        - youtube.com
      phrases:
        - Відкрий YouTube
   ```
   Тепер, якщо ми скажемо `Відкрий YouTube`, команда, яка наведена нижче, буде виконана в командному рядку:
   ```cmd
     .../scripts/web.exe youtube.com
   ```
<p align="right">(<a href="#readme-top">повернутися нагору</a>)</p>

<!-- ROADMAP -->
## План розвитку

- [x] Додати підтримку мультиязиковості
- [x] Додати інтеграцію з edu.edu
- [ ] Переробити структуру репозиторію
- [x] Додати підтримку мультиязикового README
    - [x]  Українська
    - [x]  Англійська
- [x] Перейменувати постійні змінні
- [x] Додати файл requirements.txt (НЕОБХІДНО)
- [x] Додати блок з командами та загальними інструкціями по використанню (НЕОБХІДНО)
 

Перегляньте [Відкриті проблеми](https://github.com/Neoikiru/ubiquitous-octo-assistant/issues) для повного списку запропонованих функцій (та відомих проблем).

<p align="right">(<a href="#readme-top">повернутися нагору</a>)</p>



<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- LICENSE -->
## Ліцензія

Поширюється за ліцензією MIT. Докладніше дивіться в файлі `LICENSE.txt`.

<p align="right">(<a href="#readme-top">повернутися нагору</a>)</p>



<!-- CONTACT -->
## Контакти

Автор - [@Neoikiru](https://t.me/Neoikiru) - neoikiru@gmail.com

Посилання на проект: [https://github.com/Neoikiru/ubiquitous-octo-assistant](https://github.com/Neoikiru/ubiquitous-octo-assistant)

<p align="right">(<a href="#readme-top">повернутися нагору</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Подяки

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">повернутися нагору</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[Mediapipe.com]: https://img.shields.io/badge/Mediapipe-20232A?style=for-the-badge&logo=devdotto&logoColor=#003E54
[Mediapipe-url]: https://developers.google.com/mediapipe
[PyQt.com]: https://img.shields.io/badge/PyQT-20232A?style=for-the-badge&logo=qt&logoColor=#41CD52
[PyQt-url]: https://www.qt.io/product/ui-design-tools
[OpenAI.com]: https://img.shields.io/badge/OpenAI-20232A?style=for-the-badge&logo=openai&logoColor=#412991
[OpenAI-url]: https://openai.com/
[Python.com]: https://img.shields.io/badge/Python-20232A?style=for-the-badge&logo=python&logoColor=#3776AB
[Python-url]: https://www.python.org/
[AutoHotKey.com]: https://img.shields.io/badge/AutoHotKey-20232A?style=for-the-badge&logo=autohotkey&logoColor=#334455
[AutoHotKey-url]: https://www.autohotkey.com/
