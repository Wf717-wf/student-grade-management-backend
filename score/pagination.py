# pagination.py
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'pageSize'
    max_page_size = 100

    # 自定义返回的格式
    def get_paginated_response(self, data):
        return Response({
                'total': self.page.paginator.count,
                'data': data  # 将 results 改成 data
        })
