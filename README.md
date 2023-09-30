# Пример проекта UI автотестов на демо-сайте "webdriveruniversity.com"
> WebDriverUniversity.com - это набор обучающих страниц с элементами, с которыми можно взаимодействовать.

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="images/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>

## Покрываемый функционал
- Проверка раскрытия и содержимой информации на странице с аккордеоном
- Проверка страницы c кнопками и модальными окнами
- Проверка страницы cо списком задач (добавление/вычеркивание)
- Проверка страницы с обратной связью


## Запуск тестов
#### По умолчанию все тесты запускаются удалённо на Selenoid

### Для локального запуска
1. Склонируйте репозиторий
2. Откройте проект в PyCharm
3. Введите в териминале команду
``` 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```

### Запуск тестов в [Jenkins](https://jenkins.autotests.cloud/job/qa_guru_graduation_project_UI/)
Нажмите кнопку «Собрать сейчас»
<p><img src="images/screenschot/jenkins_job.png"></p>

### <img width="3%" title="Allure Report" src="images/logo/allure_report.png"> Отчетность о прохождении тестов в Allure
#### Если тест запускался локально:
Введите в терминале команду 
```
allure serve allure-results
``` 
#### Если тест запускался в Jenkins
Нажмите Allure Report или кликните по иконке отчёта в завершённой сборке
<p><img title="Jenkins_Allure" src="images/screenschot/jenkins_allure.png"></p>

### Примеры отображения тестов
<img title="Allure_Report" src="images/screenschot/Allure Report0.png">
<img title="Allure_Example_Report" src="images/screenschot/Allure Report.png">

#### Так же в отчетах для каждого UI-теста прикрепляется видео
<img src="images/screenschot/video.gif">

### <p><img width="3%" title="Telegram" src="images/logo/tg.png"> Telegram</p>
<p>Настроена отправка отчета в Telegram</p>
<img title="Telegram_report_screen" src="images/screenschot/telegram.png">