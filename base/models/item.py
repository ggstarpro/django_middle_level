from django.db import models
from django.utils.crypto import get_random_string
import uuid
import os

def create_id():
    return get_random_string(22)

def upload_image_to(instance: "Item", filename: str):
    """ Itemは遅延型評価で指定 """
    item_id = instance.id
    return os.path.join('static', 'items', item_id, filename)


class Category(models.Model):
    """カテゴリ"""
    slug = models.CharField("カテゴリ名(アルファベット)", max_length=32, primary_key=True)
    name = models.CharField("カテゴリ名", max_length=32)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """タグ"""
    slug = models.CharField("タグ名(アルファベット)", max_length=32, primary_key=True)
    name = models.CharField("タグ名", max_length=32)

    def __str__(self):
        return self.name

class Item(models.Model):
    """商品"""
    # id = models.CharField(primary_key=True, default=create_id, max_length=22, editable=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("名前", default="", max_length=50)
    price = models.PositiveIntegerField("価格", default=0)
    stock = models.PositiveIntegerField("在庫",default=0)
    description = models.TextField("説明", default="", blank=True)
    sold_count = models.PositiveIntegerField("販売数", default=0)
    is_published = models.BooleanField("公開",default=False)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)
    image = models.ImageField(default="", blank=True, upload_to=upload_image_to)
    # カテゴリが削除されたとき、商品にはNULLをセットする
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)


    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "商品"


