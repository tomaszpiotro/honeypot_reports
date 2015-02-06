import autofixture
from django.test import TestCase
from reports.models import ReportItem


class ReportItemTest(TestCase):
    def test_not_seen_before(self):
        report_item = autofixture.create_one(
            ReportItem, field_values={'one_hour_occurrences': 0,
                                      'two_hour_occurrences': 0,
                                      'four_hour_occurrences': 0,
                                      'eight_hour_occurrences': 0,
                                      'sixteen_hour_occurrences': 0})
        print report_item.is_seen_before()
        self.assertFalse(report_item.is_seen_before())

    def test_seen_before(self):
        report_item = autofixture.create_one(
            ReportItem, field_values={'one_hour_occurrences': 1})
        self.assertTrue(report_item.is_seen_before())
