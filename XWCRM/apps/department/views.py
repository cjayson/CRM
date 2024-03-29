from django.shortcuts import render
from rest_framework.views import APIView
from .models import Department
from .serializers import DepartmentModelSerializer
from rest_framework.response import Response
from staff.models import StaffInfo


# Create your views here.
class DepartmentAPIView(APIView):
    def get(self, request):
        """
        返回所有的部门
        :param request: 空
        :return: [{"name":"总裁办","desc":"132" },{"name":"销售部","desc":"123" }]
        """
        res_list = []
        dep_list = Department.objects.all()
        print(dep_list)
        for dep in dep_list:
            print(dep, type(dep))
            serializer = DepartmentModelSerializer(dep)
            # print(serializer)
            print(serializer.data)
            res_list.append(serializer.data)
        return Response({"result": res_list})

    def create(self, request):
        res = "创建失败"
        name = request.query_params.get("name")
        desc = request.query_params.get("desc")
        if not Department.objects.get(name=name):
            Department.objects.create(
                name=name,
                desc=desc
            )
            res = "创建成功"
        return Response({"result": res})

    def put(self, request):
        res = "修改失败"
        id = request.query_params.get("id")
        name = request.query_params.get("name")
        desc = request.query_params.get("desc")
        dep_obj = Department.objects.get(id=id)
        if dep_obj:
            dep_obj.name = name
            dep_obj.desc = desc

            dep_obj.save()
            res = dep_obj
        return Response({"result": res})


class DepartmentSearchAPIView(APIView):
    def get(self, request):
        """
        获取某个部门的所有人员
        :return: {"一个部门":[人,人]}
        """
        department_name = request.query_params.get("department_name")
        staff_list = []
        if department_name:
            try:
                department = Department.objects.get(name=department_name)
            except Department.DoesNotExist:
                return Response({"result":"对不起,该部门不存在"})
            queryset = StaffInfo.objects.filter(department=department).all()
            print(queryset)
            for i in queryset:
                staff_list.append({
                    "username": i.username,
                    "department": i.department.name,
                    "mobile": i.mobile
                })
        return Response({"result":staff_list})
