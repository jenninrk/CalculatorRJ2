import unittest
import csv

from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    calculator = None
    @classmethod
    def setUpClass(cls):
        print('')
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('')
        print('tearDownClass')

    def setUp(self):
        self.calculator = Calculator()
        print('')
        print('setUp')

    def tearDown(self):

        if self.calculator is not None:
            self.calculator = None
        print('')
        print('tearDown')

    def test_plus(self):

        test_data_row_list = list()

        with open('./src//test.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                test_data_row_list.append(row)
                # print(','.join(row))
        print('')
        print('******test_plus******')
        # print(','.join(row))
        for row in test_data_row_list:
            x = row[0]
            y = row[1]
            expect_result = row[2]
            result = self.calculator.plus(x, y)
            print(str(x) + ' + ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(int(result), int(expect_result))


if __name__ == '__main__':
    unittest.main()