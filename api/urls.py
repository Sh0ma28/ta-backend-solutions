from django.urls import path
from .views import getRoutes, StatusListCreate, StatusDetail, TypeListCreate, TypeDetail, \
    CategoryListCreate, CategoryDetail, SubcategoryListCreate, SubcategoryDetail, RecordListCreate, RecordDetail


urlpatterns = [
    path('', getRoutes, name='routes'),

    path('statuses', StatusListCreate.as_view(), name='status-list-create'),
    path('statuses/<int:pk>', StatusDetail.as_view(), name='status-detail'),
    
    path('types', TypeListCreate.as_view(), name='type-list-create'),
    path('types/<int:pk>', TypeDetail.as_view(), name='type-detail'),
    
    path('categories', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>', CategoryDetail.as_view(), name='category-detail'),

    path('subcategories', SubcategoryListCreate.as_view(), name='subcategory-list-create'),
    path('subcategories/<int:pk>', SubcategoryDetail.as_view(), name='subcategory-detail'),

    path('records', RecordListCreate.as_view(), name='record-list-create'),
    path('records/<int:pk>', RecordDetail.as_view(), name='record-detail'),
]