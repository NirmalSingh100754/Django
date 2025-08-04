from django.urls import path
from . import views


urlpatterns = [
    path('',views.all_nirmal, name='all_nirmal'),
    path('order/',views.order, name='order'),
    path('<int:chai_id>/',views.chai_desc, name='chai_desc'),
]
