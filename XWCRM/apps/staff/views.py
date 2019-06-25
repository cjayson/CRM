from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StaffInfo
from .serializers import StaffModelSerializer, RegisterModelSerializer
from rest_framework.generics import CreateAPIView,UpdateAPIView


# Create your views here.


class LoginAPIView(APIView):
    def get(self, request):
        """
        登录验证
        :param request:   从request.query_params中获取参数
        :return:{"name":"","id":"","role":"ceo","role_power":"1"}
        """
        print(request.query_params)
        username = request.query_params.get("username")
        password = request.query_params.get("password")
        # 过滤出有无该账号
        staff = StaffInfo.objects.filter(username=username, password=password, is_delete=False).first()
        if staff:
            serializer = StaffModelSerializer(staff)
            print(serializer.data)
            return Response({"res": serializer.data})
        return Response({"result": "该用户不存在!!!"})


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterModelSerializer
    queryset = StaffInfo.objects.all()


class StaffListAPIView(APIView):
    def get(self, request):
        """
        查看员工信息
        :param request: pk = id
        :return: {员工信息}
        """
        pk = request.query_params.get("id")
        user = StaffInfo.objects.get(pk=pk)
        if user:
            userinfo = {
                "username": user.username,
                "mobile": user.mobile,
                "desc": user.desc,
                "gender": user.gender,
                "role": user.role,
                "role_power": user.role_power,
                "department": user.department.name
            }
            return Response({"result": userinfo})
        return Response({"result": "查询出错,请确认员工信息"})

    def put(self,request):
        pk = request.query_params.get("id")
        print(pk)
        user = StaffInfo.objects.get(pk=pk)
        if user:
            user.username = request.query_params.get("username")
            user.password = request.query_params.get("password")
            user.mobile = request.query_params.get("mobile")
            user.desc = request.query_params.get("desc")
            user.gender = request.query_params.get("gender")

            user.save()

            userinfo = {
                "username": user.username,
                "mobile": user.mobile,
                "desc": user.desc,
                "gender": user.gender,
                "role": user.role,
                "role_power": user.role_power,
                "department": user.department.name
            }
            return Response({"result": userinfo})
        return Response({"result": "查询出错,请确认员工信息"})


