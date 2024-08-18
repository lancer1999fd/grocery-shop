from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

User = get_user_model()


class LegalUser(models.Model):
    privacy = models.BooleanField(verbose_name=_("Datenschutzerklärung"), default=False)
    disclaimer = models.BooleanField(
        verbose_name=_("Haftungsausschluss"), default=False
    )
    terms = models.BooleanField(verbose_name=_("Nutzungsrichtlinien"), default=False)

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name=_("Benutzer")
    )

    def __str__(self):
        return _("Legal User: {username}").format(username=self.user.username)
