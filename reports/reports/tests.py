import autofixture
from django.test import TestCase
from reports.models import ReportItem, Report


class ReportItemTest(TestCase):
    def setUp(self):
        self.report = autofixture.create_one(Report)

    def test_not_seen_before(self):
        report_item = autofixture.create_one(
            ReportItem,
            field_values={'one_hour_occurrences': 0,
                          'two_hour_occurrences': 0,
                          'four_hour_occurrences': 0,
                          'eight_hour_occurrences': 0,
                          'sixteen_hour_occurrences': 0,
                          'report': self.report})
        self.assertFalse(report_item.is_seen_before())

    def test_seen_before(self):
        report_item = autofixture.create_one(
            ReportItem, field_values={'one_hour_occurrences': 1,
                                      'report': self.report})
        self.assertTrue(report_item.is_seen_before())
