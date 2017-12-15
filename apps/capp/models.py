from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        for field, value in postData.iteritems():
            if len(value) < 1:
                errors[field] = "{} field cannot be empty!".format(field)
            if len(postData["name"]) < 5:
                errors["name"] = "Name field must be more than 5 characters!"
            if len(postData["description"]) < 15:
                errors["description"] = "Description field must be more than 15 characters!"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = CourseManager()
