from django.shortcuts import render, redirect
  
from django.core.files.storage import FileSystemStorage         # Django’s FileSystemStorage class FileSystemStorage sets the base_url to the project’s MEDIA_ROOT.
from django.http import HttpResponse, HttpResponseNotFound  
 
#In this article I will show how to return a PDF response, which can also be used if you are just serving an existing PDF file
 
def pdfview(request):
    fs = FileSystemStorage()

    filename = 'django.pdf'           # yedi media folder vitra direct django.pdf naam gareko file cha vani yesari
    filename = 'pdf/django.pdf'       # yedi media folder vitra arko folder pdf cha re ani tes vitra django.pdf cha vani yesari path dina parcha (i.e pdf/django.pdf)  

    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="django.pdf"' #user will be prompted with the browser’s open/save file
            response['Content-Disposition'] = 'inline; filename="django.pdf"' #user will be prompted display the PDF in the browser
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')