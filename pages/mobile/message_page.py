#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.mobile.regions.message import Message


class MesssagePage(Message):

    _dashbord_locator = (By.CSS_SELECTOR, "#message-header>a")
    _message_data_locator = (By.ID, "message")
    _translate_message_locator = (By.CSS_SELECTOR, '.options ul li:nth-child(2) a')
    _tweet_this_locator = (By.CSS_SELECTOR, '.options .twitter')

    def __init__(self, testsetup):
        element = testsetup.selenium.find_element(*self._message_data_locator)
        Message.__init__(self, testsetup, element)

    def click_dashbord(self):
        self.selenium.find_element(*self._dashbord_locator).click()
        from pages.mobile.feedback import FeedbackPage
        return FeedbackPage(self.testsetup)

    def click_platform(self):
        self._root_element.find_element(*self._platform_locator).click()

    def click_locale(self):
        self._root_element.find_element(*self._locale_locator).click()

    def click_timestamp(self):
        self._root_element.find_element(*self._time_locator).click()
