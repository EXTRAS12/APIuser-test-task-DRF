from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser

from .forms import CustomUserCreationForm
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import *


class UserAPIPagination(PageNumberPagination):
    """Пагинация"""
    page_size = 0
    page_query_param = 'page_size'
    max_page_size = 100


class SignUpView(CreateView):
    """Регистрация с фронта"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users')
    template_name = 'signup.html'


class UserAPIList(generics.ListAPIView):
    """Постраничное получение кратких данных обо всех пользователях, User"""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserAPIPagination


class UserCurrentAPI(generics.RetrieveAPIView):
    """Получение данных о текущем пользователе"""
    serializer_class = UserCurrentSerializer

    def get_object(self):
        return self.request.user


class UserAPIUpdate(generics.RetrieveUpdateAPIView):
    """Изменение данных пользователя"""
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class AdminAPI(viewsets.ModelViewSet):
    """CRUD для админа"""
    queryset = CustomUser.objects.all()
    serializer_class = UserForAdminSerializer
    pagination_class = UserAPIPagination
    permission_classes = (IsAdminUser,)
