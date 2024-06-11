# Установка базового образа
FROM python:3.6

RUN apt update && apt install -y openjdk-11-jre curl tar

RUN curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz
RUN tar -zxvf allure-2.13.8.tgz -C /opt/
RUN if [ ! -s "/usr/bin/allure" ]; then ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure;fi
RUN rm allure-2.13.8.tgz


# Установка рабочей директории внутри контейнера и переход в нее
WORKDIR /otus_opencart

# Копирование зависимостей
COPY requirements.txt .

# Обновление pip и установка зависимостей
RUN pip install -U pip && pip install -r requirements.txt
