# Copyright (c) 2014 Dark Secret Software Inc.
# Copyright (c) 2015 Rackspace
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import decimal
import unittest

import dateutil.tz

import notification_utils


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.handler = notification_utils.DateTimeEncoder()

    def test_handle_datetime_non_datetime(self):
        self.assertRaises(TypeError, self.handler.default, "text")

    def test_handle_datetime(self):
        now = datetime.datetime(day=1, month=2, year=2014,
                                hour=10, minute=11, second=12)
        self.assertEqual("1391249472", self.handler.default(now))

    def test_handle_datetime_offset(self):
        now = datetime.datetime(day=1, month=2, year=2014,
                                hour=10, minute=11, second=12,
                                tzinfo=dateutil.tz.tzoffset(None, 4 * 60 * 60))
        self.assertEqual("1391220672", self.handler.default(now))


class TestDatetimeToDecimal(unittest.TestCase):
    def test_datetime_to_decimal(self):
        expected_decimal = decimal.Decimal('1356093296.123')
        utc_datetime = datetime.datetime.utcfromtimestamp(expected_decimal)
        actual_decimal = notification_utils.dt_to_decimal(utc_datetime)
        self.assertEqual(actual_decimal, expected_decimal)

    def test_decimal_to_datetime(self):
        expected_decimal = decimal.Decimal('1356093296.123')
        expected_datetime = datetime.datetime.utcfromtimestamp(
            expected_decimal)
        actual_datetime = notification_utils.dt_from_decimal(expected_decimal)
        self.assertEqual(actual_datetime, expected_datetime)

    def test_dt_from_decimal_none(self):
        self.assertEqual("n/a", notification_utils.dt_from_decimal(None))
