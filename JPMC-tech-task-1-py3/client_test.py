import unittest
from client3 import *

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
     for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


  """ ------------ Add more unit test one------------ """
  def test_getRatio_workingPrices(self):
    quote_ABC = {'bid': 87.4, 'ask': 87.35, 'price': 87.375}
    quote_DEF = {'bid': 86.8, 'ask': 85.06, 'price': 85.93}
    
    self.assertEqual(getRatio(quote_ABC['price'], quote_DEF['price']), (quote_ABC['price']/quote_DEF['price']))

  """ ------------ Add unit test two ------------ """
  def test_getRatio_secondPriceBeingZero(self):
    quote_ABC = {'bid': 87.4, 'ask': 87.35, 'price': 87.375}
    quote_DEF = {'bid': 86.8, 'ask': 85.06, 'price': 0}
    
    self.assertIsNone(getRatio(quote_ABC['price'], quote_DEF['price']))



if __name__ == '__main__':
    unittest.main()
