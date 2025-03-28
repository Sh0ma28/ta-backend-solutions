from django.db import models

# Create your models here.
# Статус
class Status(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name

# Тип
class Type(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name

# Категория
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Тип')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

# Подкатегория
class Subcategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name

# Запись
class Record(models.Model):
    created_at = models.DateField(auto_now_add=True, editable=True, verbose_name='Дата создания')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    value = models.IntegerField(default=0, verbose_name='Сумма')
    comment = models.TextField(blank=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Запись о ДДС'
        verbose_name_plural = 'Записи о ДДС'

    def __str__(self):
        return f"{self.id}"
