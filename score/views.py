from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from .pagination import CustomPageNumberPagination  # 导入自定义分页器


class StudentViewSet(viewsets.ModelViewSet):
    # 倒序
    queryset = Student.objects.all().order_by('-id');
    pagination_class = CustomPageNumberPagination
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        gender = self.request.query_params.get('gender', None)

        if gender is not None:
            queryset = queryset.filter(gender=gender)

        return queryset



