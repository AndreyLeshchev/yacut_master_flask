# Foodgram
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Используемые технологии:
* Python
* Flask
* Sqlalchemy
* Alembic

## Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:

    ```
    git clone git@github.com:AndreyLeshchev/yacut_master_flask.git
    ```
    ```
    cd yacut_master_flask
    ```

2. Cоздать и активировать виртуальное окружение:
    
    ```
    python3 -m venv env
    ```
    
    * Если у вас Linux/macOS
    
        ```
        source env/bin/activate
        ```
    
    * Если у вас windows
    
        ```
        source venv/Scripts/activate
        ```
    
3. Обновить pip и установить зависимости из файла requirements.txt:

    ```
    python -m pip install --upgrade pip
    ```
    ```
    pip install -r requirements.txt
    ```
    
4. Выполнить миграции:

    ```
    flask db upgrade
    ```

    Запустить проект:
    ```
    flask run
    ```

## Примеры API запросов и ответов:

* Для получения длинной ссылки по короткой ссылке:

   
    > GET https://127.0.0.1:5000/api/id/{short_id}/

    Пример ответа:

    ```
    {
        "url": "string"
    }
    ```


* Для создания короткой ссылки:

    > POST http://127.0.0.1:5000/api/id/


    Пример запроса:

    ```
    {
        "url": "string",
        "custom_id": "string"
    }
    ```

    Пример ответа:

    ```
    {
        "url": "string",
        "short_link": "string"
    }
    ```

### Автор - [Андрей Лещев](https://github.com/AndreyLeshchev)