# -*- coding: utf-8 -*-
#
# File: Section.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.document import ATDocument
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from uwosh.section.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Section_schema = getattr(ATFolder, 'schema', Schema(())).copy() + \
    getattr(ATDocument, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Section(ATFolder, ATDocument):
    """A combination folder/page which can contain other items and can contain rich text."""
    security = ClassSecurityInfo()

    implements(interfaces.ISection)

    meta_type = 'Section'
    _at_rename_after_creation = True

    schema = Section_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Section, PROJECTNAME)
# end of class Section

##code-section module-footer #fill in your manual code here
##/code-section module-footer



