Here Implemented Python + Django + Stripe API backend and frontend (BS5) with the following functionality:

- Django Item Model with fields (name, description, price), available for editing and adding in the site admin panel;
- Django Model API, for adding an ItemAPI obtained from the Dashboard Stripe and associated with the Item model with the OneToOneField primary key

On the main page, all services received from the Item model are displayed with the ability to go to a purchase or product information:
 - when you select the "buy" button - GET goes to /buy/{id} and goes to the Stripe payment page
 - when you select the "information" button - GET /item/{id}, with the output of all information from the Item model and the ability to "buy"

To start the server, you need to enter the service_site folder and type in the terminal - python manage.py runserver

All used libraries are listed in "requirements.txt"

________________________________________________________________________________________________________________________________________________


Здесь Реализована работа Python + Django + Stripe API бэкенда и фронтэнда (BS5) со следующим функционалом:

- Django Модель Item с полями (name, description, price), доступный для редактирования и добавления в админке сайта;
- Django Модель API, для добавления ItemAPI полученный с Dashboard Stripe и связанный с моделью Item первичным ключом OneToOneField

На главной странице выведены все услуги полученные из модели Item с возможностью перехода на покупку или информации о продукте:
 - при выбери кнопки "купить" - происходит переход по GET на /buy/{id} и переход на платежную страницу Stripe
 - при выбери кнопки "информация" - GET /item/{id}, с выводом всей информации из модели Item и возможность "купить"

Для запуска сервера необходимо войти в папку service_site и в терминале набрать - python manage.py runserver

Все исспользованные бибилиотеки указаны в "requirements.txt"
