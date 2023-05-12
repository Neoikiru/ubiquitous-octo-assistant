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
      <a href="#about-the-project">Про проєкт</a>
      <ul>
        <li><a href="#built-with">Побудовано з використанням</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Початок роботи</a>
      <ul>
        <li><a href="#prerequisites">Передумови</a></li>
        <li><a href="#requirements">Вимоги</a></li>
        <li><a href="#installation">Установка</a></li>
      </ul>
    </li>
    <li><a href="#usage">Використання</a></li>
    <li><a href="#roadmap">План розвитку</a></li>
    <li><a href="#license">Ліцензія</a></li>
    <li><a href="#contact">Контакти</a></li>
    <li><a href="#acknowledgments">Подяки</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## Про проєкт

![product-screenshot](https://github.com/Neoikiru/ubiquitous-octo-assistant/assets/101185766/bdca7e43-c628-4b3f-960b-07223b6c0dfd)

 Проектом є віртуальний AI-помічник, що має ряд функціональних можливостей. Він вміє розпізнавати голосові команди, такі як "відкрий YouTube", "програй музику", "розклад на завтра", "завдання в школі" та інші. Помічник також вміє відповідати на питання, використовуючи модель ChatGPT, розроблену OpenAI. Крім того, проект використовує камеру та технологію розпізнавання жестів для керування гучністю на комп'ютері користувача. Загалом, цей проект має на меті забезпечити комплексний та інтерактивний досвід з використанням AI-помічника з багатьма функціями.


<p align="right">(<a href="#readme-top">повернутися нагору</a>)</p>


### Побудовано з використанням
* [![Python][Python.com]][Python-url]
* [![MediaPipe][Mediapipe.com]][Mediapipe-url]
* [![OpenAI][OpenAI.com]][OpenAI-url]
* [![PyQt][PyQt.com]][PyQt-url]

<p align="right">(<a href="#readme-top">повернутися нагору</a>)</p>



<!-- GETTING STARTED -->
## Початок роботи

Щоб отримати локальну копію та розпочати роботу, слідувати цим простим інструкціям.

### Передумови
* ```sh
  python >= 3.10
  ```

### Installation

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
   python main.py
   ```
<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add multilangual support
- [x] Add edu.edu integration
- [ ] Reorganize repo structure
- [ ] Add multilangual README support
    - [ ]  Ukrainian
    - [x]  English
- [ ] Rename constant variables
- [ ] Add requirements.txt file (URGENT)
- [ ] Add block about commands and genral usage instuctions (URGENT)
 

See the [open issues](https://github.com/Neoikiru/ubiquitous-octo-assistant/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@Neoikiru](https://t.me/Neoikiru) - neoikiru@gmail.com

Project Link: [https://github.com/Neoikiru/ubiquitous-octo-assistant](https://github.com/Neoikiru/ubiquitous-octo-assistant)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[Mediapipe.com]: https://img.shields.io/badge/Mediapipe-20232A?style=for-the-badge&logo=devdotto&logoColor=#003E54
[Mediapipe-url]: https://developers.google.com/mediapipe
[PyQt.com]: https://img.shields.io/badge/PyQT-20232A?style=for-the-badge&logo=qt&logoColor=#41CD52
[PyQt-url]: https://www.qt.io/product/ui-design-tools
[OpenAI.com]: https://img.shields.io/badge/OpenAI-20232A?style=for-the-badge&logo=openai&logoColor=#412991
[OpenAI-url]: https://openai.com/
[Python.com]: https://img.shields.io/badge/Python-20232A?style=for-the-badge&logo=python&logoColor=#3776AB
[Python-url]: https://www.python.org/
