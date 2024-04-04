from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.viewsets import ViewSet
from rest_framework.generics import CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,ListAPIView

from budget.serializers import UserSerializer,ExpenseSerializer,Incomeserializer
from budget.models import Expense,Income
from django.contrib.auth.models import User

# Create your views here.

class SignupView(CreateAPIView):

    serializer_class=UserSerializer
    queryset=User.objects.all()




class ExpenseViewSetView(ViewSet):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):

        qs=Expense.objects.filter(owner=request.user)

        serializer_instance=ExpenseSerializer(qs,many=True)

        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
    

    def create(self,request,*args,**kwargs):

        serializer_instance=ExpenseSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(owner=request.user)
            return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



class IncomeViewsetView(ViewSet):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):

        qs=Income.objects.filter(owner=request.user)
        serializer_instance=Incomeserializer(qs,many=True)

        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
    

    def create(self,request,*args,**kwargs):

        serializer_instance=Incomeserializer(data=request.data)
        if serializer_instance.is_valid():

            serializer_instance.save(owner=request.user)
            return Response (data=serializer_instance.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST) 



class ExpenseDetailView(RetrieveAPIView,DestroyAPIView,UpdateAPIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=ExpenseSerializer
    queryset=Expense.objects.all()





class IncomeListCreateView(ListAPIView,CreateAPIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=Incomeserializer
    queryset=Income.objects.all()


    def get_queryset(self):
        qs=Income.objects.filter(owner=self.request.user)

        return qs 
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class IncomeDetailView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):


    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=Incomeserializer
    queryset=Income.objects.all()