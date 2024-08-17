from django.shortcuts import render
from django.http import HttpResponse
import markdown2
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,title):
    content = util.get_entry(title);
    if content == None:
        return render(request,"encyclopedia/error.html", {
            "error_message" : "requested page was not found"    
        })
    else :    
        return render(request,"encyclopedia/entry.html", {
            "title" : title,
            "entry" : markdown2.markdown(util.get_entry(title))
        })

def search(request):
    if request.method == "POST" :
        search_content = request.POST['q']
        page_content = util.get_entry(search_content)
        if page_content is not None:
            return   render(request,"encyclopedia/entry.html", {
                "title" : search_content,
                "entry" : markdown2.markdown(page_content)             
            })
        else :
            all_entries = util.list_entries()
            search_list = []
            for entry in all_entries:
                if search_content.lower() in entry.lower():
                    search_list.append(entry)  
            if len(search_list) != 0:
                return render(request,"encyclopedia/search.html", {
                    "entries": search_list,
                    "search_content" : search_content
                })
            else :
                return render(request,"encyclopedia/search.html",{
                    "entries" : None,
                    "search_content" : search_content
                })

def createPage(request):
    return render(request, "encyclopedia/createPage.html")

def savePage(request):
    if request.method == "POST":
        title_content = request.POST['title']
        entry = util.get_entry(title_content)
        if entry is not None:
            return render(request,"encyclopedia/pageError.html",
            {
            "title" : title_content    
            })
        else :
            entry_content = request.POST['content']
            util.save_entry(title_content,entry_content)
            return   render(request,"encyclopedia/entry.html",
                {
                "title" : title_content,
                "entry" : markdown2.markdown(entry_content)             
                }) 

def edit(request,title):
    return render(request, "encyclopedia/pageEdit.html", {
        "title" : title,
        "entry_content" : util.get_entry(title)
    })                

def saveEdits(request):
    if request.method == "POST":
        entry_content = request.POST['entry_content']
        entry_title = request.POST['title']
        util.save_entry(entry_title, entry_content)
        return render(request,"encyclopedia/entry.html", {
            "title" : entry_title,
            "entry" : markdown2.markdown(entry_content)
        })

def randomPage(request):
    all_entries = util.list_entries()
    random_entry = random.choice(all_entries)
    return render(request,"encyclopedia/entry.html", {
            "title" : random_entry,
            "entry" : markdown2.markdown(util.get_entry(random_entry))
        })