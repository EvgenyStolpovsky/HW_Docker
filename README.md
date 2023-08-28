### 24.1 Вьюсеты и дженерики
#### Условия домашки

#### Задание 1. Создайте новый Django-проект, подключите DRF и внесите все необходимые настройки.

#### Задание 2. Создайте следующие модели:
Пользователь:
    - все поля от обычного пользователя, но авторизацию заменить на email;
    - телефон;
    - город;
    - аватарка.
Курс:
    - название,
    - превью (картинка),
    - описание.
Урок:
    - название,
    - описание,
    - превью (картинка),
    - ссылка на видео.


#### Задание 3. Опишите CRUD для моделей курса и урока, но при этом для курса сделайте через ViewSets, а для урока — через Generic-классы. Для работы контроллеров опишите простейшие сериализаторы.
___________________________________________________________________________________________________________________

### 24.2 Сериализаторы
#### Условия домашки

#### Задание 1. Для модели курса добавьте в сериализатор поле вывода количества уроков. Запишите в эту модель данные через инструмент фикстур или кастомную команду.

#### Задание 2. Добавьте новую модель.
    Платежи:
    - пользователь,
    - дата оплаты,
    - оплаченный курс или урок,
    - сумма оплаты,
    - способ оплаты — наличные или перевод на счет.


#### Задание 3. Для сериализатора для модели курса реализуйте поле вывода уроков.

#### Задание 4. Настройте фильтрацию для эндпоинтов вывода списка платежей с возможностями:
        - менять порядок сортировки по дате оплаты,
        - фильтровать по курсу или уроку,
        - фильтровать по способу оплаты.

_____________________________________________________________________________________________________________________

### 25.1 Права доступа в DRF
#### Условия домашки

#### Задание 1. Настройте в проекте использование JWT-авторизации и закройте каждый эндпоинт авторизацией.

#### Задание 2. Заведите группу модераторов и опишите для нее права работы с любыми уроками или курсами, 
#### но без возможности их удалять и создавать новые. Заложите функционал такой проверки в контроллеры.

#### Задание 3. Опишите права доступа для объектов таким образом, чтобы пользователи, которые не входят в группу 
#### модераторов, могли видеть и редактировать только свои курсы и уроки.

_________________________________________________________________________________________________________________

### 25.2 Валидаторы, пагинация и тесты
#### Условия домашки

#### Задание 1. Для сохранения уроков и курсов реализуйте дополнительную проверку на отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com.

#### Задание 2. Добавьте модель подписки на обновления курса для пользователя. Вам необходимо реализовать эндпоинт для установки подписки пользователя и на удаление подписки у пользователя.
#### При этом при выборке данных по курсу пользователю необходимо присылать признак подписки текущего пользователя на курс. То есть давать информацию, подписан пользователь на обновления курса или нет.

#### Задание 3. Реализуйте пагинацию для вывода всех уроков и курсов.

#### Задание 4. Напишите тесты, которые будут проверять корректность работы CRUD уроков и функционал работы подписки на обновления курса.

_________________________________________________________________________________________________________________

### 26.1 Документирование и безопасность
#### Условия домашки

#### Задание 1. Подключить и настроить вывод документации для проекта. Убедиться, что каждый из реализованных эндпоинтов описан в документации верно, при необходимости описать вручную.

#### Задание 2. Подключить возможность оплаты курсов через https://stripe.com/docs/api.

__________________________________________________________________________________________________________________

### 26.2. Celery
#### Условия домашки

#### Задание 1. Настройте проект для работы с Celery. Также настройте celery-beat для выполнения последующих задач.

#### Задание 2. Ранее вы реализовывали функционал подписки на обновление курсов. Теперь добавьте асинхронную рассылку писем пользователям об обновлении материалов курса.

#### Задание 3. С помощью celery-beat реализуйте фоновую задачу, которая будет проверять пользователей по дате последнего входа по полю last_login и, если пользователь не заходил более месяца, блокировать его с помощью флага is_active.