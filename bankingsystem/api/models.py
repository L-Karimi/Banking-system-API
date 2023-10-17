from django.db import models


# Create your models here.


class Branch(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    branch_code=models.CharField(max_length=250)                         
  
    class Meta:
        verbose_name_plural = "Branches"
    def json_object(self):
        return{
            'name':self.name,
            'address':self.address,
            'branch_code':self.branch_code
        }
    def __str__(self):
        return self.name
class Bank(models.Model):
   name = models.CharField(max_length=250)
   branch=models.ForeignKey(Branch,on_delete=models.CASCADE)

   def json_objects(self):
      return{
         
          'name':self.name,
          'branch':self.branch
      }
   def __str__(self):
      return self.name


class Clientmanager(models.Model):
    name = models.CharField(max_length=250)

    def _str_(self):
        return self.name
class Client(models.Model):
    name = models.CharField(max_length=250)
    address =models.CharField(max_length=250)

    def json_object(self):
     return{
        'name':self.name,
        'address':self.address
    }
    def __str__(self):
        return self.name

class Account(models.Model):
    """represents bank account"""
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    open_date=models.CharField(max_length=250)
    account_type=models.CharField(max_length=250)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def json_object(self):
        return{
            'client':self.client,
            'open_date':self.open_date,
            'account_type':self.account_type,
            'bank':self.bank
        }
    def __str__(self):
        return self.account_type


class transfer(models.Model):
    account=models.ForeignKey(Account, on_delete=models.CASCADE)
    branch =models.ForeignKey(Branch, on_delete=models.CASCADE)
    

    def json_object(self):
        return{
            'account':self.account,
            'branch':self.branch
        }
    def __str__(self):
        return "Accout transffered to {} Branch {}".format(self.account, self.branch.name)
    
class Withdraw(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class Deposit(models.Model):
    amount = models.FloatField()
    account=models.ForeignKey(Account, on_delete=models.CASCADE)




