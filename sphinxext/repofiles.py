# -*- coding: utf-8 -*-
"""
Autorun directives with ``working/$WORK_DIR`` as the default directory
Autorun directives with ``working/repos/$WORK_DIR`` as the default directory
"""

from autorun import RunCommit
from workrun import WorkRun, WorkVar, OBJECTS_INC
from writefile import WriteFile

WORK_DIR='our_work'


class RepoRun(WorkRun):
    default_cwd = '/working/' + WORK_DIR


class RepoWrite(WriteFile):
    default_cwd = '/working/' + WORK_DIR


class RepoCommit(RunCommit):
    default_links_file = OBJECTS_INC
    default_home = '/working'
    default_cwd = '/working/' + WORK_DIR


class RepoVar(WorkVar):
    default_cwd = '/working/' + WORK_DIR


class RepoOut(RepoRun):
    """ For displaying output only, with no highlighting
    """
    opt_defaults = {'highlighter': 'none', 'hide-code': True}


def setup(app):
    app.add_directive('reporun', RepoRun)
    app.add_directive('repocommit', RepoCommit)
    app.add_directive('repovar', RepoVar)
    app.add_directive('repoout', RepoOut)
    app.add_directive('repowrite', RepoWrite)

# vim: set expandtab shiftwidth=4 softtabstop=4 :
