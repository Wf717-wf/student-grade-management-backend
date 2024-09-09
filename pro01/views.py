from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Author
from .serializers import AuthorSerializer


# class AuthorListView(APIView):
#     def get(self, request):
#         search_term = "2"  # 要模糊搜索的关键字
#
#         with connection.cursor() as cursor:
#             # 执行原生 SQL 查询
#             cursor.execute("""
#                 SELECT * FROM author
#                 WHERE name LIKE %s
#             """, [f"%{search_term}%"])
#
#             # 获取查询结果
#             rows = cursor.fetchall()
#             print(rows)
#
#         if not rows:
#             return Response([])
#
#         # 假设 rows 包含 (id, name) 等字段，我们需要将其转换为字典形式
#         # 如果您有更多的字段，您需要在这里添加它们
#         authors_data = [{'id': row[0], 'name': row[1]} for row in rows]
#
#         # 序列化数据
#         serializer = AuthorSerializer(data=authors_data, many=True)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data)


class AuthorListView(APIView):
    def get(self, request):
        # 查询所有数据
        authors=Author.objects.all()
        # 过滤数据并获取查询集
        # authors = Author.objects.filter(name='杜甫'）
        # 使用like进行查找。示例代码如下：

        # authors = Author.objects.filter(id__gt=4)

        # authors=Author.objects.filter(name__icontains='2')

        # 提取指定字段

        # 根据id倒序
        # authors=Author.objects.order_by('-id')
        # 删除

        # authors.delete()
        if not authors.exists():
            return Response([])

        # # 获取第一个匹配的作者
        # author = authors[0]
        # author.name='杜甫'
        # author.save()
        # 序列化单个对象，不需要 many=True
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
