from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.pagination import LimitOffsetPagination


class UserViewSet(DjoserUserViewSet):
    search_fields = ("username",)
    lookup_field = "username"
    lookup_value_regex = r"[\w.@+-]+"
    pagination_class = LimitOffsetPagination
