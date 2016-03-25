#!/usr/bin/env python

from itertools import permutations

MONTHS_30 = (4, 6, 9, 11)
YEAR_FROM = 2000
YEAR_TO = 3000


class DateParser(object):
    year = 0
    month = 0
    day = 0

    def __init__(self, raw_data):
        self.raw_data = raw_data
        self._parse_string()
        self._order_datas()

    def get_string(self):
        return '{}-{}-{}'.format(self.year, self.month, self.day)

    def _parse_string(self):
        self.ideal_data = sorted(
            map(int, self.raw_data.split('/')))

    def _order_datas(self):
        for data in permutations(self.ideal_data):
            self.year = data[0] + YEAR_FROM < YEAR_TO and \
                data[0] + YEAR_FROM or data[0]
            self.month = data[1]
            self.day = data[2]
            if self._check_date():
                return True

    def _is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or \
            self.year % 400 == 0

    def _check_day(self):
        if self.day > 31:
            return False
        if self.month in MONTHS_30 and self.day > 30:
            return False
        if self.month is 2 and self.day > (self._is_leap_year() and 29 or 28):
            return False
        return True

    def _check_month(self):
        return self.month <= 12

    def _check_year(self):
        return self.year >= 0 and self.year < 1000 or \
            self.year >= YEAR_FROM and self.year < YEAR_TO

    def _check_date(self):
        return self._check_day() and self._check_month() and self._check_year()


def main():
    with open('data.txt') as f:
        raw_data = f.readline()
    parser = DateParser(raw_data)

    print(parser._is_leap_year())
    print(parser.get_string())


if __name__ == '__main__':
    main()
