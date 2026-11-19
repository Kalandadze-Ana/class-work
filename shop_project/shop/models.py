from django.db import models

class Product(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.customer} - {self.product}"