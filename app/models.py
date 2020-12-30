from django.db import models


class reg(models.Model):

    name=models.CharField(max_length=50)
    gender=models.TextField(max_length=10)
    email_reg=models.EmailField()
    username_reg=models.TextField()
    password_reg=models.TextField()




    def __str__(self):
        return self.name
