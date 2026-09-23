import json

from src.main import Category, Product, load_categories_from_json


def test_product_init() -> None:
    """Проверка корректности инициализации Product."""
    product = Product("iPhone", "Смартфон", 99999.99, 5)

    assert product.name == "iPhone"
    assert product.description == "Смартфон"
    assert product.price == 99999.99
    assert product.quantity == 5


def test_category_init(sample_product: Product) -> None:
    """Проверка корректности инициализации Category."""
    category = Category("Смартфоны", "Мобильные устройства", [sample_product])

    assert category.name == "Смартфоны"
    assert category.description == "Мобильные устройства"
    assert len(category.products) == 1
    assert category.products[0] is sample_product
    assert isinstance(category.products[0], Product)


def test_category_count() -> None:
    """Проверка подсчёта категорий."""
    assert Category.category_count == 0

    Category("A", "desc", [])
    assert Category.category_count == 1

    Category("B", "desc", [])
    assert Category.category_count == 2


def test_product_count() -> None:
    """Проверка подсчёта товаров."""
    assert Category.product_count == 0

    p1 = Product("P1", "d", 10.0, 1)
    p2 = Product("P2", "d", 20.0, 2)

    Category("A", "desc", [p1, p2])
    assert Category.product_count == 2

    Category("B", "desc", [p1])
    assert Category.product_count == 3


def test_product_count_in_empty_category() -> None:
    """Пустая категория не увеличивает счётчик товаров."""
    Category("Empty", "desc", [])
    assert Category.product_count == 0
    assert Category.category_count == 1


def test_load_categories_from_json(tmp_path) -> None:
    """Проверка загрузки категорий и товаров из временного JSON."""
    data = [
        {
            "name": "Кат",
            "description": "Описание",
            "products": [
                {
                    "name": "Товар",
                    "description": "Описание товара",
                    "price": 10.5,
                    "quantity": 3,
                }
            ],
        }
    ]
    json_file = tmp_path / "data.json"
    json_file.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    categories = load_categories_from_json(str(json_file))

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Кат"
    assert len(categories[0].products) == 1
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].products[0].price == 10.5


def test_load_from_real_file() -> None:
    """Проверка загрузки из реального data/products.json."""
    categories = load_categories_from_json("data/products.json")

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 3
    assert categories[1].name == "Телевизоры"
    assert len(categories[1].products) == 1
