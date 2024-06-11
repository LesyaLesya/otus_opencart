## Описание проекта

Проект по автоматизации тестирования UI cms Opencart на selenium + pytest.

____

## Список необходимых предустановленных приложений и утилит

- Python3 - для локального и удаленного (selenoid) запуска через консоль/ide
- Chromedriver - для локального запуска тестов в Chrome
- Geckodriver - для локального запуска тестов в Firefox
- Docker - для запуска тестов в контейнере и в Jenkins + для запуска opencart
- Selenoid + образы нужных браузеров - для удаленного запуска через консоль/ide/docker/jenkins
- Allure - для получения отчета при запуске через консоль/ide/docker
- Jenkins - для запуска в Jenkins
____

## Запуск приложения Opencart
(Должен быть всегда запущен для прогона тестов)

1. Запустить Docker
2. Приложение собирается из docker-compose.opencart.yml
Значение для OPENCART_HOST передается в командной строке через переменную local_ip - адрес вашей машины в сети
(узнать через ifconfig).
Выполнить команду:

```
local_ip=123.123.123.123 docker-compose -f docker-compose.opencart.yml up -d
```
После этого станут доступны: 
- приложение local_ip:80,
- админка local_i:8888,
- БД local_ip:3306.


Подсказка - как применить сделанные в docker-compose.yml изменения:
```
docker-compose -f docker-compose.opencart.yml down

Удалить все контейнеры:
docker rm -f $(docker ps -a -q)

Удалить все тома:
docker volume rm $(docker volume ls -q)

Перезапустить контейнеры:
docker-compose up -d

```

______

## Установка для локального и удаленного запуска тестов через ide/консоль
Установить - Python3, Chromedriver, Geckodriver, Allure, Selenoid (+образы браузеров)


### Общие шаги
- Скачать репозиторий на свою машину:

```
git clone repository_url
```

- Перейти в директорию скачанного репозитория

- Установить и активировать виртуальное окружение:

```
python3 -m venv venv
source venv/bin/activate
```
- Обновить PIP и установить зависимости:

```
pip install -U pip
pip install -r requirements.txt
```

- Выбрать интерпретатор для проекта (для запуска тестов через консоль/ide)

- Запустить Opencart

- Создать в корне проекта файл .env в формате:

Для запуска в selenoid:
```
HOST=x.x.x.x
BROWSER_NAME=chrome
BROWSER_VERSION=100.0
EXECUTOR=x.x.x.x #selenoid host
WINDOW_SIZE=1920,1080
LOCAL=''
```
Для локального запуска:
```
HOST=x.x.x.x
BROWSER_NAME=firefox
WINDOW_SIZE=1920,1080
LOCAL=1
```

- После запуска тестов одним из вариантов представленных ниже получить Allure отчет:
В консоли выполнить команду, в качестве параметра указав путь до исполняемого файла allure на вашей машине:

```
./run_allure_report.sh /path/to/allure/bin
Пример: ./run_allure_report.sh /Applications/allure/bin/allure
```


#### Локальный запуск

В консоли (из директории проекта) выполнить команду:

```
pytest -m marker  -n 2 tests/
```
где:

- -n - во сколько потоков запускать тесты, если не указывать параметр при запуске - тесты будут запущены в 1 поток.
- -m - маркер группы тестов


#### Удаленный запуск (Selenoid)

1.Запустить Selenoid:
перейти в директорию с исполняемым файлом и выполнить команды, указав вместо ./bin имя исполняемого файла:
UI станет доступен на localhost:8080.
```
./bin selenoid start
./bin selenoid-ui start
```

2.В консоли (из директории проекта) выполнить команду:

```
pytest -m marker -n 2 tests/
```
где:

- -n - во сколько потоков запускать тесты, если не указывать параметр при запуске - тесты будут запущены в 1 поток.
- -m - маркер группы тестов
____


## Запуск тестов в Docker + Selenoid
Установить - Docker, Selenoid (+образы браузеров)

- Скачать репозиторий на свою машину:

```
git clone repository_url
```

- Перейти в директорию скачанного репозитория


- Запустить Docker + приложение opencart

- Запустить тесты:

```
docker-compose -f docker-compose.tests.yml up --build
```
Если надо запустить все тесты, то marker указать 'all'

____
