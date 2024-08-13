# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.db.models import ProtectedError

from django.urls import reverse, reverse_lazy
from django.views import generic

from . import models

# Create your views here.

# def author_list(request):
#     authors = models.Author.objects.all()
#     context = {
#         'objects_list': authors,
#         'page_title': "Author list"
#     }
#     return render(request, template_name="author-list.html", context=context)
    # html = "<a href=\"/author-create/\">Create  new</a> <br><table border = \"2 \"> <tr><td>id</td><td>name</td><td>-----</td><td>-----</td></tr>"
    # for author in authors:
    #     html += f"""
    #     <tr>
    #         <td>{author.id}</td>
    #         <td>{author.name}</td>
    #         <td><a href=\"/author-detail/{author.id}\">view</a>  || <td><a href=\"/author-update/{author.id}\">update</a>
    #     </td></tr>"""
    # html += "</table>"
    # return HttpResponse(html)

class AuthorList(generic.ListView):
    model = models.Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Author list"
        return context
    

class AuthorDetail(generic.DetailView):
    model = models.Author

class AuthorCreate(generic.CreateView):
    model = models.Author
    fields = ['name', 'description']

class AuthorUpdate(generic.UpdateView):
    model = models.Author
    fields = ['name', 'description']

class AuthorDelete(generic.DeleteView):
    model = models.Author
    success_url = reverse_lazy("references:author-list")
    
    # def delete(self, request, *args, **kwargs):
    #     try:
    #         return super().delete(request, *args, **kwargs)
    #     except ProtectedError:
    #         messages.error(request, "Deletion is not possible because there are related objects!")
    #         return redirect("references:author-detail", pk=self.get_object().pk)
            
              

# from django.shortcuts import get_object_or_404, redirect
# from django.contrib import messages
# from django.db.models import ProtectedError
#     def delete_author(request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         try:
#             author.delete()
#             messages.success(request, "The author was successfully deleted!")
#         except ProtectedError:
#             messages.error(request, "Deletion is not possible because there are related objects!")
#             return redirect("references:author-detail", pk=pk)
#         return redirect("references:author-list")


# def author_detail(request, author_id):
#     # pk = ???
#     # GET http://127.0.0.1:8000/author-detail/?author_id=2&abc=12
#     # author_id = request.GET.get("author_id")
#     # URL http://127.0.0.1:8000/author-detail/2/
#     # POST http://127.0.0.1:8000/author-detail  (web-form)
#     # author_id = request.GET.get("author_id")
#     # author = models.Author.objects.get(pk=author_id)
#     # html = f"<h1> Author Detail</h1> <br>{author.pk} {author.name}<br>"
#     # series = author.series.all()
#     # if series:
#     #     html += "Series of Author: <ul>"
#     #     for serie in series:
#     #         html += f"<li> total number {serie.total_number}, title {serie.name}</Li>"
#     #     html += "</ul>"
#     # return HttpResponse(html)
#     author = models.Author.objects.get(pk=author_id)
#     context = {
#         'obj': author,
#         'page_title': f"Author detail #{author_id}"
#     }
#     return render(request, template_name="author-detail.html", context=context)

# @csrf_exempt
# def author_create(request):
#     # GET get inform
#     # POST create 1 object
#     # UPDATE (what)
#     # PATCH (what)
#     # DELETE (what)
#     # HEAD
#     if request.method == "GET":
#         html = """
#         <form method="post">
#         <input name="name"> <br>
#         <textarea name="description"> </textarea> <br>
#         <button type="submit">Save</button>
#         </form>
#         """
#         return HttpResponse(html)
#     if request.method == "POST":
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         new_author = models.Author.objects.create(name=name, description=description)
#         # /author-detail/id/
#         return HttpResponseRedirect(reverse_lazy("references:author-detail", kwargs={"author_id":new_author.id}))

# @csrf_exempt
# def author_update(request, author_id):
#     if request.method == "GET":
#         author = models.Author.objects.get(pk=author_id)
#         html = f"""
#         <form method="post">
#         <input name="name" value={author.name}> <br>
#         <textarea name="description">{author.description}</textarea> <br>
#         <button type="submit">Save</button>
#         </form>
#         """
#         return HttpResponse(html)
#     if request.method == "POST":
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         # author = models.Author.objects.get(pk=author_id)
#         # author.name = name
#         # author.description = description
#         # author.save()
#         author = models.Author.objects.filter(pk=author_id).update(
#             name=name,
#             description=description 
#         )
#         return HttpResponseRedirect(reverse_lazy("references:author-detail", kwargs={"author_id":author_id}))
    
# def series_list(request):
#     series = models.Serie.objects.all()
#     context = {
#     'objects_list': series,
#     'page_title': "Series list"
#     }
#     return render(request, template_name="series-list.html", context=context)

class GenreList(generic.ListView):
    model = models.Genre

class GenreDetail(generic.DetailView):
    model = models.Genre  

class GenreCreate(generic.CreateView):
    model = models.Genre
    fields = ['name', 'description']

class GenreUpdate(generic.UpdateView):
    model = models.Genre
    fields = ['name', 'description']

class GenreDelete(generic.DeleteView):
    model = models.Genre
    success_url = reverse_lazy("references:genre-list")

# def genre_detail(request, genre_id):
#     genre = models.Genre.objects.get(pk=genre_id)
#     context = {
#         'obj': genre,
#         'page_title': f"Genre detail #{genre_id}"
#     }
#     return render(
#         request, 
#         template_name="genre-detail.html", 
#         context=context
#         )

class PublishingList(generic.ListView):
    model = models.Publishing

class PublishingDetail(generic.DetailView):
    model = models.Publishing

class PublishingCreate(generic.CreateView):
    model = models.Publishing
    fields = ['name', 'description']

class PublishingUpdate(generic.UpdateView):
    model = models.Publishing
    fields = ['name', 'description']

class PublishingDelete(generic.DeleteView):
    model = models.Publishing
    success_url = reverse_lazy("references:publishing-list")

# def publishing_detail(request, publishing_id):
#     publishing = models.Publishing.objects.get(pk=publishing_id)
#     context = {
#         'obj': publishing,
#         'page_title': f"Publishing detail #{publishing_id}"
#     }
#     return render(
#         request, 
#         template_name="publishing-detail.html", 
#         context=context
#         )

class SeriesList(generic.ListView):
    model = models.Serie
    # context_object_name = 'series'

class SeriesDetail(generic.DetailView):
    model = models.Serie

class SeriesCreate(generic.CreateView):
    model = models.Serie
    fields = ['author', 'name', 'total_number', 'description']
    # url = "/series-list/"

class SeriesUpdate(generic.UpdateView):
    model = models.Serie
    fields = ['author', 'name', 'total_number', 'description']

class SeriesDelete(generic.DeleteView):
    model = models.Serie
    success_url = reverse_lazy("references:series-list")   

# def seriesprivately_detail(request, seriesprivately_id):
#     seriesprivately = models.SeriesPrivately.objects.get(pk=seriesprivately_id)
#     context = {
#         'obj': seriesprivately,
#         'page_title': f"Seriesprivately detail #{seriesprivately_id}"
#     }
#     return render(
#         request, 
#         template_name="seriesprivately-detail.html", 
#         context=context
#         )

class SeriesPrivatelyList(generic.ListView):
    model = models.SeriesPrivately
   
class SeriesPrivatelyDetail(generic.DetailView):
    model = models.SeriesPrivately

class SeriesPrivatelyCreate(generic.CreateView):
    model = models.SeriesPrivately
    fields = ['book_number', 'book_name', 'series_name', 'description']
   
class SeriesPrivatelyUpdate(generic.UpdateView):
    model = models.SeriesPrivately
    fields = ['book_number', 'book_name', 'series_name', 'description']

class SeriesPrivatelyDelete(generic.DeleteView):
    model = models.SeriesPrivately
    success_url = reverse_lazy("references:seriesprivately-list")

# def series_detail(request, serie_id):
#     serie = models.Serie.objects.get(pk=serie_id)
#     context = {
#         'obj': serie,
#         'page_title': f"Series detail #{serie_id}"
#     }
#     return render(
#         request, 
#         template_name="series-detail.html", 
#         context=context
#         )
    # serie_id = request.GET.get("serie_id")
    # serie = models.Serie.objects.get(pk=serie_id)
    # html = f"""<h1> Series Detail</h1> 
    # <br>{serie.pk} {serie.name}
    # <br> <a href=\"/author-detail/?author_id={serie.author.id}\">{serie.author.name}</a>{serie.author.description}
    # <br>{serie.description}"""
    # return HttpResponse(html)


# def series_create(request):
#     if request.method == "GET":
#         authors = models.Author.objects.all()
#         context = {
#             'authors': authors,
#             'page_title': f"Series create"
#             }
#         return render(
#         request, 
#         template_name="series-create.html", 
#         context=context
#         )
#     if request.method == "POST":
#         author_id = request.POST.get("author")
#         author = models.Author.objects.get(pk=author_id)
#         name = request.POST.get("name")
#         total_number = request.POST.get("total_number")
#         description = request.POST.get("description")
#         new_serie = models.Serie.objects.create(
#             author = author,
#             name = name,
#             total_number = total_number,
#             description = description
#         )
#         print(new_serie)
#         return HttpResponseRedirect(reverse_lazy("references:series-detail", kwargs={"serie_id":new_serie.id}))
    
    
    #     name = request.POST.get('name')
    #     description = request.POST.get('description')
    #     new_author = models.Author.objects.create(name=name, description=description)
    #     # /author-detail/id/
    #     return HttpResponseRedirect(f"/author-detail/{new_author.id}/")
    # context = {
    #     'obj': serie,
    #     'page_title': f"Series detail #{serie_id}"
    # }
    # return render(request, template_name="series-detail.html", context=context)