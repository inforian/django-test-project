"""
"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class HangryPerson(models.Model):
    """
    """

    first_name = models.CharField(_("Person First Name"), max_length=40)
    last_name =  models.CharField(_("Person Last Name"), max_length=40)
    email = models.EmailField(_("Person Email"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified at"), auto_now=True)

    class Meta:
        verbose_name_plural = "Hangry Persons"

    def __str__(self):
        return f"ID : ({self.id}) || NAME : ({self.first_name} {self.last_name})"