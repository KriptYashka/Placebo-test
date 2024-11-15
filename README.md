# Placebo-test

Запуск проекта:

1. Подготовить виртуальное окружение

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

2. Создать и применить миграции БД

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

2.1 [Опционально] Перед началом работы скачать БД (чтобы не создавать свои модели).

[Ссылка на БД](https://file.io/sYbVX73N8pvB)

3. Запустить сервер

```bash
python3 manage.py runserver
```


---

Postman
---

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://app.getpostman.com/run-collection/21066826-fff39b60-fb06-48a2-ae53-b019850e9003?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D21066826-fff39b60-fb06-48a2-ae53-b019850e9003%26entityType%3Dcollection%26workspaceId%3D9d498819-4129-4dbf-9b0b-5ad3b5b0d539)