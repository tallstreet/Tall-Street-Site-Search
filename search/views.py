# -*- coding: utf-8 -*-
from django.views.decorators.cache import cache_page
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader, Context
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound, HttpResponseForbidden

from django.views.generic.list_detail import object_list, object_detail
from whoosh.index import getdatastoreindex
from whoosh.qparser import QueryParser, MultifieldParser
from django.utils.translation import ugettext_lazy as _
import urllib
from search.models import Page, SEARCHSCHEMA

#@cache_page(60 * 60 * 24)
def index(request):
    t = loader.get_template("index.html")
    c = RequestContext(request, {
    })
    return HttpResponse(t.render(c))
   
def update_last_updated(request):
    Pages = Page.all().order('update_time').fetch(100)
    for Page in Pages:
        Page.put()
        logging.info("Updated %s" % (Page.searchter_id))
    return TextResponse("Success, Finished!")

#@cache_page(60 * 60 * 5)
def search(request):
    ix = getdatastoreindex("search", schema=SEARCHSCHEMA)
    if request.GET.has_key("query"):
        ix = getdatastoreindex("search", schema=SEARCHSCHEMA)
        parser = MultifieldParser(["title", "description", "keywords", "page"], schema = ix.schema)
        query = parser.parse(request.GET['query'])
        title = "Search Results  - %s" % request.GET['query']
        results = ix.searcher().search(query)
        results.model = Page
        return object_list(request, results, paginate_by=100, extra_context={'object_list': results, 'title': title, 'query': request.GET['query']})
    else:
        return HttpResponseRedirect(reverse("search.index"))

def show_id(request, key):
    return object_detail(request, Page.all(), key)
