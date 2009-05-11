# -*- coding: utf-8 -*-
from django.db.models import permalink, signals
from google.appengine.ext import db
from django.db.models.signals import post_save, pre_save, post_delete


from whoosh import store
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
from whoosh.index import getdatastoreindex
import logging
import urllib
from django.utils.translation import ugettext_lazy as _
from beautifulsoup.BeautifulSoup import BeautifulSoup

SEARCHSCHEMA = Schema(url=ID(unique=True, stored=True), title=TEXT(stored=True), description=TEXT(stored=True), keywords=KEYWORD(lowercase=True), page=TEXT())

class Page(db.Model):
    url = db.LinkProperty(verbose_name=_("URL"))
    create_time = db.DateTimeProperty(auto_now_add=True)
    update_time = db.DateTimeProperty(auto_now=True)
    change_time = db.DateTimeProperty(auto_now_add=True)
    
    def __init__(self, *args, **kw):
        kw['key_name'] = "t%s" % kw['url']
        super(Page, self).__init__(*args, **kw)

    def __unicode__(self):
        return '%s' % (self.url)
       
    @permalink
    def get_absolute_url(self):
        return ('search.views.show_id', (), {'key': self.key()})
           

def get_page(sender, instance, **kwargs):
    data = urllib.urlopen(instance.url)
    instance.page = unicode(data.read(), errors='ignore')
    soup = BeautifulSoup(instance.page)
    instance.title = soup.html.head.title.string
    desc = soup.find("meta", {"name": "description"})
    if desc:
        instance.description = desc["content"] 
    else:
        instance.description = ""
    keywords = soup.find("meta", {"name": "keywords"})
    if keywords:
        instance.keywords = keywords["content"]
    else:
        instance.keywords = ""
    
def update_search(sender, instance, **kwargs):
    ix = getdatastoreindex("search", schema=SEARCHSCHEMA)
    writer = ix.writer()
    writer.update_document(url=u"%s" % instance.url, title=instance.title, description=instance.description, keywords=instance.keywords, page=instance.page)
    writer.commit()
    
def delete_search(sender, instance, **kwargs):
    ix = getdatastoreindex("search", schema=SEARCHSCHEMA)
    ix.delete_by_term('url', u"%s" % instance.url)
    ix.commit()
    
post_save.connect(update_search, sender=Page)
pre_save.connect(get_page, sender=Page)
post_delete.connect(delete_search, sender=Page)
