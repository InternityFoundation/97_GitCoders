from django.db import models
import os
import re

from datetime import datetime
def upload_livestock_image_directory_path(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return 'livestock/'+re.sub('[-:. ]','',str(datetime.today()))+file_extension


class CategoryA(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to = upload_livestock_image_directory_path)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name

class CategoryB(models.Model):
    category = models.ForeignKey("categoryA", verbose_name="Category A", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to = upload_livestock_image_directory_path)
    disease_name = models.CharField("Disease", max_length=120)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name

class CategoryAImage(models.Model):
    category = models.ForeignKey("categoryA", verbose_name="Category A", on_delete=models.CASCADE)
    image = models.ImageField(upload_to = upload_livestock_image_directory_path)


class CategoryBImage(models.Model):
    category = models.ForeignKey("categoryB", verbose_name="Category B", on_delete=models.CASCADE)
    image = models.ImageField(upload_to = upload_livestock_image_directory_path)

class LiveStockDisease(models.Model):
    name = models.CharField("Disease Name", max_length=100)
    about = models.TextField("About", null=True, blank= True)
    causes = models.TextField("Causes", null=True, blank= True)
    mode_of_transmission = models.TextField("Mode Of Transmission", null=True, blank= True)
    symptoms = models.TextField("Symptoms", null=True, blank= True)
    diagnostic_tests = models.TextField("Diagnostic Tests", null=True, blank= True)
    preventive_methods = models.TextField("Preventive Methods", null=True, blank= True)
    suggested_first_aid = models.TextField("Suggested First Aid", null=True, blank= True)
    control_measures = models.TextField("Control Measures", null=True, blank= True)

    def __str__(self):
        return self.name



# class UploadFile(models.Model):
#     name = models.CharField(max_length=30, null = True, blank = True)
#     image = models.ImageField(upload_to = upload_image_directory_path)
#     edited = models.ImageField(upload_to = upload_image_directory_path, null = True, blank = True)
#     segmented = models.ImageField(upload_to = upload_image_directory_path, null = True, blank = True)
#     def __str__(self):
#         return self.name

# class Disease(models.Model):
#     name = models.CharField(max_length=100)
#     plant = models.ForeignKey('Plant', on_delete=models.CASCADE , related_name="diseases")
#     symptoms = models.TextField(null = True, blank = True)
#     cause = models.TextField(null = True, blank = True)
#     comments = models.TextField(null = True, blank = True)
#     management = models.TextField(null = True, blank = True)
#     image = models.CharField(max_length = 100, null = True, blank = True)

#     def __str__(self):
#         return self.name
