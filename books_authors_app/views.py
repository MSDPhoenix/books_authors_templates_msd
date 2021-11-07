from django.shortcuts import render,redirect
from .models import *

def books_page(request):
    context = {
        "books" : Book.objects.all()
    }
    return render(request,'add_book.html',context)

def add_book(request):
    new_title=request.POST["title"]
    description=request.POST["description"]
    Book.objects.create(title=new_title,desc=description)
    return redirect('/')

def view_book(request,book_id):
    authors_left=[]
    book=Book.objects.get(id=book_id)
    for author in Author.objects.all():
        if book not in author.books.all():
            authors_left.append(author)
    context = {
        "book":Book.objects.get(id=book_id),
        "authors_left":authors_left,
    }
    return render(request,'view_book.html',context)

def delete_book(request,book_id):
    book=Book.objects.get(id=book_id)
    book.delete()
    return redirect('/')

def authors_page(request):
    context = {
        "authors":Author.objects.all()
    }
    return render(request,'authors_page.html',context)

def add_author(request):
    fname=request.POST["first_name"]
    lname=request.POST["last_name"]
    note_s=request.POST["notes"]
    Author.objects.create(first_name=fname,last_name=lname,notes=note_s)
    return redirect('/authors')

def view_author(request,author_id):
    books_left=[]
    author=Author.objects.get(id=author_id)
    for book in Book.objects.all():
        if author not in book.authors.all():
            books_left.append(book)
    context = {
        "author":Author.objects.get(id=author_id),
        "books_left":books_left,
    }
    return render(request,'view_author.html',context)

def delete_author(request,author_id):
    author=Author.objects.get(id=author_id)
    author.delete()
    return redirect('/authors')

def add_book_to_author(request,author_id):
    if request.POST['book_to_add_to_author'] !="0":
        author=Author.objects.get(id=author_id)
        this_book=Book.objects.get(id=request.POST['book_to_add_to_author'])
        author.books.add(this_book)
    return redirect('/view_author/'+str(author_id))

def remove_book_from_author(request,book_id,author_id):
    author=Author.objects.get(id=author_id)
    this_book=Book.objects.get(id=book_id)
    author.books.remove(this_book)
    return redirect('/view_author/'+str(author_id))

def add_author_to_book(request,book_id):
    if request.POST['author_to_add_to_book'] !="0":
        book=Book.objects.get(id=book_id)
        author=Author.objects.get(id=request.POST['author_to_add_to_book'])
        book.authors.add(author)
    return redirect('/view_book/'+str(book_id))

def remove_author_from_book(request,book_id,author_id):
    author=Author.objects.get(id=author_id)
    book=Book.objects.get(id=book_id)
    book.authors.remove(author)
    return redirect('/view_book/'+str(book_id))

def update_book(request,book_id):
    authors_left=[]
    book=Book.objects.get(id=book_id)
    for author in Author.objects.all():
        if book not in author.books.all():
            authors_left.append(author)
    context = {
        "book":Book.objects.get(id=book_id),
        "authors_left":authors_left,
    }
    return render(request,'update_book.html',context)

def save_book_update(request,book_id):
    book=Book.objects.get(id=book_id)
    book.desc=request.POST['description']
    book.save()
    return redirect('/view_book/'+str(book_id))

def update_author(request,author_id):
    books_left=[]
    author=Author.objects.get(id=author_id)
    for book in Book.objects.all():
        if author not in book.authors.all():
            books_left.append(book)
    context = {
        "author":Author.objects.get(id=author_id),
        "books_left":books_left,
    }
    return render(request,'update_author.html',context)

def save_author_update(request,author_id):
    author=Author.objects.get(id=author_id)
    author.notes=request.POST['notes']
    author.save()
    return redirect('/view_author/'+str(author_id))

