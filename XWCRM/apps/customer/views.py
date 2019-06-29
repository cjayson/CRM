from rest_framework.views import APIView
from .models import Customer
from staff.models import StaffInfo
from rest_framework.response import Response
from django.db.models import Q
from .serializers import CutomerSerializers, PublicCutomerSerializers


class CustomerAPIView(APIView):
    def get(self, request):
        """
        查看自己的所有顾客
        :param request:
        :return:
        """
        owner_id = int(request.query_params.get("id"))
        owner_name = request.query_params.get("username")
        customer_list = []
        try:
            staff = StaffInfo.objects.get(Q(id=owner_id) or Q(username=owner_name))
        except StaffInfo.DoesNotExist:
            return Response({"message": 0, "result": "当前用户不存在,请确认后重试!"})
        queryset = Customer.objects.filter(owner=staff).all()
        for i in queryset:
            customer_list.append({
                "name": i.name,
                "desc": i.desc,
                "status": i.status,
                "owner": i.owner.username,
            })

        return Response({"message": 1, "result": customer_list})

    def post(self, request):
        """
        添加一名新顾客
        :param request:
        :return: {"message":1,"result":""}
        """
        name = request.query_params.get("name")
        mobile = request.query_params.get("mobile")
        status = request.query_params.get("status")
        desc = request.query_params.get("desc")
        age = request.query_params.get("age")
        owner = request.query_params.get("owner")


        try:
            user = Customer.objects.create(
                mobile=mobile,
                name=name,
                desc=desc,
                age=age,
                status=status,
                owner=StaffInfo.objects.get(id=owner)
            )

            user.save()

            return Response({"message": 1, "result": "创建客户成功"})
        except:
            return Response({"message":0,"result":"创建客户失败"})

    # query = CutomerSerializers(message)


    def put(self, request):
        """
        修改顾客信息
        :param request:
        :return:
        """
        id = request.query_params.get("id")
        name = request.query_params.get("name")
        mobile = request.query_params.get("mobile")
        status = request.query_params.get("status")
        desc = request.query_params.get("desc")
        age = request.query_params.get("age")
        owner = request.query_params.get("owner")
        try:
            customer = Customer.objects.get(id=id)
            customer.name = name
            customer.mobile = mobile
            customer.status = status
            customer.desc = desc
            customer.age = age
            customer.owner = StaffInfo.objects.get(id=owner)
            customer.save()
            return Response({"message": 1, "result": "成功修改客户资料"})
        except Customer.DoesNotExist:
            return Response({"message": 0, "result": "修改客户失败"})


    def delete(self, request):
        """
        将顾客放入公海列表
        :param request:
        :return:
        """
        id = int(request.query_params.get("id"))
        try:
            customer = Customer.objects.get(id=id)
            customer.owner = None
            customer.save()
            return Response({"message": 1, "result": "成功修改为公海客户"})
        except Customer.DoesNotExist:
            return Response({"message": 0, "result": "修改客户失败"})


class PublicCustomerAPIView(APIView):
    def get(self, request):
        customer_list = []
        query = Customer.objects.filter(owner=None).all()
        serializers = PublicCutomerSerializers(query, many=True)
        for customer in serializers.data:
            customer_list.append({
                "name": customer.get("name"),
                "desc": customer.get("desc"),
                "status": customer.get("status")
            })

        return Response({"message": 1, "result": customer_list})

    def put(self, request):
        """
        修改顾客为私有客户
        :param request:
        :return:
        """
        id = request.query_params.get("id")
        owner = request.query_params.get("owner")
        try:
            customer = Customer.objects.get(id=id)
            customer.owner = StaffInfo.objects.get(id=owner)
            customer.save()
            return Response({"message": 1, "result": "成功修改为私有客户"})
        except Customer.DoesNotExist:
            return Response({"message": 0, "result": "修改客户失败"})
