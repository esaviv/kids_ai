# Kids AI
### Описание
Тестовое наставника kids ai

### Технологии
aiogram==2.25.1 | python-dotenv==0.19.0

## Локальный запуск проекта:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/esaviv/kids_ai.git
```
```
cd kids_ai/
```
Создать файл .env и заполнить его по образцу .env.template.

Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv | python -m venv venv
```
```
source env/bin/activate | source venv/Scripts/activate
```
```
python3 -m pip install --upgrade pip | python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Запустить:
```
python main.py
```
Для наполнения БД используйте команду ```/admin```.

### Автор
esaviv
