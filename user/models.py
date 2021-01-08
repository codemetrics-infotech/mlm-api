from django.db import models

# Create your models here.

class BasicDetail(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True, default='')
    last_name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()
    pan_number = models.CharField(max_length=12)
    mobile_number = models.CharField(max_length=13)
    email = models.EmailField(max_length=30)
    photo = models.ImageField(upload_to='user/images',blank=True ,default='')
    referral_code = models.CharField(max_length=20)

    def __str__(self):
        return self.user_id

class ParmanentAddress(models.Model):
    address_id = models.CharField(max_length=20, primary_key=True)
    user_id = models.ForeignKey(BasicDetail, on_delete=models.CASCADE, related_name='address_id')
    house_number = models.CharField(max_length=5)
    street = models.CharField(max_length=20)
    village = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    nationality = models.CharField(max_length=20)

    def __str__(self):
        return self.address_id+''+self.state