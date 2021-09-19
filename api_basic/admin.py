from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import Grade
from django import forms

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'term', 'subject', 'catalogNbr', 'courseDescription',
                  'instructorLast', 'instructorFirst', 'aCount', 'bCount',
                  'cCount', 'dCount', 'fCount', 'satisfactory', 'dropCount',
                  'percentA')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Grade.objects.update_or_create(
                    term=fields[0],
                    subject=fields[1],
                    catalogNbr=fields[2],
                    courseDescription=fields[3],
                    instructorLast=fields[4],
                    instructorFirst=fields[5],
                    aCount=fields[6],
                    bCount=fields[7],
                    cCount=fields[8],
                    dCount=fields[9],
                    fCount=fields[10],
                    satisfactory=fields[11],
                    dropCount=fields[12],
                    percentA=fields[13],

                )

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(Grade, GradeAdmin)