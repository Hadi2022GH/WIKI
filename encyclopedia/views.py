import random
from html import entities
from django.shortcuts import render
from markdown2 import Markdown

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Markdown to HTML Conversion 
def convert(title):
    md = util.get_entry(title)
    markdowner = Markdown()
    if md == None:
        return None
    else:
        return markdowner.convert(md)

# Entry Page: Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry,
#             should render a page that displays the contents of that encyclopedia entry.
def entry(request, title):
    html_entry = convert(title)
    if html_entry == None:
        return render(request, "encyclopedia/error.html", {
            "error_massage" : "Requested page was not found"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title" : title,
            "HTML" : html_entry,
        })

# Search: Allow the user to type a query into the search box in the sidebar
#         to search for an encyclopedia entry.
def search(request):
    if request.method == "POST":
        search_q = request.POST["q"]
        html_entry = convert(search_q)
        # If the query does not match the name of an encyclopedia entry,
        #    the user should instead be taken to a search results page that displays
        #    a list of all encyclopedia entries that have the query as a substring
        if html_entry == None:
            list_entries = util.list_entries()
            suggestions = []
            for entry in list_entries:
                if search_q.casefold() in entry.casefold():
                    suggestions.append(entry)
            len_sugg = len(suggestions)
            return render(request, "encyclopedia/search.html", {
                "suggestions" : suggestions,
                "len_sugg" : len_sugg
            })
        else:
            return render(request, "encyclopedia/entry.html", {
            "title" : search_q,
            "HTML" : html_entry,
            })

# New Page: Clicking “Create New Page” in the sidebar should take the user
#          to a page where they can create a new encyclopedia entry.
def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        title_Repetitious = util.get_entry(title)
        # When the page is saved, if an encyclopedia entry already exists with the provided title,
        #     the user should be presented with an error message.
        if title_Repetitious is not None:
            return render(request, "encyclopedia/error.html", {
                "error_massage" : "an entry already exists with the provided title"
            })
        else:
            util.save_entry(title, content)
            html_entry = convert(title)
            return render(request, "encyclopedia/entry.html", {
                "title" : title,
                "HTML" : html_entry,
            })

# Edit Page: On each entry page, the user should be able to click a link to be
#   taken to a page where the user can edit that entry’s Markdown content in a textarea.
def edit_page(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title" : title,
            "content" : content,
        })

# The user should be able to click a button to save the changes made to the entry.
def save(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_entry = convert(title)
        return render(request, "encyclopedia/entry.html", {
            "title" : title,
            "HTML" : html_entry,
        })

# Random Page: Clicking “Random Page” in the
#  sidebar should take user to a random encyclopedia entry.
def random_entry(request):
    list_entry = util.list_entries()
    rand = random.choice(list_entry)
    html_entry = convert(rand)
    return render(request, "encyclopedia/entry.html", {
    "title" : rand,
    "HTML" : html_entry,
        })

