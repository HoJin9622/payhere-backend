from django.db import models
from common.models import CommonModel


class Household(CommonModel):

    """가계부 기록 모델 정의"""

    amount = models.PositiveIntegerField(verbose_name="사용금액")
    memo = models.TextField(default="", verbose_name="메모", blank=True)
    is_active = models.BooleanField(default=True, verbose_name="활성여부")
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="households",
        verbose_name="유저",
    )

    class Meta:
        verbose_name = "가계부 기록"
        verbose_name_plural = "가계부 기록(들)"

    def __str__(self):
        return f"{self.user}의 {self.amount}원 지출"
