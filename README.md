# Это инструкция для запуска тестового задания

## Локальное развёртывание проекта
Клонируйте репозиторий проекта и перейдите в него с помощью командной строки
```
git clon https://github.com/BobrPavel/test_task_Polza_Agency.git
```

Создайте виртуальное окружение Pyton и активируйте его
```
python3 -m venv venv  
```
```
venv\Scripts\activate  
```
Установите зависимости

```
pip install -r requirements.txt  
```
Пожалуйста проверьте как выглядит директория проекта, должно быть вот так:
```
test_task_Polza_Agency/
├── Checking email domains 1/
│   └── ... (файлы 1 задания)
├── Telegram_interhation_2/
│   └── ... (файлы 2 задания)
├── Architecture_3.pdf
├── .gitignore
└── req.txt

venv/
└── ... (файлы виртуального окружения)
 
```

 ### Задание 1
 Для проверки запустите файл main.py. В файлы mails.txt вы можете записать email адресса для проверки на наличие MX записей домена

### Задание 2
Для проверки, запустите файл boy.py. Перейдите в бот по ссылке: [https://t.me/shlapnikov_polza_agancy_bot](https://t.me/shlapnikov_polza_agancy_bot). Выполните команду start и вам будет отправленно сообщение из файла text.txt

