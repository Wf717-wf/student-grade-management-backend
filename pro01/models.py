from django.db import models


# class Author(models.Model):
#     name = models.CharField(max_length=100, null=True, blank=True)
#     age = models.IntegerField(null=True, blank=True, help_text='年龄')
#     id = models.AutoField(primary_key=True, help_text='作者id')
#
#     class Meta:
#         db_table = 'author'
#         verbose_name = 'Author'
#         verbose_name_plural = 'Authors'
#         # 添加表注释的方式（仅在某些数据库中支持）
#         # 注释仅在 MySQL 中有效，其他数据库可能不支持这种功能
#         # managed = False
