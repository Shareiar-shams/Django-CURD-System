from django.urls import path
from .views import Home, Add_Worker, Delete_Worker, Edit_Wroker

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add-worker', Add_Worker.as_view(), name='add-worker'),
    path('delete-worker', Delete_Worker.as_view(), name='delete-worker'),
    path('edit-worker/<int:id>/', Edit_Wroker.as_view(), name='edit-worker')
]