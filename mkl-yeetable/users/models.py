from django.db import models

# Create your models here.


# class Hours(models.Model):
#     monday = models.CharField(max_length=200)
#     tuesday = models.CharField(max_length=200)
#     wednesday = models.CharField(max_length=200)
#     thursday = models.CharField(max_length=200)
#     friday = models.CharField(max_length=200)
#     saturday = models.CharField(max_length=200)
#     sunday = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.monday, self.tuesday


class Restaurant(models.Model):
    business_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    stars = models.DecimalField(max_digits=11, decimal_places=1)
    review_count = models.IntegerField()
    is_open = models.BooleanField()
    categories = models.CharField(max_length=200)
    hours = models.CharField(max_length=200)
    # hours = models.ForeignKey(Hours, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
