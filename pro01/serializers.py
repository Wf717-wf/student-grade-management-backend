from rest_framework import serializers
# from pro01.models import UserType, User

# class UserTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserType
#         fields = '__all__'
#
# class UserSerializer(serializers.ModelSerializer):
#     user_type_name = serializers.SerializerMethodField()
#     user_type_id = serializers.IntegerField(source='type.id', read_only=True)
#
#     def get_user_type_name(self, obj):
#         return obj.type.name if obj.type else None
#
#     class Meta:
#         model = User
#         fields = ['id', 'name', 'email', 'user_type_id', 'user_type_name']


# serializers.py
from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'age']  # Adjust fields as needed
