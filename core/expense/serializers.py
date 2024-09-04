from rest_framework import serializers
from .models import Transactions

class TransactionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transactions
        fields =[ 
                 "id",
                 "title",
                "amount",
                "trans_type"
        ]
    
    def validate(self, attrs):
        if not attrs.get('trans_type'):
            raise serializers.ValidationError("Transaction type is required")
        return attrs

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 200)
    password = serializers.CharField(max_length = 20)
    