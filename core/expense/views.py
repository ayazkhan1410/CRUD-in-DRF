from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transactions
from .serializers import *
from rest_framework.views import APIView
from django.db.models import Sum
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET'])
def get_transactions(request):
    trans_obj = Transactions.objects.all()
    serializer = TransactionsSerializer(trans_obj, many=True)
    return Response({
        "data":serializer.data,
    }) 

class RecordCreation(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        trans_obj = Transactions.objects.all().order_by('-pk')
        serializer = TransactionsSerializer(trans_obj, many=True)
        return Response({
            "data":serializer.data,
            "total": trans_obj.aggregate(total = Sum('amount'))['total'] or 0
        }) 
    
    def post(self, request):
        data = request.data        
        serializer = TransactionsSerializer(data = data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                "message": "Data saved",
                "data": serializer.data
            })
        else:
            return Response({
                "message": "data not saved",
                "error": serializer.errors
            })
    
    def patch(self,request):
        data = request.data
        
        if not data.get('id'):
            return Response({
                "error": "ID is required"
            })
            
        trans_obj = Transactions.objects.get(id = data.get('id'))
        serializer = TransactionsSerializer(trans_obj, data = data, partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                "message": "Data Partially Updated successfully",
                "data": serializer.data
            })
        else:
            return Response({
                "message": "data not saved",
                "error": serializer.errors
            })
    
    def put(self, request):
        data = request.data
        
        if not data.get('id'):
            return Response({
                "error": "ID is required"
            })
            
        trans_obj = Transactions.objects.get(id = data.get('id'))
        serializer = TransactionsSerializer(trans_obj, data = data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                "message": "Data Updated successfully",
                "data": serializer.data
            })
        else:
            return Response({
                "message": "data not saved",
                "error": serializer.errors
            })
    
    def delete(self, request):
        data = request.data
        
        if not data.get('id'):
            return Response({
                "error": "ID is required"
            })
        id = data.get('id')
        trans_obj = Transactions.objects.get(id = id).delete()
        
        return Response({
            "Message": "Record Deleted",
            "data": {}
        })

class LoginApi(APIView):
    
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not  serializer.is_valid(raise_exception=True):
            return Response({
                "message": "Error",
                "data":serializers.error
            })
            
        user_obj = authenticate(username = data['username'], password = data['password'])
        token, _ = Token.objects.get_or_create(user=user_obj)
        
        if user_obj:
            return Response({
                "status": True,
                "Token": str(token)
            })
        else:
            return Response({
                "status": False,
                "data": "invalid credential"
            })