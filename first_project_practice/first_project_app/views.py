from django.shortcuts import render
from django.http import HttpResponse
from first_project_app.models import Topic, Webpage, AccessRecord, User
from first_project_app.forms import NewUserForm

def index(request):
    # str = "<em> My own Django project and app with urls"
    return render(request, "first_project_app/index.html")


def help(request):
    my_dict = {'insert_me' : "Hey pillagaada endira pillagaada endi ra na gunde kaada lolli"}
    return render(request, 'first_project_app/index.html', context=my_dict)


def modelTest(request):
    webpagesList = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' : webpagesList}
    return render(request, 'first_project_app/modelindex.html', context=date_dict)

def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error from Form')
    return render(request, 'first_project_app/usersindex.html', {'form' : form})
