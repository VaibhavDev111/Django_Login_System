from django.db import models
import constants
import json


class UserQuerySet(models.QuerySet):
    def serialize(self):
        query_set = self
        final_array = []
        for obj in query_set:
            struct = json.loads(obj.serialize())
            final_array.append(struct)
        return json.dumps(final_array)


class UserManager(models.Manager):
    def get_queryset(self):
        return UserQuerySet(self.model, self._db)


class UserInfo(models.Model):

    id = models.IntegerField(primary_key=True, unique=True)
    imageUrl = models.CharField(max_length=50, default=constants.DEFAULT_IMAGE)
    name = models.CharField(max_length=70, default=constants.DEFAULT_NAME)
    fatherName = models.CharField(max_length=70, default=constants.DEFAULT_FATHER_NAME)
    deptName = models.CharField(max_length=70, default=constants.DEFAULT_DEPT_NAME)
    inchargeName = models.CharField(max_length=70, default=constants.DEFAULT_INCHARGE_NAME)
    contactNo = models.CharField(max_length=15, default=constants.DEFAULT_CONTACT_NO)
    bloodGroup = models.CharField(max_length=5, default=constants.DEFAULT_BLOOD_GROUP)
    qualification = models.CharField(max_length=50, default=constants.DEFAULT_QUALIFICATION_GROUP)

    objects = UserManager()


class EnterExitQuerySet(models.QuerySet):
    def serialize(self):
        query_set = self
        final_array = []
        for obj in query_set:
            struct = json.load(obj.serialize())
            final_array.append(struct)
        return json.dumps(final_array)


class EnterExitManager(models.Manager):
    def get_queryset(self):
        return EnterExitQuerySet(self.model, self._db)


class EnterExitInfo(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    uid = models.IntegerField()
    inTime = models.TimeField(auto_now_add=True)
    outTime = models.TimeField(auto_now_add=False)
    diffTime = models.TimeField(auto_created=False)
    date = models.DateField(auto_now_add=True)
    isIn = models.BooleanField()

    objects = EnterExitManager()
