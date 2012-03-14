#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
import pytest

from pages.mobile.feedback import FeedbackPage

xfail = pytest.mark.xfail


class Test_Feedback_Layout:

    '''
    @xfail(reason="Bug 715542 - visiting the mobile site returns a 500 error")
    @pytest.mark.nondestructive
    def test_the_header_layout(self, mozwebqa):

        feedback_pg = FeedbackPage(mozwebqa)
        feedback_pg.go_to_feedback_page()

        Assert.true(feedback_pg.is_feed_visible)
        Assert.false(feedback_pg.is_statistics_visible)
        Assert.false(feedback_pg.is_settings_visible)

        feedback_pg.click_settings_tab()

        Assert.false(feedback_pg.is_feed_visible)
        Assert.false(feedback_pg.is_statistics_visible)
        Assert.true(feedback_pg.is_settings_visible)

        feedback_pg.click_statistics_tab()

        Assert.false(feedback_pg.is_feed_visible)
        Assert.true(feedback_pg.is_statistics_visible)
        Assert.false(feedback_pg.is_settings_visible)

        feedback_pg.click_feed_tab()

        Assert.true(feedback_pg.is_feed_visible)
        Assert.false(feedback_pg.is_statistics_visible)
        Assert.false(feedback_pg.is_settings_visible)
    '''

    @pytest.mark.nondestructive
    def test_feedback_data_is_the_same_on_view_feedback_page(self, mozwebqa):
        feedback_pg = FeedbackPage(mozwebqa)
        feedback_pg.go_to_feedback_page()

        for idx, mess in enumerate(feedback_pg.messages):

            messages = feedback_pg.messages
            message_data = {}
            message_data['body'] = messages[idx].body
            message_data['time'] = messages[idx].time
            message_data['type'] = messages[idx].type
            message_data['locale'] = messages[idx].locale
            message_data['platform'] = messages[idx].platform

            message_page = messages[idx].click()


            Assert.equal(message_data['body'] , message_page.body)
            Assert.equal(message_data['time'] , message_page.time)
            Assert.equal(message_data['type'] , message_page.type)
            Assert.equal(message_data['locale'] , message_page.locale)
            Assert.equal(message_data['platform'] , message_page.platform)


            feedback_pg = message_page.click_dashbord()


