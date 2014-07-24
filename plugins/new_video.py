# -*- coding: utf-8 -*-

# Copyright © 2012-2014 Roberto Alsina and others.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import unicode_literals, print_function
import codecs
import datetime
import os
import sys
import subprocess

from blinker import signal
import dateutil.tz

from nikola.plugin_categories import Command
#from nikola.plugins.command.new_page import CommandNewPage
from nikola import utils


LOGGER = utils.get_logger('new_video', utils.STDERR_HANDLER)


class CommandNewVideoPage(Command):
    """Create a new video page."""

    name = "new_video"
    doc_usage = "[options] [path]"
    doc_purpose = "create a new video page"
    cmd_options = [
        { 'name': 'title', 'short': 't', 'long': 'title', 'type': str, 'default': '', 'help': 'Page title' },
        { 'name': 'video', 'short': 'v', 'long': 'video_file', 'type': str, 'default': None, 'help': 'Path to the video file' },
        { 'name': 'content_type', 'short': 'c', 'long': 'content_type', 'type': str, 'default': 'post', 'help': 'Page or post' },
    ]

    def _execute(self, options, args):
        """Create a new video page."""
        options['is_page'] = options['content_type'] == 'page'
        options['onefile'] = False
        options['twofile'] = True
        options['content_format'] = 'markdown'
        options['edit'] = False
        options['template_name']='video.tmpl'

        p = self.site.plugin_manager.getPluginByName('new_page', 'Command').plugin_object
        LOGGER.error(locals())
        return p.execute(options, args)
