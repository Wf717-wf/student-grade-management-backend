# from django.db import models
#
# # Create your models here.
#
#
# from django.db import models
#
# class Author(models.Model):
#     # 主键 id 字段会自动添加
#     name = models.CharField(max_length=100)
#     email = models.EmailField(blank=True, null=True)  # 可选字段
#     bio = models.TextField(blank=True, null=True)  # 可选字段
#     class Meta:
#         db_table = 'author'
#         verbose_name = 'Author'
#         verbose_name_plural = 'Authors'
#         # 添加表注释的方式（仅在某些数据库中支持）
#         # 注释仅在 MySQL 中有效，其他数据库可能不支持这种功能
#         # managed = False
#
# class Article(models.Model):
#     # 主键 id 字段会自动添加
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     published_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # 可选字段
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'article'
#         verbose_name = 'article'
#         verbose_name_plural = 'article'
#         # 添加表注释的方式（仅在某些数据库中支持）
#         # 注释仅在 MySQL 中有效，其他数据库可能不支持这种功能
#         # managed = False
#
#
# class AuthorExtension(models.Model):
#     id = models.AutoField(primary_key=True)
#     birthday = models.CharField(max_length=20, blank=True, null=True)
#     university = models.CharField(max_length=20, blank=True, null=True)
#     # 一对一关系
#     author = models.OneToOneField(Author, on_delete=models.CASCADE, blank=True, null=True, related_name='extensions')
#
#     class Meta:
#         db_table = "author_extension"
#         verbose_name = "AuthorExtension"
#         verbose_name_plural = "AuthorExtension"