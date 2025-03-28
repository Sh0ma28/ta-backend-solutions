from django.contrib import admin
from django.contrib.auth.models import User, Group
import nested_admin
from rangefilter.filters import DateRangeFilterBuilder
from .models import Status, Type, Category, Subcategory, Record

# Register your models here.
# Инлайны
class SubcategoryInline(nested_admin.NestedStackedInline):
    model = Subcategory
    extra = 0

class CategoryInline(nested_admin.NestedStackedInline):
    model = Category
    inlines = [SubcategoryInline]
    extra = 0

# Статус
class StatusAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    list_display_links = ['name']

# Тип
class TypeAdmin(nested_admin.NestedModelAdmin):
    inlines = [CategoryInline]
    search_fields = ['name']
    list_display = ['name']
    list_display_links = ['name']

# Категория
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryInline]
    search_fields = ['name']
    list_display = ['name', 'type']
    list_display_links = ['name']
    list_filter = ['type']

# Подкатегория
class SubcategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'category', 'type_name']
    list_display_links = ['name']
    list_filter = ['category__type', 'category']

    @admin.display(description="Тип")
    def type_name(self, obj):
        return obj.category.type.name

# Запись
class RecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'status', 'type_name', 'category_name', 'subcategory', 'value']
    list_display_links = ['id']
    list_filter = [
        ('created_at', DateRangeFilterBuilder()),
        ('status', admin.RelatedOnlyFieldListFilter),
        ('subcategory__category__type', admin.RelatedOnlyFieldListFilter),
        ('subcategory__category', admin.RelatedOnlyFieldListFilter),
        ('subcategory', admin.RelatedOnlyFieldListFilter)
    ]

    @admin.display(description="Тип")
    def type_name(self, obj):
        return obj.subcategory.category.type.name
    
    @admin.display(description="Категория")
    def category_name(self, obj):
        return obj.subcategory.category.name

# Регистрации
admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Record, RecordAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
