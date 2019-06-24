from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StaffInfo
# Create your views here.

class LoginAPIView(APIView):
    def get(self,request):
        """
        登录验证呢
        :param request: 发送过来的数据
        :return:{"name":"","id":"","role":"ceo","role_power":"1"}
        """
        print(request.data)
        return Response({"res":"OK"})
