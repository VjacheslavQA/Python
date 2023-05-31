import unittest

from Task5.task5_1_1 import get_requests_not_200
from Task5.task5_1_2 import post_request
from Task5.task5_1_3_1_and_5_1_3_2 import find_languages_code
from Task5.task5_1_3_1_and_5_1_3_2 import number_of_people_using_language


class Test1_2(unittest.TestCase):

    def test_get_requests_not_200(self):
        self.assertNotEqual(get_requests_not_200().values(), "200")

    def test_post_request(self):
        self.form = {"comments": "Test post",
                     "custemail": "putler@kaput",
                     "custname": "Tester",
                     "custtel": "+38097654321",
                     "delivery": "12:15",
                     "size": "large",
                     "topping": ["bacon", "mushroom"]
                     }
        self.headers = {"User-Agent": "Python Learning Requests"}
        self.assertEqual(self.form, post_request()[0])
        self.assertIsInstance(self.form, dict)


class Test3_4(unittest.TestCase):

    def setUp(self):
        self.languages = ['kwn', 'srp', 'lit', 'smo', 'glv', 'kck', 'tam', 'swa', 'msa',
                          'sot', 'que', 'sqi', 'run', 'isl', 'prs', 'kon', 'ltz', 'niu',
                          'uzb', 'bar', 'tso', 'dzo', 'ben', 'kor', 'arc', 'pus', 'aze',
                          'kin', 'mfe', 'fij', 'nld', 'por', 'hin', 'lin', 'rar', 'fao',
                          'lat', 'nfr', 'nso', 'deu', 'ell', 'ukr', 'lav', 'hrv', 'tsn',
                          'mlg', 'hye', 'hat', 'nde', 'cat', 'pap', 'cnr', 'mya', 'gil',
                          'zul', 'pih', 'ara', 'eng', 'tkl', 'zdj', 'est', 'loz', 'nor',
                          'nob', 'kaz', 'gsw', 'toi', 'tur', 'khm', 'crs', 'afr', 'tha',
                          'cha', 'hif', 'mkd', 'ita', 'xho', 'tpi', 'ber', 'mon', 'zho',
                          'bos', 'fas', 'mah', 'bwg', 'bul', 'hgm', 'amh', 'slv', 'pau',
                          'heb', 'sna', 'nbl', 'ssw', 'sin', 'ndc', 'tgk', 'kal', 'mri',
                          'spa', 'smi', 'fin', 'sag', 'tet', 'swe', 'gle', 'mey', 'fra',
                          'ces', 'pov', 'nya', 'aym', 'tir', 'slk', 'pol', 'nzs', 'nep',
                          'jam', 'rus', 'jpn', 'nau', 'mlt', 'tuk', 'bjz', 'bis', 'div',
                          'ven', 'ind', 'bel', 'ndo', 'lao', 'her', 'vie', 'urd', 'khi',
                          'nrf', 'cal', 'dan', 'ton', 'hmo', 'kir', 'tvl', 'roh', 'som',
                          'kat', 'hun', 'zib', 'ckb', 'lua', 'fil', 'ron', 'grn', 'nno']

        self.lang_codes = find_languages_code()

    def test_find_languages_code(self):
        for lang in self.languages:
            self.assertIn(lang, self.lang_codes)

    def test_number_of_people_using_language(self):
        lang_population = {'ukr': 44134693}
        self.assertEqual(number_of_people_using_language(['ukr']), lang_population)


if __name__ == '__main__':
    unittest.main()
