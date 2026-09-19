# Домашнее задание 14.1

Учебный проект по Python: описание товаров и категорий товаров с подсчётом статистики и загрузкой данных из JSON.

## Функционал проекта

### Классы

- **Product** — описывает товар:
  - name — название товара;
  - description — описание;
  - price — цена (с копейками);
  - quantity — количество в наличии (в штуках).

- **Category** — описывает категорию товаров:
  - name — название категории;
  - description — описание;
  - products — список объектов класса Product.

### Атрибуты класса Category

- **category_count** — общее количество созданных категорий;
- **product_count** — общее количество товаров во всех категориях.

Оба атрибута заполняются автоматически при инициализации нового объекта Category.

### Дополнительный функционал

- **load_categories_from_json(file_path)** — функция, которая читает JSON-файл и создаёт на его основе объекты классов Category и Product. Возвращает список категорий.

## Структура проекта

dz_14_1/
├── data/
│   └── products.json
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_main.py
├── .flake8
├── pyproject.toml
├── poetry.lock
└── README.md

## Технологии

- Python 3.14
- Poetry — управление зависимостями
- pytest, pytest-cov — тестирование и покрытие
- flake8 — линтер (PEP 8)
- black, isort — форматирование кода
- mypy — проверка типов

## Установка и запуск

### Установка зависимостей

poetry install --no-root

### Запуск тестов с покрытием

poetry run pytest

Отчёт о покрытии в HTML создаётся в папке htmlcov/. Открыть отчёт: htmlcov/index.html.

### Проверка кода линтерами

poetry run flake8 src tests
poetry run black --check src tests
poetry run isort --check-only src tests
poetry run mypy src

## Тесты

Покрытие функционального кода тестами — 96 %.

Проверяется:

- корректность инициализации объектов класса Product;
- корректность инициализации объектов класса Category;
- автоматический подсчёт количества товаров (product_count);
- автоматический подсчёт количества категорий (category_count);
- загрузка категорий и товаров из JSON-файла.

## Автор

nnc-k (katkova.a1997@gmail.com)