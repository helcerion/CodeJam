from os import path
from sys import argv
'''
Problem
 You recive a credit C at a local sotre and would like to buy two items. You first walk
 through the store and create a list L of all available items. From this list you woluld like to
 buy two items that add up to the entire value of the credit. The solution you provide will
 consist of the two integers indicating the positions of the items in your list (smaler
 number first).
Input
 The first line of input gives the number of cases, N. N test cases follow. For each test case
 there will be:
     * One line containing the value C, the amount of credit you have at the store.
     * One line containing the value I, the number of items in the store.
     * One line containing a space separated list fo I integers. Each integer P indicates the
       price of an item in the store.
     * Each test case will have exactly one solution.
 Output
  For each test case, output one line containing "Case #x: " followed by the indices of the
  two items whose price adds up to the store credit. The lower index should be output first.
 Limits
  5 <= C <= 1000
  1 <= P <= 1000
 Small dataset
  N = 10
  3 <= I <= 100
 Large dataset
  N = 50
  3 <= I <= 2000
 Sample
 # Input                         Output
 #  3                             case #1: 2 3
 #  100                           case #2: 1 4
 #  3                             case #3: 4 5
 #  5 75 25
 #  200
 #  7
 #  150 24 79 50 88 345 3
 #  8
 #  8
 #  2 1 9 4 4 56 90 3
'''

class StoreCredit(object):
    _credit = None
    _store_size = None
    _store = None
    
    def __init__(self, *args):
        super(StoreCredit, self).__init__(*args)

    def setListSize(self, size):
        self._store_size = size
        
    def setItemsList(self, list):
        self._store = self._checkStoreList(list)
        
    def buyItems(self, credit):
        self._checkCredit(credit)
        items = []
        for index_a, item_a in enumerate(self._store, 1):
            if int(item_a) < credit:
                for index_b, item_b in enumerate(self._store[index_a:], index_a + 1):
                    if (int(item_a) + int(item_b)) == credit:
                        items.append(index_a)
                        items.append(index_b)
                        break 
        return items
        
    def _checkCredit(self, credit):
        if not (5 <= credit <= 1000):
            raise Exception('Credit out of limit')
        return credit
            
    def _checkStoreList(self, store_list):
        if len(store_list) != self._store_size:
            raise Exception('Incorrect number of items')
        for price in store_list:
            self._checkProductPrice(int(price))
        return store_list
            
    def _checkProductPrice(self, price):
        if not (1 <= price <= 1000):
            raise Exception('Price ' + str(price) + ' out of limit')
        
def main():
    # Parsear el fichero con el input
    file_input = open(path.realpath(argv[1]))
    number_of_cases = int(file_input.readline())
    store = StoreCredit()
    for case in range(1, number_of_cases + 1):
        amount = int(file_input.readline())
        number_of_items = int(file_input.readline())
        items_list = (file_input.readline()).split()
        store.setListSize(number_of_items)
        store.setItemsList(items_list)
        items = store.buyItems(amount)
        print 'case #' + str(case) + ':', items[0], items[1]
    pass
            
if __name__ == "__main__":
    main()