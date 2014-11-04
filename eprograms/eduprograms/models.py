from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProgramFor(models.Model):
    """
    Describe for who program is dedicated too.
    """

    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        verbose_name = _('Program For')
        verbose_name_plural = _('Programs For')

    def __unicode__(self):
        return self.name


class ProgramCategory(models.Model):
    """
    Describe category of program
    """

    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        verbose_name = _('Program Category')
        verbose_name_plural = _('Program Categories')

    def __unicode__(self):
        return self.name


class Program(models.Model):
    """
    Program details
    """

    name = models.CharField(_('Name'), max_length=255)
    program_for = models.ManyToManyField(ProgramFor)
    program_category = models.ManyToManyField(ProgramCategory)

    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')

    def __unicode__(self):
        return self.name


class ProgramChapter(models.Model):
    """
    Describe each chapter of the program
    """

    title = models.CharField(_('Title'), max_length=255)
    priority = models.PositiveSmallIntegerField(default=0)
    program = models.ForeignKey(Program)

    subtitle_1 = models.CharField(_('Subtitle'), max_length=255)
    subtext_1 = models.CharField(_('Subtext'), max_length=1000)

    class Meta:
        verbose_name = _('Chapter')
        verbose_name_plural = _('Chapters')

    def __unicode__(self):
        return self.title
