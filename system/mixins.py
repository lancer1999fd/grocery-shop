from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

from system.models import SocialUser


class LegalRequirementMixin:
    def dispatch(self, request, *args, **kwargs):

        if not request.user.legaluser.privacy:
            return redirect("privacy")

        if not request.user.legaluser.disclaimer:
            return redirect("disclaimer")

        if not request.user.legaluser.terms:
            return redirect("terms")

        return super().dispatch(request, *args, **kwargs)


class BlockedUserRedirectMixin:
    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        user_social, created = SocialUser.objects.get_or_create(user=user)

        if request.user in user_social.blocked.all():
            return HttpResponseRedirect(reverse("home"))

        return super().dispatch(request, *args, **kwargs)


class AdminRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.config.role.name != "Admin":
            return HttpResponseRedirect(reverse("home"))
        return super().dispatch(request, *args, **kwargs)


class ModeratorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.config.role.name in ["Admin", "Moderator"]:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse("home"))
