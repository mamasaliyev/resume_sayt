from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from.models import About


def about_view(request):
    about_info = About.objects.all()
    return render(request,'about/about.html',{'about_info':about_info})

def download_file(request, file_id):
    about_entry = get_object_or_404(About, pk=file_id)
    file = about_entry.file
    response = HttpResponse(file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{file.name}"'
    return response
