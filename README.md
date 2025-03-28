<h1 align="center">Тестовое задание</h1>

<h3 align="center">Для компании IT-Solutions</h3>

<br>

<h2 align="center">Запуск приложения</h2>

### Клонируем репозиторий

```bash
git clone https://github.com/Sh0ma28/ta-backend-solutions.git
```

Переход в проект

```bash
cd ta-backend-solutions
```

### Создаем виртуальное окружение

Документация: [https://docs.python.org/3/library/venv.html]

```bash
python -m venv venv
```

Запуск (Linux):

```bash
source venv/bin/activate
```

Запуск (Windows):

```bash
venv\Scripts\activate.bat
```

### Устанавливаем зависимости

```bash
pip install -r requirements.txt
```

### Применяем миграции

```bash
python manage.py migrate
```

### Создаем админ-аккаунт

```bash
python manage.py createsuperuser
```

Требуется вписать необходимые поля по запросу консоли

### Запуск приложения

```bash
python manage.py runserver
```

Работа происходит в админ панели по адресу: [http://127.0.0.1:8000/admin/]

<h2 align="center">Возникшие вопросы и проблемы</h2>

В описании задания указано, что запись о ДДС должна содержать тип, категорию и подкатегорию, между которыми существуют отношения "Тип<-Категория<-Подкатегория"

Если в модель записи о ДДС вставить тип, категорию и подкатегорию, то это нарушит нормальную форму. Поэтому я оставил только подкатегорию, из которой можно узнать о категории (из которой можно узнать о типе).