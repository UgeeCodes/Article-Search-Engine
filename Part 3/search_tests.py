from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)

    def test_keyword_to_titles(self):
        metadata = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023, ['canadian', 'canada', 'lee', 'jazz', 'rock', 'singer']]]
        expected = {'canadian': ['List of Canadian musicians'], 'canada': ['List of Canadian musicians'], 'lee': ['List of Canadian musicians'], 'jazz': ['List of Canadian musicians'], 'rock': ['List of Canadian musicians'], 'singer': ['List of Canadian musicians']}
        self.assertEqual(keyword_to_titles([[]]), {})
        self.assertEqual(keyword_to_titles([]), {})
        self.assertEqual(keyword_to_titles(metadata), expected)
    
    def test_title_to_info(self):
        metadata = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023, ['canadian', 'canada', 'lee', 'jazz', 'rock', 'singer']]]
        expected = {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}}
        self.assertEqual(title_to_info([[]]), {})
        self.assertEqual(title_to_info([]), {})
        self.assertEqual(title_to_info(metadata), expected)
    
    def test_search(self):
        bank = {'canadian': ['List of Canadian musicians'], 'canada': ['List of Canadian musicians'], 'lee': ['List of Canadian musicians'], 'jazz': ['List of Canadian musicians'], 'rock': ['List of Canadian musicians'], 'singer': ['List of Canadian musicians']}
        self.assertEqual(search('canadian', bank), ['List of Canadian musicians'])
        self.assertEqual(search('', {}), [])
        self.assertEqual(search('', bank), [])
        self.assertEqual(search('canada', {}), [])
    
    def test_article_length(self):
        information = {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}}
        titles = ['List of Canadian musicians']
        self.assertEqual(article_length(35000, [], information), [])
        self.assertEqual(article_length(60, [], {}), [])
        self.assertEqual(article_length(30000, titles, information), titles)
        
    def test_key_by_author(self):
        information = {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}}
        titles = ['List of Canadian musicians']
        expected = {'Jack Johnson': ['List of Canadian musicians']}
        self.assertEqual(key_by_author([], information), {})
        self.assertEqual(key_by_author([], {}), {})
        self.assertEqual(key_by_author(titles, information), expected)

    def test_filter_to_author(self):
        information = {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}}
        titles = ['List of Canadian musicians']
        self.assertEqual(filter_to_author('', [], {}), [])
        self.assertEqual(filter_to_author('Jack Johnson', [], information), [])
        self.assertEqual(filter_to_author('Jack Johnson', titles, information), titles)

    def test_filter_out(self):
        words = {'canadian': ['List of Canadian musicians'], 'canada': ['List of Canadian musicians'], 'lee': ['List of Canadian musicians'], 'jazz': ['List of Canadian musicians'], 'rock': ['List of Canadian musicians'], 'singer': ['List of Canadian musicians']}
        titles = ['List of Canadian musicians']
        self.assertEqual(filter_out('', titles, {}), titles)
        self.assertEqual(filter_out('aluminium', [], {}), [])
        self.assertEqual(filter_out('condemn', titles, words), titles)

    def test_articles_from_year(self):
        information = {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1686751200, 'length': 21023}}
        titles = ['List of Canadian musicians']
        self.assertEqual(articles_from_year(2023, titles, information), titles)
        self.assertEqual(articles_from_year(2023, [], {}), [])
        self.assertEqual(articles_from_year(2000, titles, information), [])

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_1(self, input_mock):
        keyword = 'sOcCeR'
        advanced_option = 1
        advanced_response = 30000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_2(self, input_mock):
        keyword = 'came'
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: {'Mack Johnson': ['Rock music']}\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_3(self, input_mock):
        keyword = 'any'
        advanced_option = 3
        advanced_response = 'Jack Johnson'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Time travel']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_4(self, input_mock):
        keyword = 'tomorrow'
        advanced_option = 4
        advanced_response = 'hunger'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Annie (musical)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_6(self, input_mock):
        keyword = 'love'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: ['2009 in music', 'Tim Arnold (musician)', '1936 in music', 'Alex Turner (musician)', '2006 in music']\n"

        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
