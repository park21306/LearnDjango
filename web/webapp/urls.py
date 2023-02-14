from django.urls import path
from webapp import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('form',views.form),
    path('showdata',views.showdata),
    path('edit/<person_id>',views.edit),
    path('delete/<person_id>',views.delete)
]
