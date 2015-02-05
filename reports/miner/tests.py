from .models import Operation
from .models import SaveNotAllowedException
from .models import FrequentItemSet

from unittest import TestCase
import autofixture


class MinerTest(TestCase):
    def test_operation_save(self):
        self.assertRaises(SaveNotAllowedException,
                          autofixture.create_one, Operation)

    def test_frequent_item_set_save(self):
        self.assertRaises(SaveNotAllowedException,
                          autofixture.create_one, FrequentItemSet,
                          generate_fk=True)
