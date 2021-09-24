from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail

# Create your views here.
def index(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        try:
            send_mail(
                subject,
                'Name - ' + name + '\n' + '\n' + 'Email Address - ' + email + '\n' + '\n' + 'Message - ' + message,
                email,
                ['hrushikeshbhat@gmail.com'],
                fail_silently=False,
            )
            context = {'success': True}
            return render(request, 'email_sucessfull.html', context)
        except BadHeaderError:
            return render(request, 'home.html')

    context = {'success': False}
    return render(request, 'home.html', context)

def games(request):
    return render(request, 'games.html')

def artworks(request):
    return render(request, 'artworks.html')

def others(request):
    return render(request, 'others.html')


def mainOld(request):
    return render(request, 'index.html')