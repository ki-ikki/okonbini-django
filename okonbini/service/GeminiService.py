import google.generativeai as gemini
import re
from okonbini.models.ItemCategory import ItemCategory
from icecream import ic
from config.settings.local import GEMINI_API_KEY

# KEY = 'AIzaSyAgNqDBv1rwLxWc7pFZHWUbtqIRTW3kFGQ'

def getItemCategoryFromItemName(itemName, itemInfo=None):
    """
    照明と商品情報から Gemini 使用して商品カテゴリを推測し、
    ItemCategory インスタンスを返す

    Args:
        itemName (str): 商品名
        itemInfo (str): 商品情報

    Returns:
        ItemCategory: アイテムカテゴリ
    """
    gemini.configure(api_key = GEMINI_API_KEY)
    modelGemini = gemini.GenerativeModel('gemini-1.5-flash')

    itemCategoryList = list(ItemCategory.getItemCategoryNameList())

    # 商品名からカテゴリを推測する
    prompt = f"商品名「{itemName}」、商品情報「{itemInfo}」にはどのカテゴリが適していますか？以下のカテゴリと一致するワードが入っていれば、それを選択し、それ以外の場合は推測して1つ選択して、カテゴリ名だけ返してください: {', '.join(itemCategoryList)}。該当するカテゴリがない場合はotherを返してください"

    try:
        getCategoryNameFromGemini = modelGemini.generate_content(prompt)
    except Exception as e:
        print(f'Gemini で商品カテゴリを取得できなかったため、 other で登録し、後続処理を実行します: {e}')
        return ItemCategory.getItemCategoryFromName(ItemCategory.CATEGORY_OTHER)
    print(getCategoryNameFromGemini.text)

    # 取得した結果のカテゴリ名の後ろに空白が入るため、正規表現で削除し、ItemCategory インスタンスを返す
    return ItemCategory.getItemCategoryFromName(re.sub(r'\s', '', getCategoryNameFromGemini.text))