#!/usr/bin/python3
"""
"""

from collections import OrderedDict

from django.shortcuts import render

from .forms import (
    UnitSelectForm,
)
from .models import (
    LyndisLeague,
    FireEmblemGenealogy,
    DragonsGate,
)
import aenir.morph


class StatCompareViews:
    """
    """

    # for use in creating Morphs
    QUINTESSENCE = OrderedDict()

    # for use in Morph methods
    datadir_root = "./stat_compare/static/stat_compare/data/"

    # for use in rendering the web page
    about_unit = {}
    unit_history = {}

    @classmethod
    def index(cls, request):
        """
        Contains a compendium of links to the application to access.
        """
        context = {"view_name": ""}
        return render(request, "stat_compare/index.html", context=context)

    @classmethod
    def create(cls, request):
        """
        """
        context = {
                "view_name": "Create",
                "form": UnitSelectForm(),
                }
        return render(request, "stat_compare/create.html", context=context)

    @classmethod
    def edit(cls, request):
        """
        """
        context = {"view_name": "Edit"}
        return render(request, "stat_compare/edit.html", context=context)

    @classmethod
    def compare(cls, request):
        """
        """
        context = {"view_name": "Compare"}
        return render(request, "stat_compare/compare.html", context=context)
