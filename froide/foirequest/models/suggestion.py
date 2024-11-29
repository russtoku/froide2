from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from froide.publicbody.models import PublicBody

from .request import FoiRequest


class PublicBodySuggestion(models.Model):
    request = models.ForeignKey(
        FoiRequest,
        verbose_name=_("Freedom of Information Request"),
        on_delete=models.CASCADE,
    )
    public_body = models.ForeignKey(
        PublicBody, verbose_name=_("Public Agency"), on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("User"),
    )
    timestamp = models.DateTimeField(_("Timestamp of Suggestion"), auto_now_add=True)
    reason = models.TextField(
        _("Reason this Public Agency fits the request"), blank=True, default=""
    )

    class Meta:
        get_latest_by = "timestamp"
        ordering = ("timestamp",)
        verbose_name = _("Public Agency Suggestion")
        verbose_name_plural = _("Public Agency Suggestions")
