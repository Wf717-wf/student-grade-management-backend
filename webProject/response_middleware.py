from django.http import JsonResponse

class UnifiedResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # 如果响应已经是一个JsonResponse，则不进行处理
        if isinstance(response, JsonResponse):
            return response

        # 尝试解析响应内容，如果解析失败则返回原始响应
        try:
            data = response.content.decode('utf-8')
            # 如果响应内容为空且状态码为204，则将数据设置为None
            if response.status_code == 204:
                data = None
        except UnicodeDecodeError:
            data = response.content

            # 定义统一的响应格式
        unified_response = {
            'code': response.status_code,
            'message': response.reason_phrase,
            'data': data
        }

        # 创建新的JsonResponse对象
        new_response = JsonResponse(unified_response)

        # 如果状态码是204，统一改为200
        if response.status_code == 204:
            new_response.status_code = 200
        else:
            new_response.status_code = response.status_code


        # 复制其他头信息
        for header, value in response.items():
            new_response[header] = value

        return new_response
