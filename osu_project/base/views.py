from django.shortcuts import render

from django.http import HttpResponse

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'base/homepage.html', context_dict)

def location(request):
    return render(request, 'base/location.html')

def menus(request):
    return render(request, 'base/menus.html')

def schedule(request):
    return render(request, 'base/schedule.html')

def rules(request):
    return render(request, 'base/rules.html')

def registration(request):
    return render(request, 'base/registration.html')

def contact(request):
    return render(request, 'base/contact.html')
