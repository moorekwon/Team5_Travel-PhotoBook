from django.http import HttpResponse
from django.shortcuts import render, redirect

from members.models import User
from photobook.models import PhotoBook, Page, Photo


def page_create(request, photobook_pk):
    photobook = PhotoBook.objects.get(pk=photobook_pk)
    page = Page.objects.create(
        book=photobook
    )
    return redirect('edit_page', page_pk=page.pk)


def edit_page(request, page_pk):
    temp = request.GET.get('temp_num')
    if temp:
        for i in range(int(temp)):
            print('asd')

        # i의 범위를 지정해서 i값에 따라 templates를 다르게 출력하면
        # return redirect() 사진 입력하는 templates을 만들면 됩니다.
    return render(request, 'edit_page.html')


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

    if request.method == 'POST':
        book_name = request.POST['book_name']
        author = request.user

        photobook = PhotoBook.objects.create(book_name=book_name, author=author)
        num = photobook.pk
        print(num)
        return redirect('page_1', photobook_pk=num)

    return render(request, 'create_photobook.html')
