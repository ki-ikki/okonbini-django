from django.db import models
from django.utils.timezone import now
from okonbini.models.Store import Store

class ItemCategory(models.Model):
    CATEGORY_ONIGIRI = 'onigiri' # おにぎり
    CATEGORY_SUSHI = 'sushi' # 寿司
    CATEGORY_BENTO = 'bento' # 弁当
    CATEGORY_SANDWICH = 'sandwich' # サンドイッチ
    CATEGORY_BREAD = 'bread' # パン
    CATEGORY_SOBA = 'soba' # そば
    CATEGORY_UDON = 'udon' # うどん
    CATEGORY_NOODLE = 'noodle' # 中華麺
    CATEGORY_PASTA = 'pasta' # パスタ
    CATEGORY_GRATIN = 'gratin' # グラタン
    CATEGORY_DORIAN = 'dorian' # ドリア
    CATEGORY_DAILY_DISH = 'daily_dish' # 惣菜
    CATEGORY_SALAD = 'salad' # サラダ
    CATEGORY_SWEETS = 'sweets' # スイーツ
    CATEGORY_ICE_CREAM = 'ice_cream' # アイスクリーム
    CATEGORY_HOT_SNACK = 'hot_snack' # 揚げ物・惣菜
    CATEGORY_ODEN = 'oden' # おでん
    CATEGORY_CHUKAMAN = 'chukaman' # 中華まん
    CATEGORY_FROZEN = 'frozen' # 冷凍食品
    CATEGORY_CAFE = 'cafe' # カフェ
    CATEGORY_BAKED_SWEETS = 'baked_sweets' # 焼き菓子
    CATEGORY_PROCESSED_FOOD = 'processed_food' # 加工食品
    CATEGORY_BEVERAGE = 'beverage' # 飲料
    CATEGORY_ALCOHOL = 'alcohol' # 酒類
    CATEGORY_OTHER = 'other' # その他

    category_name = models.CharField(unique=True, max_length=255, null=False)
    is_active = models.BooleanField(null=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'item_categories'

    def __str__(self):
        return self.category_name

    def createItemCategory(itemCategoryName):
        itemCategory = ItemCategory.objects.create(
            category_name=itemCategoryName,
            is_active=True,
            created_at=now(),
            updated_at=now(),
        )
        return itemCategory

    def getItemCategoryFromName(itemCategoryName):
        """
        アイテムカテゴリ名からアイテムカテゴリを取得する

        Args:
            itemCategoryName (str): アイテムカテゴリ名

        Returns:
            ItemCategory: アイテムカテゴリ
        """

        return ItemCategory.objects.get(category_name=itemCategoryName)

    def getItemCategoryNameList():
        return ItemCategory.objects.values_list('category_name', flat=True)
