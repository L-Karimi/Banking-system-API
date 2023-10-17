from rest_framework import serializers 


from .models import*


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('name','address','branch_code')
        read_only_fields =('id')

class BranchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('_all_')


class BankSerializer(serializers.ModelSerializer):
    branch=BranchSerializer
    class Meta:
        model = Bank
        fields = ('_all_')

class ClientManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientmanager
        fields = ('_all_')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('_all_')
class AccountSerializer(serializers.ModelSerializer):
    Client = ClientSerializer()
    bank=BankSerializer()
    class Meta:
       model= Account
       fields = ('_all_')
class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model =transfer
        fields = ('_all_')
class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = ('_all_')

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ('_all_')





