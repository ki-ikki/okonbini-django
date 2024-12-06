import icecream as ic
import requests, os, time
from datetime import datetime
from okonbini.models.ItemImage import ItemImage
from okonbini.models.Store import Store
from okonbini.models.Item import Item
import re

def downLoadImageFromUrl(
    itemImgUrl,
    ):
    """
    画像URLから画像をダウンロードして保存する

    Args:
        itemImgUrl (str): 画像URL

    Returns:
        itemImage (ItemImage) : 商品画像オブジェクト
    """

    saveDir = "./images"  # 任意の保存先ディレクトリを指定

    os.makedirs(saveDir, exist_ok=True)

    itemImgFileName = os.path.basename(itemImgUrl)  # ファイル名を取得
    itemSavePath = os.path.join(saveDir, itemImgFileName) # 保存先のファイルパスを作成

    try:
        # 画像を取得して保存
        getItemImage = requests.get(itemImgUrl, stream=True)
        getItemImage.raise_for_status()  # HTTPエラーをチェック
        with open(itemSavePath, "wb") as pi:
            for chunk in getItemImage.iter_content(1024):  # 1KBずつ書き込み
                pi.write(chunk)
        print("保存しました:", itemSavePath)
    except requests.exceptions.RequestException as e:
        print("画像のダウンロード中にエラーが発生しました:", e)

    # 処理を休止
    time.sleep(1)

    itemImage = ItemImage.createItemImage(itemSavePath)

    return itemImage

def releaseDateToDateTime(
    storeName,
    releaseDateText
    ):
    """
    日付の文字列を日付オブジェクトに変換する

    Args:
        storeName (str): コンビニ名
        releaseDateText (str): 日付の文字列

    Return:
        releaseDate (datetime.date): 日付オブジェクト
    """

    # 店舗ごとに正規表現で日付を取得する
    match storeName:
        case Store.SEVEN_ELEVEN:
            releaseDateMatch = re.search(r'(\d{4})年(\d{2})月(\d{2})日', releaseDateText)
        case Store.LAWSON:
            releaseDate = None
            print("ローソンの商品情報は未実装です。")
        case Store.FAMILY_MART:
            releaseDate = None
            print("ファミリーマートの商品情報は未実装です。")

    # パターンマッチした場合、 releaseDate に日付を保存する
    if releaseDateMatch is not None:
            # 年、月、日を取得
            year, month, day = map(int, releaseDateMatch.groups())

            # 日付オブジェクトに変換
            releaseDate = datetime(year, month, day).date()
    else:
        # 失敗した場合、Noneで保存する。後続処理を実行するため
        print("日付の抽出に失敗しました。")
        itemReleaseDate = None

    return releaseDate

def calculateExclusivePriceFromTaxPrice(
    storeName,
    itemPriceText
    ):
    """
    税込価格から税抜価格を計算する

    Args:
        itemPriceText (string): 税込価格の文字列

    Returns:
        itemPrice (int): 税抜価格
    """

    # 店舗ごとに正規表現で税込価格を取得する
    match storeName:
        case Store.SEVEN_ELEVEN:
            taxMatch = re.search(r'税込(\d+(\.\d+)?)', itemPriceText)
        case Store.LAWSON:
            itemPrice = None
            print("ローソンの商品情報は未実装です。")
        case Store.FAMILY_MART:
            itemPrice = None
            print("ファミリーマートの商品情報は未実装です。")

    taxPrice = float(taxMatch.group(1))
    itemPrice = int(taxPrice * (1 + Item.TAX_RATE))

    return itemPrice