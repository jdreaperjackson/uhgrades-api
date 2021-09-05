from django.db import models

# Create your models here.

class Grade(models.Model):
    term = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    catalogNbr = models.CharField(max_length=100)
    courseDescription = models.CharField(max_length=100)
    instructorLast = models.CharField(max_length=100)
    instructorFirst = models.CharField(max_length=100)
    aCount = models.CharField(max_length=100)
    bCount = models.CharField(max_length=100)
    cCount = models.CharField(max_length=100)
    dCount = models.CharField(max_length=100)
    fCount = models.CharField(max_length=100)
    satisfactory = models.CharField(max_length=100)
    dropCount = models.CharField(max_length=100)
    percentA = models.CharField(max_length=100)

    def __str__(self):
        return self.courseDescription