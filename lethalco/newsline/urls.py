from django.urls import path
# Импортируем созданные нами представления
from .views import PostsList, PostDetail, PostSearch, PostCreate, ProfileDetail, MessageCreate, MessageList
from django.views.decorators.cache import cache_page
from .models import Message

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostsList.as_view(), name='post_list'), #cache_page(60)(PostsList.as_view())
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostDetail.as_view(), name='post_detail'), #cache_page(300)(PostDetail.as_view())
   path('search/', PostSearch.as_view(), name='post_search'),
   path('memes/create/', PostCreate.as_view(), name='post_create'),
   path('found/create/', PostCreate.as_view(), name='post_create'),
   path('profile/<int:pk>', ProfileDetail.as_view(), name='profile' ),
   path('message/<int:pk>', MessageCreate.as_view(model=Message, success_url='/posts/'), name='message'),
   path('messages/', MessageList.as_view(), name='messages')
   
#    path('<int:pk>/edit/', PostUpdate.as_view(), name='edit'),
#    path('<int:pk>/delete/', PostDelete.as_view(), name='delete'),
#    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
#    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]