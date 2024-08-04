from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt

from . import models

# Create your views here.

def author_list(request):
    authors = models.Author.objects.all()
    html = "<a href=\"/author-create/\">Create  new</a> <br><table border = \"2 \"> <tr><td>id</td><td>name</td><td>-----</td><td>-----</td></tr>"
    for author in authors:
        html += f"""
        <tr>
            <td>{author.id}</td>
            <td>{author.name}</td>
            <td><a href=\"/author-detail/{author.id}\">view</a>  || <td><a href=\"/author-update/{author.id}\">update</a>
        </td></tr>"""
    html += "</table>"
    return HttpResponse(html)

def author_detail(request, author_id):
    # pk = ???
    # GET http://127.0.0.1:8000/author-detail/?author_id=2&abc=12
    # author_id = request.GET.get("author_id")
    # URL http://127.0.0.1:8000/author-detail/2/
    # POST http://127.0.0.1:8000/author-detail  (web-form)
    # author_id = request.GET.get("author_id")
    # author = models.Author.objects.get(pk=author_id)
    # html = f"<h1> Author Detail</h1> <br>{author.pk} {author.name}<br>"
    # series = author.series.all()
    # if series:
    #     html += "Series of Author: <ul>"
    #     for serie in series:
    #         html += f"<li> total number {serie.total_number}, title {serie.name}</Li>"
    #     html += "</ul>"
    # return HttpResponse(html)
    author = models.Author.objects.get(pk=author_id)
    context = {
        'obj': author,
        'page_title': f"Author detail #{author_id}"
    }
    return render(request, template_name="author-detail.html", context=context)

@csrf_exempt
def author_create(request):
    # GET get inform
    # POST create 1 object
    # UPDATE (what)
    # PATCH (what)
    # DELETE (what)
    # HEAD
    if request.method == "GET":
        html = """
        <form method="post">
        <input name="name"> <br>
        <textarea name="description"> </textarea> <br>
        <button type="submit">Save</button>
        </form>
        """
        return HttpResponse(html)
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        new_author = models.Author.objects.create(name=name, description=description)
        # /author-detail/id/
        return HttpResponseRedirect(f"/author-detail/{new_author.id}/")

@csrf_exempt
def author_update(request, author_id):
    if request.method == "GET":
        author = models.Author.objects.get(pk=author_id)
        html = f"""
        <form method="post">
        <input name="name" value={author.name}> <br>
        <textarea name="description">{author.description}</textarea> <br>
        <button type="submit">Save</button>
        </form>
        """
        return HttpResponse(html)
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        # author = models.Author.objects.get(pk=author_id)
        # author.name = name
        # author.description = description
        # author.save()
        author = models.Author.objects.filter(pk=author_id).update(
            name=name,
            description=description 
        )
        return HttpResponseRedirect(f"/author-detail/{author_id}/")
    
def series_list(request):
    series = models.Serie.objects.all()
    context = {
        'objects_list': series,
        'page_title': "Series list"
    }
    return render(request, template_name="series-list.html", context=context)
 # html = "<table border = \"2 \"> <tr><td>id</td><td>name</td><td>-----</td></tr>"
    # for serie in series:
    #     html += f"<tr><td>{serie.id}</td><td>{serie.name}</td><td><a href=\"/series-detail/?serie_id={serie.id}\">view</a></td></tr>"
    # html += "</table>"
    # MVT (MVC)
    # ORM -> SQLAlchemy
    # TE (template engine) -> Jinja

def series_detail(request, serie_id):
    serie = models.Serie.objects.get(pk=serie_id)
    context = {
        'obj': serie,
        'page_title': f"Series detail #{serie_id}"
    }
    return render(
        request, 
        template_name="series-detail.html", 
        context=context
        )
    # serie_id = request.GET.get("serie_id")
    # serie = models.Serie.objects.get(pk=serie_id)
    # html = f"""<h1> Series Detail</h1> 
    # <br>{serie.pk} {serie.name}
    # <br> <a href=\"/author-detail/?author_id={serie.author.id}\">{serie.author.name}</a>{serie.author.description}
    # <br>{serie.description}"""
    # return HttpResponse(html)


def series_create(request):
    if request.method == "GET":
        authors = models.Author.objects.all()
        context = {
            'authors': authors,
            'page_title': f"Series create"
            }
        return render(
        request, 
        template_name="series-create.html", 
        context=context
        )
    if request.method == "POST":
        author_id = request.POST.get("author")
        author = models.Author.objects.get(pk=author_id)
        name = request.POST.get("name")
        total_number = request.POST.get("total_number")
        description = request.POST.get("description")
        new_serie = models.Serie.objects.create(
            author = author,
            name = name,
            total_number = total_number,
            description = description
        )
        print(new_serie)
        return HttpResponseRedirect(f"/series-detail/{new_serie.id}/")
    
    
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