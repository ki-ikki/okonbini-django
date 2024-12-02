from okonbini.models.Store import Store
from okonbini.models.ItemCategory import ItemCategory
from okonbini.models.ItemImage import ItemImage
from okonbini.models.Item import Item
from django.utils.timezone import now

def create_test_store():
    """
    テスト用の店舗情報を作成
    """
    return Store.objects.create(
        store_name = "Test Store",
        color_code = "#FFFFFF",
        is_active = True,
        updated_at = now(),
        )

def create_test_category():
    """
    テスト用のカテゴリ情報を作成
    """
    return ItemCategory.objects.create(
        category_name = "Test Category",
        is_active = True,
        created_at = now(),
        updated_at = now(),
        )

def create_test_item_image():
    """
    テスト用のアイテム画像情報を作成
    """
    return ItemImage.objects.create(
        item_image_url = "https://example",
        created_at = now(),
        updated_at = now(),
    )

def create_test_item():
    """
    テスト用のアイテム情報を作成
    """
    store = create_test_store()
    category = create_test_category()
    itemImage = create_test_item_image()

    return Item.objects.create(
        store = store,
        item_category = category,
        item_image = itemImage,
        item_name = "Test Item",
        item_info = "Test Item Info",
        price = 400,
        release_date = now(),
        is_active = True
    )