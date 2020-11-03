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

        with open('./src//plus_test.csv') as csv_file:
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

    def test_minus(self):

        test_data_row_list = list()

        with open('./src//minus_test.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                test_data_row_list.append(row)
                # print(','.join(row))
        print('')
        print('******test_minus******')
        # print(','.join(row))
        for row in test_data_row_list:
            x = row[1]
            y = row[0]
            expect_result = row[2]
            result = self.calculator.minus(x, y)
            print(str(x) + ' - ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(int(result), int(expect_result))


    def test_multiply(self):

        test_data_row_list = list()

        with open('./src//multiply_test.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                test_data_row_list.append(row)
                # print(','.join(row))
        print('')
        print('******test_multiply******')
        # print(','.join(row))
        for row in test_data_row_list:
            x = row[0]
            y = row[1]
            expect_result = row[2]
            result = self.calculator.multiply(x, y)
            print(str(x) + ' * ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(int(result), int(expect_result))

    def test_divide(self):

        test_data_row_list = list()

        with open('./src//divide_test.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                test_data_row_list.append(row)
                # print(','.join(row))
        print('')
        print('******test_divide******')
        # print(','.join(row))
        for row in test_data_row_list:
            x = row[1]
            y = row[0]
            expect_result = row[2]
            result = self.calculator.divide(x, y)
            print(str(x) + ' / ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(round(float(result),9), float(expect_result))

    def test_squared(self):

        test_data_row_list = list()

        with open('./src//squared_test.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                test_data_row_list.append(row)
                # print(','.join(row))
        print('')
        print('******test_squared******')
        # print(','.join(row))
        for row in test_data_row_list:
            x = row[0]
            expect_result = row[1]
            result = self.calculator.squared(x)
            print(str(x) + ' ** ' + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(int(result), int(expect_result))

    def test_sqrt(self):

        test_data_row_list = list()

        with open('./src//sqrt_test.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                test_data_row_list.append(row)
                # print(','.join(row))
        print('')
        print('******test_sqrt******')
        # print(','.join(row))
        for row in test_data_row_list:
            x = row[0]
            expect_result = row[1]
            result = self.calculator.sqrt(x)
            print(str(x) + ' ** (1 / 2)' + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(round(float(result),8), round(float(expect_result),8))



if __name__ == '__main__':
    unittest.main()
