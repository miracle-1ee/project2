from django.db import models

# Create your models here.

class cal(models.Model):
    value_a=models.CharField(max_length=10)
    value_b=models.FloatField(max_length=10)
    result=models.CharField(max_length=10)

class UserInfo(models.Model):
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    age=models.IntegerField()

class Department(models.Model):
    did=models.CharField(max_length=32)
    dname=models.CharField(max_length=32)

class Department2(models.Model):
    '''部门表'''
    title=models.CharField(verbose_name='标题',max_length=32)

    def __str__(self):
        return self.title

class UserInfo2(models.Model):
    '''员工表'''
    name=models.CharField(verbose_name="姓名",max_length=16)
    password=models.CharField(verbose_name="密码",max_length=64)
    age=models.IntegerField(verbose_name="年龄")
    account=models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0)
    create_time=models.DateTimeField(verbose_name="入职时间")

    '''外键'''
    depart=models.ForeignKey(to="Department2",to_field="id",on_delete=models.CASCADE)

    gender_choices=(
        (1,"男"),
        (2,"女"),
    )
    gender=models.SmallIntegerField(verbose_name="性别",choices=gender_choices)




