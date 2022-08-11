from django.urls import path,include
from . import views


app_name = 'cars'

# domain.com/delete

urlpatterns = [
    path('add/',views.add,name='add'),
    path('delete/',views.delete,name='delete'),
    path('list/',views.list,name='list'),

]
