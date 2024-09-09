from django.db import models

# class UserType(models.Model):
#     name = models.CharField(max_length=50, unique=True, verbose_name='名称')
#
#     class Meta:
#         verbose_name = '用户类型表'
#         db_table = "user_type"
#
# class User(models.Model):
#     name = models.CharField(max_length=50, verbose_name='姓名')
#     email = models.CharField(max_length=50, unique=True, verbose_name='邮箱')
#     type = models.ForeignKey(UserType, null=True, on_delete=models.SET_NULL, verbose_name='用户类型')
#
#     def update_user_info(self, name, user_type_id, email):
#         self.name = name
#         self.email = email
#         self.user_type_id = user_type_id
#         self.save()
#
#     class Meta:
#         verbose_name = '用户表'
#         db_table = "user"


# class Book(models.Model):
#     title = models.CharField(max_length=100, null=True, blank=True, verbose_name='标题')
#     author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.CASCADE, verbose_name='作者')
#
#     class Meta:
#         verbose_name = '图书'
#         verbose_name_plural = '图书表'
#         db_table = 'book'
#
#     def __str__(self):
#         return self.title
class Author(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, help_text='年龄')
    id = models.AutoField(primary_key=True, help_text='作者id')

    class Meta:
        db_table = 'author'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        # 添加表注释的方式（仅在某些数据库中支持）
        # 注释仅在 MySQL 中有效，其他数据库可能不支持这种功能
        # managed = False

    def __str__(self):
        return self.name if self.name else 'No Name'
