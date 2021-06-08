from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(blank=True)
    created_ad = models.DateTimeField(auto_now_add="True", verbose_name="Дата создания")
    updated_ad = models.DateTimeField(auto_now="True", verbose_name="Дата обновления")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликована нет ?")
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        verbose_name="Категория",
    )

    def get_absolute_url(self):
        return reverse("views_news", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_ad"]


class Category(models.Model):
    title = models.CharField(
        max_length=150, db_index=True, verbose_name="Название категории"
    )

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]
