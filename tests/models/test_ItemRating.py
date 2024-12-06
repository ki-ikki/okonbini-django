from django.test import TestCase
from okonbini.models.ItemRating import ItemRating
from tests.models.factories import createTestItem, createTestStore

class CreateItemRatingTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_item_rating_success(self):
        """正常系: 商品評価情報が正常に作成される"""
        item = createTestItem()
        store = createTestStore()
        favoriteWeeklyCount = 10
        favoriteMonthlyCount = 20
        favoriteTotalCount = 30
        reviewWeeklyCount = 40
        reviewMonthlyCount = 50
        reviewTotalCount = 60

        itemRating = ItemRating.createTestItemRating(
            item,
            store,
            favoriteWeeklyCount,
            favoriteMonthlyCount,
            favoriteTotalCount,
            reviewWeeklyCount,
            reviewMonthlyCount,
            reviewTotalCount
        )

        self.assertIsNotNone(itemRating.id)
        self.assertEqual(itemRating.item, item)
        self.assertEqual(itemRating.store, store)
        self.assertEqual(itemRating.favorite_weekly_count, favoriteWeeklyCount)
        self.assertEqual(itemRating.favorite_monthly_count, favoriteMonthlyCount)
        self.assertEqual(itemRating.favorite_total_count, favoriteTotalCount)
        self.assertEqual(itemRating.review_weekly_count, reviewWeeklyCount)
        self.assertEqual(itemRating.review_monthly_count, reviewMonthlyCount)
        self.assertEqual(itemRating.review_total_count, reviewTotalCount)