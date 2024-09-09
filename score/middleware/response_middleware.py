import json
from django.http import JsonResponse

class UnifiedResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # 如果响应已经是 JsonResponse，则不进行处理
        if isinstance(response, JsonResponse):
            return response

        # 尝试解析响应内容
        try:
            content = response.content.decode('utf-8')
            if response.status_code == 204 or response.status_code == 201:
                # 处理 204 No Content 响应
                content = {
                    'code': 200,
                    'msg': '操作成功',
                    'data': None
                }
            else:
                try:
                    # 尝试解析内容为 JSON 对象
                    content_dict = json.loads(content)
                    # 如果内容已经是字典，并且不包含 code，则需要包装为统一格式
                    if isinstance(content_dict, dict) and 'code' not in content_dict:
                        content = {
                            'code': response.status_code,
                            'msg': response.reason_phrase,
                            'data': content_dict
                        }
                    else:
                        # 如果内容是列表或其他类型，则直接使用
                        content = {
                            'code': response.status_code,
                            'msg': response.reason_phrase,
                            'data': content_dict
                        }
                except json.JSONDecodeError:
                    # 如果内容不是有效 JSON 格式
                    content = {
                        'code': response.status_code,
                        'msg': response.reason_phrase,
                        'data': content
                    }
        except UnicodeDecodeError:
            # 处理内容无法解码的情况
            content = {
                'code': response.status_code,
                'msg': response.reason_phrase,
                'data': None
            }

        # 创建新的 JsonResponse，允许非字典对象
        new_response = JsonResponse(content, safe=False)

        # 如果状态码是 204，统一改为 200
        if response.status_code == 204 or response.status_code == 201:
            new_response.status_code = 200
        else:
            new_response.status_code = response.status_code

        # 复制其他头信息
        for header, value in response.items():
            new_response[header] = value

        return new_response
