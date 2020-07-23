import unittest
from testing.new import Operations
from classes.Item import *
from classes.Order import *


class MyTest(unittest.TestCase):
    item = Item()
    order = Order()

    def test_add(self):
        abc = Operations()
        actual_result = abc.add(5, 6)
        expected_result = 11
        self.assertEqual(expected_result, actual_result)

    def test_check_even_no(self):
        op = Operations()
        actual_result = op.check_even_no(6)
        # expected_result = True
        # self.assertEqual(expected_result, actual_result)
        self.assertTrue(actual_result)

    def test_check_even_no(self):
        op = Operations()
        actual_result = op.check_even_no(5)
        self.assertFalse(actual_result)

    def test_add_item(self):
        result = self.item.add_item('test_item', 'test_type', 100)
        self.assertTrue(result)

    def test_add_item_view(self):
        result = self.item.add_item('', '', 100)
        self.assertFalse(result)

    def test_add_item_view(self):
        result = self.item.add_item('test', 'type', 'asd')
        self.assertFalse(result)

    def test_add_item_view(self):
        result = self.item.add_item('', '', -100)
        self.assertFalse(result)

    def test_show_items(self):
        data = self.item.show_item()
        actual_result = len(data)
        expected_result = 9
        self.assertEqual(expected_result, actual_result)

    def test_search_item(self):
        data = self.item.search_item('momo')
        actual_result = len(data)
        expected_result = 2
        self.assertEqual(expected_result, actual_result)

    def test_search_items1(self):
        data = self.item.search_item('noodle')
        actual_result = len(data)
        expected_result = 0
        self.assertEqual(expected_result, actual_result)

    def test_order_items(self):
        listdata = [(1,5)]
        data = self.order.add_order(5, listdata)
        self.assertTrue(data)

    def test_order_items(self):
        listdata = [(1, 5)]
        data = self.order.add_order("five", listdata)
        self.assertFalse(data)

    def test_order_items(self):
        listdata = [("", "")]
        data = self.order.add_order(5, listdata)
        self.assertFalse(data)

    def test_order_items(self):
        listdata = [(1, 5)]
        data = self.order.add_order("", listdata)
        self.assertFalse(data)

    def test_ordershow_items(self):
        data = self.order.show_orders_by_order_id(3)
        actual_result = len(data)
        expected_result = 3
        self.assertEqual(expected_result, actual_result)

    def test_showallorder(self):
        data=self.order.show_all_orders()
        actual_result = len(data)
        expected_result=44
        self.assertEqual(expected_result, actual_result)

    def test_showallorder(self):
        data=self.order.show_all_orders()
        actual_result = len(data)
        expected_result=42
        self.assertNotEqual(expected_result, actual_result)

    # def test_updatedorderitem(self):

