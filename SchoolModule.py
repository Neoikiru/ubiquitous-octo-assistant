import re
from bs4 import BeautifulSoup as bs
import requests
from fuzzywuzzy import fuzz
import datetime
from PyQt6.QtCore import pyqtSignal, QObject
import config


class Module:
    def __init__(self, module_name, tests, creative):
        self.module_name = module_name
        self.tests = tests
        self.creative = creative


class Course:
    def __init__(self, course_name, modules):
        self.course_name = course_name
        self.modules = modules


# course_test = Course(
#     course_name='Algebra',
#     modules=[
#         Module(
#             module_name='Module 1',
#             tests=['test1', 'test2'],
#             creative=['creative1', 'creative2']
#         ),
#         Module(
#             module_name='Module 2',
#             tests=['test1', 'test2'],
#             creative=['creative1', 'creative2']
#         )
#     ]
# )


class Lesson:
    def __init__(self, date, name, title, description):
        self.date = date
        self.name = name
        self.title = title
        self.description = description


class SchoolAutomationSystem(QObject):
    StatusUI = pyqtSignal(str)
    SchoolOutputText = pyqtSignal(str, list)

    def __init__(self):
        super().__init__()

    def display_tasks(self):
        s = requests.session()
        tasks = []
        login_data = {"login": config.EDU_LOGIN, "password": config.EDU_PASSWORD}
        try:
            response = s.post("https://edu.edu.vn.ua/user/login", login_data, verify=False)
            if str(response.url) == 'https://edu.edu.vn.ua/?error=true':
                self.StatusUI.emit('Wrong login or pass!')
                return
            home_page = s.get('https://edu.edu.vn.ua/course/userlist')
            home_soup = bs(home_page.content, "html.parser")
            courses = None
            courses = home_soup.find_all('a', href=re.compile('/course/view/'))
            if courses is None:
                self.StatusUI.emit('Something went worng!')
                return
            for course in courses:
                # main_out = ''
                main_course = Course(
                    course_name='',
                    modules=[]
                )
                printMain = False

                course_link = f'https://edu.edu.vn.ua{course["href"]}'
                course_page = s.get(course_link)
                course_soup = bs(course_page.content, "html.parser")

                course_name = course_soup.find('h2', string=re.compile('Курс:')).text
                # main_out += f"{course_name} ↓\n"
                main_course.course_name = course_name

                lessons = course_soup.find_all('a', href=re.compile(f'/part/view/{course["href"].split("/")[3]}/'))
                # lessons = course_soup.find_all('a', href=re.compile('/part/view/982/'))
                for less in lessons:
                    # output_text = ''
                    shouldPrint = False
                    main_module = Module(
                        module_name='',
                        tests=[],
                        creative=[],
                    )

                    lesson_url = f'https://edu.edu.vn.ua{less["href"]}'
                    lesson_page = s.get(lesson_url)
                    lesson_soup = bs(lesson_page.content, "html.parser")

                    lesson_name = lesson_soup.find("h3").text.replace(course_name.replace("Курс: «", "").replace("»", ""), "")
                    # output_text += f'            {lesson_name} ↓\n'
                    main_module.module_name = lesson_name

                    materials = lesson_soup.find_all('table', 'datatable')
                    tests_name = []
                    for material in materials:
                        current_group = material.previous_sibling.previous_sibling.get_text(strip=True)
                        # if current_group != 'Навчальні матеріали':
                            # output_text += f'                ——{current_group}\n'
                        if current_group == 'Тестування':
                            tests = material.find_all('tr')
                            for test in tests:
                                if test.find_all('div', string=re.compile('Не пройдено')):
                                    shouldPrint = True
                                    printMain = True
                                    test_name = test.find('a').text
                                    tests_name.append(test_name)
                                    # output_text += f'                    ↪ {test_name}\n'
                                    main_module.tests.append(test_name)
                        elif current_group == 'Творчі завдання':
                            creative = material.find_all('tr')
                            for cr in creative:
                                if cr.find_all('div', string=re.compile('Не пройдено')):
                                    shouldPrint = True
                                    printMain = True
                                    cr_name = cr.find('a').text
                                    # output_text += f'                    ↪ {cr_name}\n'
                                    main_module.creative.append(cr_name)
                    if shouldPrint:
                        main_course.modules.append(main_module)
                        # print(output_text)
                        # main_out += output_text
                if printMain:
                    tasks.append(main_course)
                    # print(main_out)
                    # print(main_module)
            self.SchoolOutputText.emit('tasks', tasks)
        except requests.exceptions.ConnectionError:
            self.StatusUI.emit('Connection refused!')
            return

    def __scan_for_class(self, text):
        confidence = {
            '11-А': 0,
            '11-Б': 0
        }
        for letter in confidence.keys():
            for sentence in text.split(' '):
                ratio = fuzz.WRatio(letter, sentence)
                if ratio > confidence[letter]:
                    confidence[letter] = ratio
        return confidence

    def __check_date(self, day=None, month=None):
        day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        date = datetime.datetime.today() + datetime.timedelta(days=1)
        year = date.year
        day_to_check = datetime.datetime.strptime(f'{day} {month} {year}', '%d %m %Y').weekday()
        if day_name[day_to_check] == 'Saturday' or day_name[day_to_check] == 'Sunday':
            return False
        else:
            return True

    def display_tomorrow_schedule(self, day=None, month=None):
        date = datetime.datetime.today() + datetime.timedelta(days=1)
        if month is None:
            month = date.month
        if day is None:
            day = date.day

        if not self.__check_date(day, month):
            self.StatusUI.emit('There is no lessons for the day!')
            return
        s = requests.session()
        login_data = {"login": config.EDU_LOGIN, "password": config.EDU_PASSWORD}
        try:
            response = s.post("https://edu.edu.vn.ua/user/login", login_data, verify=False)
            if str(response.url) == 'https://edu.edu.vn.ua/?error=true':
                self.StatusUI.emit('Wrong login or pass!')
                return
            home_page = s.get(f"https://edu.edu.vn.ua/calendar/view/2023/{month}/all")
            soup = bs(home_page.content, "html.parser")
            calendar = soup.find_all('div', 'calendar-cell-header', string=re.compile(f'{day}'))
            required_cell = None
            for cell in calendar:
                text = "".join(cell.text.split())
                if text == str(day):
                    required_cell = cell
                    break
            if required_cell is None:
                self.StatusUI.emit('Something went wrong!')
                return

            return_data = []
            for subject in required_cell.find_next_sibling('div').find_all('li'):
                date = subject.find('p', 'date').text
                name = subject.find('p', 'course').text
                title = subject.find('h2', attrs={"data-event-field": "title"}).text
                description = subject.find('p', attrs={"data-event-field": "description"}).text

                title_scan = self.__scan_for_class(title)

                key_list = list(title_scan.keys())
                val_list = list(title_scan.values())

                if val_list.count(val_list[0]) == len(val_list) or max(title_scan.values()) <= 60 or key_list[val_list.index(max(title_scan.values()))] == '11-Б':
                    return_data.append(Lesson(
                        date=date,
                        name=name,
                        title=title,
                        description=description
                    ))
                    # print(return_data)
            # print('Successfully executed schedule')
            self.SchoolOutputText.emit('schedule', return_data)
        except requests.exceptions.ConnectionError:
            self.StatusUI.emit('Connection refused!')
            return


# if __name__ == "__main__":
#     warnings.filterwarnings('ignore')
#     edu = SchoolAutomationSystem(
#         login='bondarenko_a_o_2006_08_31',
#         password='rqyb2QG6weB5qWK'
#     )
#     startTime = time.time()
#     edu.display_tomorrow_schedule()
#     print(f'It took: {time.time() - startTime}secs')
#     # edu.display_tasks()
#     # lessons = edu.display_tomorrow_schedule(day=4, month=4)
#     # if lessons:
#     #     for less in lessons:
#     #         print(less.title)
