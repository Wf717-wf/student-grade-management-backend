# books/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from .models import Author
from .forms import AuthorForm

from django.db import connection


# 显示作者列表
def author_list(request):
    # 查询所有作者
    authors= Author.objects.all()
    # print(authors)
    return render(request, 'books/author_list.html', {'authors': authors})

# 显示单个作者的详细信息
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'books/author_detail.html', {'author': author})
# 创建新的作者
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('author-list'))
    else:
        form = AuthorForm()
    return render(request, 'books/author_form.html', {'form': form})
# 编辑现有作者
def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect(reverse('author-detail', args=[author.pk]))
    else:
        form = AuthorForm(instance=author)
    return render(request, 'books/author_form.html', {'form': form})

# 删除作者
def author_delete(request, pk):
    #根据主键 pk 从 Author 模型中获取对应的对象,果该主键对应的对象存在，则将其赋值给 author 变量；如果对象不存在，则返回一个 404 错误页面，表示找不到所请求的资源。
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':

        author.delete()
        return redirect(reverse('author-list'))
    return render(request, 'books/author_confirm_delete.html', {'author': author})



#使用原生sql操作数据库
def getUser(request):
    cursor = connection.cursor()
    # 执行 SQL 查询
    cursor.execute("SELECT * FROM user")
    # 获取所有的数据
    rows = cursor.fetchall()
    # 获取列名
    column_names = [desc[0] for desc in cursor.description]

    # 将数据转换为字典格式
    data = [dict(zip(column_names, row)) for row in rows]
    data = {
        "data": data
    }
    # 返回 JSON 响应
    return JsonResponse(data, safe=False)


def addUser(request):
    # res = [{
    #     'name': "12"
    # }]
    # print(122)
    cursor = connection.cursor()
    # 执行 SQL 查询
    cursor.execute("SELECT * FROM user")
    # 获取所有的数据
    rows = cursor.fetchall()

    user=rows.objects.filter(name="张三")
    print('过滤的数据为：')
    print(user)


    # 获取列名
    column_names = [desc[0] for desc in cursor.description]

    # 将数据转换为字典格式
    data = [dict(zip(column_names, row)) for row in rows]
    data = {
        "data": data
    }
    # 返回 JSON 响应
    return JsonResponse(data, safe=False)