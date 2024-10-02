from django.urls import path
from .views import RegisterApiView, LoginApiView,TodoAddApiView,TodoListApiView,TodoDetailsApiView

# Define urlpatterns
urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('Addtodo/', TodoAddApiView.as_view(), name='addTodo'),
    path('TodoListApiView/', TodoListApiView.as_view(), name='listTodo'),
    path('todoDetial/<int:id>', TodoDetailsApiView.as_view(), name='details'),
]
