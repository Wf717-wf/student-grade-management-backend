from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    gender_display = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'name', 'gender', 'gender_display']

    def get_gender_display(self, obj):
        # 根据 gender 字段返回相应的性别描述
        return "女" if obj.gender == 1 else "男"
