# from django.http import HttpResponse
# return HttpResponse (text)

from django.shortcuts import render

MENU = {"Home": "/", "Unser Ziel": "/goal", "Kontakt": "/about"}


def main_page(request):
    title = "H2Sunbelt"
    data = {"menu": MENU, "title": title}
    return render(request, "./index.html", context=data)


def goal_page(request):
    title = "Unser Ziel"
    data = {"menu": MENU, "title": title}
    return render(request, "./goal.html", context=data)


def about_page(request):
    title = "Kontakt"
    data = {"menu": MENU, "title": title}
    return render(request, "./about.html", context=data)
