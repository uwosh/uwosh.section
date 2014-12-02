# -*- coding: utf-8 -*-
#
# File: setuphandlers.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


import logging
logger = logging.getLogger('uwosh.section: setuphandlers')
from uwosh.section.config import PROJECTNAME
from uwosh.section.config import DEPENDENCIES
import os
from Products.CMFCore.utils import getToolByName
import transaction
##code-section HEAD
##/code-section HEAD
from Products.CMFEditions.setuphandlers import DEFAULT_POLICIES

def isNotuwoshsectionProfile(context):
    return context.readDataFile("uwoshsection_marker.txt") is None



def updateRoleMappings(context):
    """after workflow changed update the roles mapping. this is like pressing
    the button 'Update Security Setting' and portal_workflow"""
    if isNotuwoshsectionProfile(context): return 
    wft = getToolByName(context.getSite(), 'portal_workflow')
    wft.updateRoleMappings()

def postInstall(context):
    """Called as at the end of the setup process. """
    # the right place for your custom code
    if isNotuwoshsectionProfile(context): return
    site = context.getSite()
    # add Section to versionable types
    type_id = u'Section'
    portal_repository = site.portal_repository
    versionable_types = list(portal_repository.getVersionableContentTypes())
    if type_id not in versionable_types:
        versionable_types.append(type_id)
        # Add default versioning policies to the versioned type
        for policy_id in DEFAULT_POLICIES:
            portal_repository.addPolicyForContentType(type_id, policy_id)
        portal_repository.setVersionableContentTypes(versionable_types)

##code-section FOOT
##/code-section FOOT
