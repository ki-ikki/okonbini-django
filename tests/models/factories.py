from okonbini.models.Store import Store
from okonbini.models.ItemCategory import ItemCategory
from okonbini.models.ItemImage import ItemImage
from okonbini.models.Item import Item
from django.utils.timezone import now

def createTestStore():
    """
    テスト用の店舗情報を作成
    """
    storeList = [
        Store.SEVEN_ELEVEN,
        Store.LAWSON,
        Store.FAMILY_MART
    ]

    for store in storeList:
        return Store.objects.create(
            store_name = store,
            color_code = "#FFFFFF",
            is_active = True,
            updated_at = now()
        )

def createTestCategory():
    """
    テスト用のカテゴリ情報を作成
    """
    return ItemCategory.objects.create(
        category_name = "Test Category",
        is_active = True,
        created_at = now(),
        updated_at = now(),
        )

def createTestItemImage():
    """
    テスト用のアイテム画像情報を作成
    """
    return ItemImage.objects.create(
        item_image_url = "https://example",
        created_at = now(),
        updated_at = now(),
    )

def createTestItem():
    """
    テスト用のアイテム情報を作成
    """
    store = createTestStore()
    category = createTestCategory()
    itemImage = createTestItemImage()

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

def createTestItemCategoryList():
    itemCategories = [
        'onigiri',
        'sushi',
        'bento',
        'sandwich',
        'bread',
        'soba',
        'udon',
        'noodle',
        'pasta',
        'gratin',
        'dorian',
        'daily_dish',
        'salad',
        'sweets',
        'ice_cream',
        'hot_snack',
        'oden',
        'chukaman',
        'frozen',
        'cafe',
        'baked_sweets',
        'processed_food',
        'beverage',
        'alcohol',
        'other'
    ]
    for itemCategory in itemCategories:
        ItemCategory.objects.create(
            category_name = itemCategory,
            is_active = True,
            created_at = now(),
            updated_at = now(),
        )