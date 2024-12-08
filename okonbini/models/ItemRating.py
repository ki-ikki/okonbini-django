from django.db import models
from django.utils.timezone import now

class ItemRating(models.Model):
    item = models.ForeignKey(
        'Item',
        on_delete=models.DO_NOTHING,
        null=False
    )
    store = models.ForeignKey(
        'Store',
        on_delete=models.DO_NOTHING,
        null=False
    )
    favorite_weekly_count = models.IntegerField(null=False)
    favorite_monthly_count = models.IntegerField(null=False)
    favorite_total_count = models.IntegerField(null=False)
    review_weekly_count = models.IntegerField(null=False)
    review_monthly_count = models.IntegerField(null=False)
    review_total_count = models.IntegerField(null=False)
    sort_date = models.DateField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # managed = False
        db_table = 'item_ratings'

    def __str__(self):
        return f'{self.item} / {self.store}'

    def createItemRating(
        item,
        store,
        favoriteWeeklyCount,
        favoriteMonthlyCount,
        favoriteTotalCount,
        reviewWeeklyCount,
        reviewMonthlyCount,
        reviewTotalCount
    ):
        """
        商品評価情報を作成
        """
        itemRating = ItemRating.objects.create(
            item = item,
            store = store,
            favorite_weekly_count = favoriteWeeklyCount,
            favorite_monthly_count = favoriteMonthlyCount,
            favorite_total_count = favoriteTotalCount,
            review_weekly_count = reviewWeeklyCount,
            review_monthly_count = reviewMonthlyCount,
            review_total_count = reviewTotalCount,
            created_at = now()
            )

        return itemRating