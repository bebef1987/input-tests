#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Firefox Input.
#
# The Initial Developer of the Original Code is
# Mozilla Corp.
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Vishal
#                 David Burns
#                 Dave Hunt <dhunt@mozilla.com>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****
'''
Created on Nov 24, 2010
'''
from vars import ConnectionParameters
import input_base_page
import type_filter_region
import product_filter_region

page_load_timeout = ConnectionParameters.page_load_timeout


class ThemesPage(input_base_page.InputBasePage):

    _page_title = 'Themes :: Firefox Input'

    _themes_locator = "id('themes')//li[contains(@class, 'theme')]"

    _themes_title_locator = "xpath=//div[@id='messages']//h2[.='Common Themes']"
    
    
    _feedback_link_locator = "css=a.dashboard"
    _themes_link_locator = "css=a.themes"
    _firefox_link_locator = "link=Firefox Input Dashboard"
    _sites_link_locator = "css=a.issues"

    _product_list = ("Firefox",
                     "Mobile")

    _type_list = ("All",
                  "Praise",
                  "Issues",
                  "Ideas")
    def go_to_themes_page(self):
        self.selenium.open('/themes/')
        self.is_the_current_page

    @property
    def get_product_list(self):
        return self._product_list
    
    @property
    def get_type_list(self):
        return self._type_list

    @property
    def get_feedback_link(self):
        return self._feedback_link_locator

    @property
    def get_themes_link(self):
        return self._themes_link_locator

    @property
    def get_firefox_link(self):
        return self._firefox_link_locator

    @property
    def get_sites_link(self):
        return self._sites_link_locator

    @property
    def type_filter(self):
        return type_filter_region.TypeFilter.ButtonFilter(self.selenium)

    @property
    def product_filter(self):
        return product_filter_region.ProductFilter.ButtonFilter(self.selenium)

    @property
    def theme_count(self):
        return int(self.selenium.get_xpath_count(self._themes_locator))

    @property
    def themes(self):
        return [self.Theme(self.selenium, i + 1) for i in range(self.theme_count)]
    
    @property
    def get_messages_title(self):
        return self.selenium.get_text(self._themes_title_locator)
 
    def theme(self, index):
        return self.Theme(self.selenium, index)

    class Theme(object):

        _type_locator = " .type"
        _similar_messages_locator = " .more"

        def __init__(self, selenium, index):
            self.selenium = selenium
            self.index = index

        def absolute_locator(self, relative_locator):
            return self.root_locator + relative_locator

        @property
        def root_locator(self):
            return "css=#themes .theme:nth(%s)" % (self.index - 1)

        @property
        def type(self):
            return self.selenium.get_text(self.absolute_locator(self._type_locator))

        def click_similar_messages(self):
            self.selenium.click(self.absolute_locator(self._similar_messages_locator))
            self.selenium.wait_for_page_to_load(page_load_timeout)
