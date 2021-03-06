from django.utils.translation import ugettext_lazy as _
from google.appengine.ext import db
from ragendja.auth.models import EmailUserTraits

class User(EmailUserTraits):
    """User class that provides support for Django and Google Accounts."""
    user = db.UserProperty()
    username = db.StringProperty(required=True, verbose_name=_('username'))
    email = db.EmailProperty(verbose_name=_('e-mail address'))
    first_name = db.StringProperty(verbose_name=_('first name'))
    last_name = db.StringProperty(verbose_name=_('last name'))

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    @classmethod
    def create_djangouser_for_user(cls, user):
        return cls(user=user, email=user.email(), username=user.email())
