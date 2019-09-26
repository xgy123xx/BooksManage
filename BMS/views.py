
# Create your views here.
from django.shortcuts import render,HttpResponse,reverse,redirect
from BMS.models import *

def index(request):
    book_list = Book.objects.all()
    return render(request,"index.html",{"book_list":book_list})

def register(request):
    if request.method == "POST":
        bookInfo=request.POST
        Book.objects.create(title=bookInfo["title"],author=bookInfo["author"],publishDate=bookInfo["publishDate"],
                            publish=bookInfo["publish"],price=bookInfo["price"])
        return redirect("/index/")
    else:
        return render(request,"register.html")

def delbook(request,id):
    Book.objects.filter(nid=id).delete()
    return redirect("/index/")

def editbook(request,id):
    book_obj = Book.objects.filter(nid=id).first()
    if request.method == "POST":
        bookInfo=request.POST
        Book.objects.filter(nid=id).update(title=bookInfo["title"],author=bookInfo["author"],publishDate=bookInfo["publishDate"],
                            publish=bookInfo["publish"],price=bookInfo["price"])
        return redirect("/index/")
    else:
        return render(request,"edit.html",{"book" : book_obj})

def showAuthor(request,id):
    #通过id找到作者，通过作者找到相应的书籍
    authorName = Book.objects.filter(nid=id).first().author
    book_list = Book.objects.filter(author=authorName)
    return render(request,"author.html",{"book_list" : book_list})

def showPublish(request,id):
    #通过id找到作者，通过作者找到相应的书籍
    publishName = Book.objects.filter(nid=id).first().publish
    book_list = Book.objects.filter(publish=publishName)
    return render(request,"publish.html",{"book_list" : book_list})

def eatjj(request):

    return render(request, "home.html")