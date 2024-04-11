# tengryClone
This is my pet project. The clone of https://tengrinews.kz/

1. Как запустить проект?
   1.1 Установим питон : )
   Так как гитхаб не позволил мне выгрузить виртуальное окружение в репозиторий, нужно будет скачать интерпретатор питона на сайте python.org
   Далее в командно строке вводим pip install django.
   1.2 Запустим сервер
   Скачайте все файлы с репозитория в виде архива. Распакуйте архив и зайдите в папку django_news/. ВАЖНО: чтобы в этой папке был файл manage.py он самый главный.
    в папке с файлом manage.py запустите команду python manage.py runserver
    сайт создатся на локальном сервере http://127.0.0.1:8000/

2. Админская панель.
   2.1 Зайдите по ссылке http://127.0.0.1:8000/admin/
   2.2 Админские логин и пароль: login: nurbe  password: outpeertheN!
   2.3 на левой панели можете добавить статью либо категорию. (Все пункты относящиеся к статье вы можете добавлять не выходя со страницы добавления статьи)
   ![изображение](https://github.com/mountain-nomad/tengryClone/assets/119871226/711de6f6-a66c-49a7-acdc-83ba6746f0a2)

3. Разберем пункты с задания
- Реализуйте базовую функцию списка новостей для отображения списка новостных статей на фронтенде с данными с бэкенда. (Сделано)
- Позвольте пользователям кликать по статье для просмотра её детальной информации. (Сделано)
- Реализуйте пагинацию для управления отображением новостных статей. (Сделано)
- Введите возможность фильтровать новости по категориям. (Сделано) (Категории не ограничены и можно добавлять сколько угодно в админской панели)
- Обеспечьте функциональность поиска, позволяющую пользователям находить новости по ключевым словам.
  (Кстати для этого были добавлены статьи КНБ и НЕ КНБ, я просто пытался проверить как работает функция поиска если ключевое слово не первое, а один из дефолтных новостей с тегри начинался с КНБ) (Сделано)
- Включите функцию для сортировки новостных статей по дате публикации, чтобы первыми отображались последние новости.
  (Можно менять дату публикации, но не заходить в будущее, при создании статьи. В зависимости от этого статия будет отображаться на главной странице)

ЧТО БЫ ХОТЕЛЬСЬ ДОБАВИТЬ НА САЙТ:
-Возможность добавлять дополнительные фото (Для этого заранее была создана модель AdditionalImg)
-Возможность кастомизировать стиль статьи
-Коментарии к статьям
-Возможность создания аккаунтов и еженедельной рассылки
-Возможность для аккаунта подать заяку на авторство статьи
-Возможность добавления коментариев к статьям
-Мультиязычность сайта

Приступлю к изменениям после проверки. Как только дедлайн пройдет, изменений в этом репозитории не будет (academic integrity)

Так как время поджимало, не было возможности покреативить, но основные запросы были выполнены.
Было интересно, спасибо! : )
   

