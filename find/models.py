from django.db import models


class Para(models.Model):
    para = models.TextField()
    
    def __str__(self):
        return self.para


class File(models.Model):
    file = models.FileField()

    def __str__(self):
        return self.file


class Word(models.Model):
    word = models.CharField(max_length=20)
    Location = models.ForeignKey(Para,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.word


class Unique(models.Model):
    word = models.CharField(max_length=20)
    location = models.ManyToManyField(Para, blank=True) #manytomany field it match more than one field 

    def __str__(self):
        return self.word
