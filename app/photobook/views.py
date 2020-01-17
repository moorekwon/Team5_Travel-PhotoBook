from django.shortcuts import render, redirect

from members.models import User
from photobook.models import PhotoBook, Page, Photo


def page_create(request, photobook_pk):
    photobook = PhotoBook.objects.get(pk=photobook_pk)
    Page.objects.create(
        book=photobook
    )
    return render(request, 'page_1.html')


def add_photo(request, page_pk, photo_num):
    page = Page.objects.get(pk=page_pk)
    pass
    # if request.method =='POST':
    # for i in photo_num:
    #     Photo.objects.create(
    #         photo_page=page,
    #     )


def index(request):
    return render(request, 'index.html')


def album_create(request):
    author = request.user
    PhotoBook.objects.create(
        author=author,
    )
    return redirect('page_1')
