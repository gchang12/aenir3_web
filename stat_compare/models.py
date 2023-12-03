from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class FireEmblemGame(models.Model):
    game_num = models.PositiveSmallIntegerField(
        primary_key=True,
        )
    # to NOT be displayed
    game_name = models.CharField(
        unique=True,
        max_length=50,
        )
    display_gamename = models.CharField(
        unique=True,
        max_length=50,
        verbose_name="Game",
        )

    def __str__(self):
        return str(self.game_num) + ": " + self.display_gamename


class FireEmblemUnit(models.Model):
    game_num = models.ForeignKey(
        FireEmblemGame,
        on_delete=models.PROTECT,
        )
    unit_name = models.CharField(
        max_length=50,
        #verbose_name="Unit",
        )
    display_unitname = models.CharField(
        max_length=50,
        #verbose_name="Unit",
        )

    def __str__(self):
        return self.display_unitname
        #return str(self.game_num.game_num) + ": " + self.display_unitname


class UnitSelect(models.Model):
    game_num = models.ForeignKey(
        FireEmblemGame,
        on_delete=models.PROTECT,
        verbose_name="Game",
        )
    unit_name = ChainedForeignKey(
        FireEmblemUnit,
        chained_field="game_num",
        chained_model_field="game_num",
        show_all=False,
        sort=False,
        verbose_name="Unit",
        )

    def __str__(self):
        return str(self.game_num) + ": " + self.unit_name.display_unitname


# not to be used in forms and so forth

class LyndisLeague(models.Model):
    game_num = models.PositiveSmallIntegerField(
        #primary_key=True,
        )
    unit_name = models.CharField(
        max_length=50,
        primary_key=True,
        )
    display_unitname = models.CharField(
        max_length=50,
        )

    def __str__(self):
        return self.display_unitname


class FireEmblemGenealogy(models.Model):
    # Store both kids and dads here
    game_num = models.PositiveSmallIntegerField(
        )
    unit_name = models.CharField(
        primary_key=True,
        max_length=50,
        )
    display_unitname = models.CharField(
        max_length=50,
        )
    can_inherit = models.BooleanField()

    def __str__(self):
        if self.can_inherit:
            genealogy = "Child"
        else:
            genealogy = "Father"
        return genealogy + ": " + self.display_unitname
