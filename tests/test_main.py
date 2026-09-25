import json

from src.main import Category, Product, load_categories_from_json


# ---------- Product: init ----------

def test_product_init() -> None:
    product = Product("iPhone", "Смартфон", 99999.99, 5)

    assert product.name == "iPhone"
    assert product.description == "Смартфон"
    assert product.price == 99999.99
    assert product.quantity == 5


# ---------- Product: price getter / setter ----------

def test_product_price_getter(sample_product: Product) -> None:
    assert sample_product.price == 100.0


def test_product_price_setter_valid(sample_product: Product) -> None:
    sample_product.price = 250.0
    assert sample_product.price == 250.0


def test_product_price_setter_zero(sample_product: Product, capsys) -> None:
    sample_product.price = 0
    assert sample_product.price == 100.0

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_price_setter_negative(sample_product: Product, capsys) -> None:
    sample_product.price = -10.0
    assert sample_product.price == 100.0

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


# ---------- Product: classmethod new_product ----------

def test_new_product() -> None:
    data = {"name": "Test", "description": "Desc", "price": 50.0, "quantity": 3}
    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Test"
    assert product.description == "Desc"
    assert product.price == 50.0
    assert product.quantity == 3


# ---------- Product: __str__ ----------

def test_product_str() -> None:
    product = Product("iPhone", "Смартфон", 99999.99, 5)
    assert str(product) == "iPhone, 99999.99 руб. Остаток: 5 шт."


# ---------- Product: __add__ ----------

def test_product_add() -> None:
    a = Product("A", "d", 100.0, 10)
    b = Product("B", "d", 200.0, 2)

    assert a + b == 1400.0


def test_product_add_three_variants() -> None:
    p1 = Product("P1", "d", 180000.0, 5)
    p2 = Product("P2", "d", 210000.0, 8)
    p3 = Product("P3", "d", 31000.0, 14)

    assert p1 + p2 == 2580000.0
    assert p1 + p3 == 1334000.0
    assert p2 + p3 == 2114000.0


# ---------- Category: init / getter ----------

def test_category_init(sample_product: Product) -> None:
    category = Category("Смартфоны", "Мобильные устройства", [sample_product])

    assert category.name == "Смартфоны"
    assert category.description == "Мобильные устройства"
    assert category.products == "Test Product, 100.0 руб. Остаток: 5 шт.\n"


def test_products_getter_multiple() -> None:
    p1 = Product("A", "d", 100.0, 1)
    p2 = Product("B", "d", 200.0, 2)
    category = Category("Cat", "Desc", [p1, p2])

    expected = "A, 100.0 руб. Остаток: 1 шт.\nB, 200.0 руб. Остаток: 2 шт.\n"
    assert category.products == expected


def test_products_getter_empty() -> None:
    category = Category("Empty", "Desc", [])
    assert category.products == ""


# ---------- Category: __str__ ----------

def test_category_str() -> None:
    p1 = Product("A", "d", 100.0, 10)
    p2 = Product("B", "d", 200.0, 2)
    category = Category("Кат", "Описание", [p1, p2])

    assert str(category) == "Кат, количество продуктов: 12 шт."


def test_category_str_empty() -> None:
    category = Category("Пусто", "Описание", [])
    assert str(category) == "Пусто, количество продуктов: 0 шт."


# ---------- Category: add_product ----------

def test_add_product(sample_category: Category) -> None:
    new_product = Product("New", "Desc", 200.0, 3)
    sample_category.add_product(new_product)

    assert "New" in sample_category.products
    assert "200.0 руб." in sample_category.products


def test_add_product_increments_counter(sample_category: Category) -> None:
    assert Category.product_count == 1

    sample_category.add_product(Product("New", "Desc", 200.0, 3))
    assert Category.product_count == 2


# ---------- Class counters ----------

def test_category_count() -> None:
    assert Category.category_count == 0

    Category("A", "desc", [])
    assert Category.category_count == 1

    Category("B", "desc", [])
    assert Category.category_count == 2


def test_product_count() -> None:
    assert Category.product_count == 0

    p1 = Product("P1", "d", 10.0, 1)
    p2 = Product("P2", "d", 20.0, 2)

    Category("A", "desc", [p1, p2])
    assert Category.product_count == 2

    Category("B", "desc", [p1])
    assert Category.product_count == 3


def test_product_count_in_empty_category() -> None:
    Category("Empty", "desc", [])
    assert Category.product_count == 0
    assert Category.category_count == 1


# ---------- JSON loading ----------

def test_load_categories_from_json(tmp_path) -> None:
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
    assert "Товар" in categories[0].products
    assert "10.5 руб." in categories[0].products


def test_load_from_real_file() -> None:
    categories = load_categories_from_json("data/products.json")

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert "Samsung Galaxy C23 Ultra" in categories[0].products
    assert categories[1].name == "Телевизоры"
    assert "QLED 4K" in categories[1].products