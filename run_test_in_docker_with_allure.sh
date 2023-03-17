#!/bin/bash

# Собираем image с тегом tests
docker build -t tests .


# Запускаем контейнер под именем my_container из image tests
# В параметрах передаем логин, пароль, количество потоков для запуска и маркер
if [ $5 -eq "all" ]
then
  docker run --name my_container tests --url $1  --browser-name $2 --browser-version $3 --executor $4 -n 2
else
  docker run --name my_container tests --url $1  --browser-name $2 --browser-version $3 --executor $4 -m $5 -n 2
fi

# Копируем из контейнера созданный allure-report
docker cp my_container:/otus_opencart/allure-results .

# Запускаем хост для отчета аллюр (утилита лежит локально)
$6 serve allure-results

# Удаляем из системы созданный контейнер и образ
docker system prune -f
docker image rm tests
