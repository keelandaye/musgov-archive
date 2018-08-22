from django.db import models


class House(models.Model):
    house_name = models.CharField(max_length=100)
    house_code = models.CharField(max_length=2)
    logo_url = models.URLField(default="https://einfon.com/wp-content/uploads/2017/05/Flag-Of-USA.jpg")

    def __str__(self):
        return self.house_name + " - " + self.house_code


class Bill(models.Model):
    bill_number = models.IntegerField()
    bill_name = models.CharField(max_length=250)
    bill_house = models.ForeignKey(House, on_delete=models.CASCADE, default=1)
    bill_content = models.TextField()
    date_first_posted = models.DateField()

    def __str__(self):
        return self.bill_house.house_code + '. ' + str(self.bill_number) + ' - ' + self.bill_name
