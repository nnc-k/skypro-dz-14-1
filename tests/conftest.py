import pytest

from src.main import Category, Product


@pytest.fixture(autouse=True)
def reset_counters() -> None:
    """Сбрасывает счётчики классов перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_product() -> Product:
    return Product("Test Product", "Test Description", 100.0, 5)


@pytest.fixture
def sample_category(sample_product: Product) -> Category:
    return Category("Test Category", "Test Description", [sample_product])