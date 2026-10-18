# Домашнее задание 16.1

Учебный проект по Python: описание товаров и категорий товаров с подсчётом статистики, загрузкой данных из JSON, магическими методами и наследованием.

## Функционал проекта

### Классы

- **Product** — базовый класс для описания товара:
  - name — название товара;
  - description — описание;
  - price — цена (приватный атрибут);
  - quantity — количество в наличии.

- **Smartphone** (наследник Product) — смартфон. Дополнительные атрибуты:
  - efficiency — производительность;
  - model — модель;
  - memory — объём встроенной памяти;
  - color — цвет.

- **LawnGrass** (наследник Product) — газонная трава. Дополнительные атрибуты:
  - country — страна-производитель;
  - germination_period — срок прорастания;
  - color — цвет.

- **Category** — категория товаров:
  - name — название;
  - description — описание;
  - products — приватный список объектов Product.

### Атрибуты класса Category

- **category_count** — общее количество созданных категорий;
- **product_count** — общее количество товаров во всех категориях.

### Методы

- **Category.add_product(product)** — добавляет товар с проверкой типа (isinstance). При попытке добавить не Product выбрасывается TypeError.
- **Product.new_product(dict)** — classmethod, создаёт объект Product из словаря.

### Геттеры и сеттеры

- **Product.price** — геттер и сеттер с проверкой: при значении ≤ 0 выводится сообщение «Цена не должна быть нулевая или отрицательная», цена не меняется.
- **Category.products** — геттер приватного списка товаров, возвращает строку.

### Магические методы

- **Product.__str__** — «Название, X руб. Остаток: X шт.».
- **Product.__add__** — сложение двух товаров с проверкой type(): можно складывать только объекты одного класса, иначе TypeError.
- **Category.__str__** — «Название, количество продуктов: X шт.».

### Дополнительный функционал

- **load_categories_from_json(file_path)** — загрузка категорий и товаров из JSON-файла.

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

Покрытие функционального кода тестами — 99 %.

Проверяется:

- корректность инициализации Product, Smartphone, LawnGrass, Category;
- геттеры и сеттеры Product.price;
- classmethod Product.new_product;
- Category.add_product с проверкой типа;
- магические методы __str__ и __add__;
- ограничения сложения разных типов (TypeError);
- ограничения добавления не-Product (TypeError);
- загрузка из JSON.

## Автор

nnc-k (katkova.a1997@gmail.com)