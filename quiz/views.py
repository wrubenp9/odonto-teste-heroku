from django.shortcuts import render

def forms(request):
    template_name = 'forms.html'
    return render(request, template_name)