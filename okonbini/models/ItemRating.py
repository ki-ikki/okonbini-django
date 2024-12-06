from django.db import models
from django.utils.timezone import now

class ItemRating(models.Model):
    item = models.ForeignKey(
        'Item',
        on_delete=models.DO_NOTHING,
    )
    store = models.ForeignKey(
        'Store',
        on_delete=models.DO_NOTHING,
    )
    favorite_weekly_count = models.IntegerField(blank=True, null=True)
    favorite_monthly_count = models.IntegerField(blank=True, null=True)
    favorite_total_count = models.IntegerField(blank=True, null=True)
    review_weekly_count = models.IntegerField(blank=True, null=True)
    review_monthly_count = models.IntegerField(blank=True, null=True)
    review_total_count = models.IntegerField(blank=True, null=True)
    sort_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

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