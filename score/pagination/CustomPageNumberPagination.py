# pagination.py
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'  # 允许通过查询参数 'limit' 设置每页记录数
    max_page_size = 100  # 最大每页记录数
