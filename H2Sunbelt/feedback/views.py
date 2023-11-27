from django.shortcuts import render
from .models import Guestbook
MENU = {"Home": "/", "Unser Ziel": "/goal", "Kontakt": "/about", "Feedback": "/feedback"}


def feedback_page(request):
    guestbook = Guestbook.objects.all()
    title = "Feedback"
    data = {"menu": MENU, "title": title, "guestbook": guestbook}
    return render(request, "./feedback.html", context=data)


def add_comment_page(request):
    guestbook = Guestbook.objects.all()
    title = "Add comment"
    data = {"menu": MENU, "title": title, "guestbook": guestbook}
    return render(request, "./add_comment.html", context=data)


def thanks_page(request):
    user_first_name = request.POST['user_first_name']
    user_last_name = request.POST['user_last_name']
    email = request.POST['email']
    feedback_frame = request.POST['feedback_frame']
    Guestbook.objects.create(user_first_name=user_first_name, user_last_name=user_last_name,
                             email=email, feedback_frame=feedback_frame,)
    title = "Thank you!"
    data = {"menu": MENU, "title": title, "user_first_name": user_first_name, "user_last_name": user_last_name}
    return render(request, "./thanks.html", context=data)


# Create your views here.
