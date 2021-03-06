"""
Copyright (c) 2016-17 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import logging

from programy.config.base import BaseConfigurationData

class BotSpellingConfiguration(BaseConfigurationData):

    def __init__(self):
        BaseConfigurationData.__init__(self, name="spelling")
        self._classname = None
        self._corpus = None
        self._alphabet = None
        self._check_before = False
        self._check_and_retry = False

    @property
    def classname(self):
        return self._classname

    @property
    def corpus(self):
        return self._corpus

    @property
    def alphabet(self):
        return self._alphabet

    @property
    def check_before(self):
        return self._check_before

    @property
    def check_and_retry(self):
        return self._check_and_retry

    def load_config_section(self, file_config, bot_config, bot_root):
        spelling = file_config.get_section("spelling", bot_config)
        if spelling is not None:
            self._classname = file_config.get_option(spelling, "classname", missing_value=None)
            self._alphabet = file_config.get_option(spelling, "alphabet", missing_value=None)
            corpus = file_config.get_option(spelling, "corpus", missing_value=None)
            self._corpus = self.sub_bot_root(corpus, bot_root)
            self._check_before = file_config.get_bool_option(spelling, "check_before", missing_value=False)
            self._check_and_retry = file_config.get_option(spelling, "check_and_retry", missing_value=False)
        else:
            logging.warning("'spelling' section missing from bot config, using to defaults")