<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Neoikiru/ubiquitous-octo-assistant">
    <img src="GUI/Icons/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Virtual Assistant</h3>

  <p align="center">
    Fancy virtual assistant with cool features
    <br />
    <a href="https://github.com/Neoikiru/ubiquitous-octo-assistant"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Neoikiru/ubiquitous-octo-assistant/blob/main/README.md">English</a>
    ·
    <a href="https://github.com/Neoikiru/ubiquitous-octo-assistant/blob/main/README.ua.md">Ukrainian</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

![product-screenshot](https://github.com/Neoikiru/ubiquitous-octo-assistant/assets/101185766/bdca7e43-c628-4b3f-960b-07223b6c0dfd)

  The project is a virtual AI assistant that incorporates various features. It includes voice command recognition, allowing users to give instructions such as "open YouTube," "play music," "schedule for tomorrow," and other similar commands. The assistant can also answer questions using ChatGPT, a language model developed by OpenAI. Additionally, the project utilizes camera and gesture recognition technology to control the volume on a user's PC. Overall, this project aims to provide a comprehensive and interactive AI assistant experience with multiple functionalities.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With
* [![Python][Python.com]][Python-url]
* [![MediaPipe][Mediapipe.com]][Mediapipe-url]
* [![OpenAI][OpenAI.com]][OpenAI-url]
* [![PyQt][PyQt.com]][PyQt-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites
* ```sh
  python >= 3.10
  ```

### Installation

1. Get a free API Keys at [ChatGPT](https://platform.openai.com/account/api-keys), [ElevenLabs](https://docs.elevenlabs.io/authentication/01-xi-api-key), [PicoVoice](https://console.picovoice.ai/profile)
2. Clone the repo
   ```cmd
   git clone https://github.com/Neoikiru/ubiquitous-octo-assistant.git
   ```
3. Install all requirements
   ```cmd
    pip install -r requirements.txt
    ```
4. Enter your API in `config.py`
   ```python
   GPT_TOKEN = 'ENTER YOUR API';
   PICOVOICE_ACCESS_KEY  = 'ENTER YOUR API';
   ELEVENLABS_API_KEY  = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

<!-- Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources. -->
Run main Script
*  ```cmd
   py main.py
   ```
Enter your edu.edu login and password
*  [```
   Edu.edu login <---
   Edu.edu password <---
   ```
  It will be saved in `config.py`]
You can set activation word in `config.py`, 
   'Hey, Elli!' - default,
   'Start' - other option
*  ```python
   ACTIVATION_WORD = 'Hey, Elli'  # [Start; Hey, Elli]
   ```
Rotate your index finger clockwise or counterclockwise to increase or decrease volume respectively
  Hold your hand closed for a few seconds to mute master volume
*  ```
   Camera feed preview to test
   ```
<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add multilangual support
- [x] Add edu.edu integration
- [ ] Reorganize repo structure
- [x] Add multilangual README support
    - [x]  Ukrainian
    - [x]  English
- [x] Rename constant variables
- [x] Add requirements.txt file (URGENT)
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

Creator - [@Neoikiru](https://t.me/Neoikiru) - neoikiru@gmail.com

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
