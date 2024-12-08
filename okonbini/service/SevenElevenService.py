import requests, re
from okonbini.models.Store import Store
from okonbini.models.ItemCategory import ItemCategory
from okonbini.models.Item import Item
import okonbini.service.ScrapingService as ScrapingService
import okonbini.service.GeminiService as GeminiService
from bs4 import BeautifulSoup
from icecream import ic

BASE_URL = 'https://www.sej.co.jp/'

def scrapingSevenElevenExistingProducts():
    """
    セブンイレブンの既存商品をスクレイピングする一連の処理
    基本はアプリリリースの前に一度行うのみ
    """

    store = Store.getStoreFromName(Store.SEVEN_ELEVEN)

    itemCategoryUrlIdMapping = {
        'cat/010010010000000' : ItemCategory.CATEGORY_ONIGIRI, # 手巻おにぎり
        'cat/010010020000000' : ItemCategory.CATEGORY_ONIGIRI, # 直巻おにぎり
        'cat/010010030000000' : ItemCategory.CATEGORY_ONIGIRI, # その他のおむすび
        'cat/010030010000000' : ItemCategory.CATEGORY_SUSHI, # 手巻き寿司
        'cat/010030020000000' : ItemCategory.CATEGORY_SUSHI, # いなり寿司
        'cat/010030030000000' : ItemCategory.CATEGORY_SUSHI, # その他のお寿司
        'cat/010020010000000' : ItemCategory.CATEGORY_BENTO, # お弁当
        'cat/010020020000000' : ItemCategory.CATEGORY_BENTO, # チルド弁当
        'sandwich' : ItemCategory.CATEGORY_SANDWICH, # サンドイッチ
        'cat/050010010000000' : ItemCategory.CATEGORY_BREAD, # 食パン
        'cat/050010020000000' : ItemCategory.CATEGORY_BREAD, # 食事パン
        'cat/050020010000000' : ItemCategory.CATEGORY_BREAD, # 菓子パン
        'cat/050020020000000' : ItemCategory.CATEGORY_BREAD, # 惣菜パン
        'donut' : ItemCategory.CATEGORY_SWEETS, # ドーナッツ
        'cat/030010010000000' : ItemCategory.CATEGORY_SOBA, # そば
        'cat/030010020000000' : ItemCategory.CATEGORY_UDON, # うどん
        'cat/030010030000000' : ItemCategory.CATEGORY_NOODLE, # 中華麺
        'cat/030010040000000' : ItemCategory.CATEGORY_SOBA, # 焼きそば・焼うどんほか
        'pasta' : ItemCategory.CATEGORY_PASTA, # スパゲティ・パスタ
        'gratin' : ItemCategory.CATEGORY_GRATIN, # グラタン・ドリア
        'dailydish' : ItemCategory.CATEGORY_DAILY_DISH, # 惣菜
        'cat/040020010000000' : ItemCategory.CATEGORY_SALAD, # サラダ
        'cat/040020020000000' : ItemCategory.CATEGORY_SALAD, # パスタサラダ・おかずサラダほか
        'cat/040020030000000' : ItemCategory.CATEGORY_SALAD, # ７プレミアム（副菜）
        'cat/080080030000000' : ItemCategory.CATEGORY_SALAD, # カット野菜・カットフルーツ
        'cat/060010010000000' : ItemCategory.CATEGORY_SWEETS, # 洋菓子
        'cat/060010020000000' : ItemCategory.CATEGORY_SWEETS, # 和菓子
        'cat/060020010000000' : ItemCategory.CATEGORY_ICE_CREAM, # アイスクリーム
        'cat/060020020000000' : ItemCategory.CATEGORY_ICE_CREAM, # ファミリータイプ
        'cat/090030010000000' : ItemCategory.CATEGORY_HOT_SNACK, # 揚げ物・惣菜
        'cat/090030020000000' : ItemCategory.CATEGORY_OTHER, # その他の商品
        'oden' : ItemCategory.CATEGORY_ODEN, # おでん
        'chukaman' : ItemCategory.CATEGORY_CHUKAMAN, # 中華まん
        'cat/150010000000000' : ItemCategory.CATEGORY_FROZEN, # 冷凍食品
        'cat/150020000000000' : ItemCategory.CATEGORY_FROZEN, # 冷凍食材
        'cat/150030000000000' : ItemCategory.CATEGORY_FROZEN, # ロックアイス
        'sevencafe' : ItemCategory.CATEGORY_CAFE, # セブンカフェ
    }

    # 商品一覧のページ数。わざわざ取得する必要ないので、適当な数値を設定
    itemCategoryUrlListIds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    for itemCategoryUrlId in itemCategoryUrlIdMapping:
        # 商品ページのURLから商品カテゴリを取得
        itemCategory = ItemCategory.getItemCategoryFromName(itemCategoryUrlIdMapping.get(itemCategoryUrlId))

        for itemCategoryUrlListId in itemCategoryUrlListIds:
            # 商品一覧を取得
            requestGetItemUrlLists = requests.get(BASE_URL + 'products/a/' + itemCategoryUrlId + '/' + str(itemCategoryUrlListId) + '/l15/')

            # 商品一覧が取得できなかった場合、処理をスキップする
            itemUrlLists = []
            if requestGetItemUrlLists.status_code != 200:
                print('商品一覧が取得できませんでした')
                break

            # 商品一覧から商品情報を取得
            itemTextData = BeautifulSoup(requestGetItemUrlLists.text, 'html.parser').find_all(class_='list_inner')

            if itemTextData is not None:
            # 商品詳細ページのテキストデータから商品情報を保存する
                try:
                    scrapingItemDetailDataFromHtml(itemTextData, store, False, itemCategory)
                except Exception as e:
                    print(f'商品詳細ページのテキストデータから商品情報を保存する際にエラーが発生しました : {e}')
                    continue
            else:
                print(f'商品一覧が取得できませんでした。itemCategoryUrlId : {itemCategoryUrlId}, itemCategoryUrlListId : {itemCategoryUrlListId}')
                continue

def scrapingSevenElevenNewProducts():
    """
        セブンイレブンの新商品をスクレイピングする一連の処理
        稼働後は cron 等で定期実行される
    """

    areaListIds = [
        'hokkaido',
        # 'tohoku',
        # 'kanto',
        # 'koshinetsu',
        # 'hokuriku',
        # 'tokai',
        # 'kinki',
        # 'chugoku',
        # 'shikoku',
        # 'kyushu',
        # 'okinawa'
    ]

    store = Store.getStoreFromName(Store.SEVEN_ELEVEN)

    # 商品一覧のページ数。わざわざ取得する必要ないので、適当な数値を設定
    itemCategoryUrlListIds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    for areaListId in areaListIds:
        for itemCategoryUrlListId in itemCategoryUrlListIds:
            # 商品一覧を取得
            requestGetItemUrlLists = requests.get(BASE_URL + 'products/a/thisweek/area/' + areaListId + '/' + str(itemCategoryUrlListId) + '/l15')

            # 商品一覧が取得できなかった場合、処理をスキップする
            if requestGetItemUrlLists.status_code != 200:
                print('商品一覧が取得できませんでした')
                break

            # 商品一覧から商品情報を取得
            itemTextData = BeautifulSoup(requestGetItemUrlLists.text, 'html.parser').find_all(class_='list_inner')

            # 商品詳細ページのテキストデータから商品情報を保存する
            if itemTextData is not None:
                try:
                    scrapingItemDetailDataFromHtml(itemTextData, store)
                except Exception as e:
                    print(f'商品詳細ページのテキストデータから商品情報を保存する際にエラーが発生しました : {e}')
                    continue
            else:
                print(f'商品一覧が取得できませんでした。areaId : {areaListId}, itemCategoryUrlListId : {itemCategoryUrlListId}')
                continue

def scrapingItemDetailDataFromHtml(parserItemTextData, store, isNewProduct=True, itemCategory=None):
    # 商品情報から商品詳細ページを取得する
    itemUrlLists = []
    for itemText in parserItemTextData:
        itemUrl = itemText.find('a', href=True)
        itemUrlLists.append(itemUrl['href'])

    # 商品URLから商品詳細を取得し、保存する
    for itemUrl in itemUrlLists:
        requestGetItemDetailData = requests.get(BASE_URL + itemUrl)

        if requestGetItemDetailData.status_code == 200:
            parserItemTextData = BeautifulSoup(requestGetItemDetailData.text, 'html.parser')

            # 商品名を取得する
            if parserItemTextData.find(class_='item_ttl') is not None:
                itemName = re.sub(r'\s', '', parserItemTextData.find(class_ = 'item_ttl').text)
            else:
                print('商品名が存在しないため、処理をスキップします')
                continue

            # 既に同一の商品が登録されているかを判定
            if Item.isItemExist(itemName):
                print('既に商品が存在するため、処理をスキップします')
                continue

            # 商品情報を取得する
            if parserItemTextData.find(class_ = 'item_text') is not None:
                itemInfo = parserItemTextData.find(class_ = 'item_text').text
            else:
                itemInfo = None
                print('商品情報が存在しません。null許容なので None として後続の処理を実行します')

            # 新商品の場合、商品名/商品情報からカテゴリから Gemini を使用して取得する
            if isNewProduct:
                itemCategory = GeminiService.getItemCategoryFromItemName(itemName, itemInfo)

            # 商品発売日が存在する場合、正規表現で置換して日付を取得する
            if parserItemTextData.find(class_='item_launch') is not None:
                releaseDateText = parserItemTextData.find(class_ = 'item_launch').text
                itemReleaseDate = ScrapingService.releaseDateToDateTime(Store.SEVEN_ELEVEN, releaseDateText)
            else:
                itemReleaseDate = None

            # 商品価格(税込)を正規表現で置換し、税率から税抜金額を計算する
            itemPriceText = parserItemTextData.find(class_ = 'item_price').text
            itemPrice = ScrapingService.calculateExclusivePriceFromTaxPrice(Store.SEVEN_ELEVEN, itemPriceText)

            # 複数画像の場合、クラス名が異なる。
            # 単一画像が取得できなかった場合、複数画像で画像URLを取得する
            # 画像が取得できない場合、処理をスキップする
            itemImageUrl = None
            for itemImageClass in ['productWrap', 'slideWrap']:
                itemImageParserText = parserItemTextData.find(class_=itemImageClass)
                if itemImageParserText and itemImageParserText.find('img'):
                    itemImageUrl = itemImageParserText.find('img')['src']
                    break

            if not itemImageUrl:
                print('画像が取得できませんでした'  + itemName)
                continue

            # 画像URLからダウンロード
            itemImage = ScrapingService.downLoadImageFromUrl(itemImageUrl)

            # 商品情報を保存する
            item = Item.createItem(
                store,
                itemCategory,
                itemImage,
                itemName,
                itemInfo,
                itemPrice,
                itemReleaseDate,
                True
            )

            print('商品情報を保存しました')
            ic(
                item.store.store_name,
                item.item_category.category_name,
                item.item_image.item_image_url,
                item.item_name,
                item.item_info,
                item.price,
                item.release_date,
                item.is_active
            )