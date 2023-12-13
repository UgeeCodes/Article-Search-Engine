from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        # Storing into a variable so don't need to copy and paste long list every time
        # If you want to store search results into a variable like this, make sure you pass a copy of it when
        # calling a function, otherwise the original list (ie the one stored in your variable) might be
        # mutated. To make a copy, you may use the .copy() function for the variable holding your search result.
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(search('dog'), expected_dog_search_results)


    def test_search(self):
        assert search('') == []
        assert search('cAt') == ['Voice classification in non-classical music']
        assert search('volleyball') == ['USC Trojans volleyball', 'Mets de Guaynabo (volleyball)']

    def test_title_length(self):
        titles = ['Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        assert title_length(15, titles) == ['Dalmatian (dog)', 'Guide dog', 'Endoglin', 'Sun dog', 'The Mandogs', 'Landseer (dog)']
        assert title_length(100, titles) == ['Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        assert title_length(0, titles) == []
    
    def test_article_count(self):
        language = ['C Sharp (programming language)', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Comparison of programming languages (basic instructions)', 'Ruby (programming language)']
        assert article_count(10, language) == ['C Sharp (programming language)', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Comparison of programming languages (basic instructions)', 'Ruby (programming language)']
        assert article_count(0, language) == []
        assert article_count(6, language) == ['C Sharp (programming language)', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Comparison of programming languages (basic instructions)', 'Ruby (programming language)']

    def test_random_article(self):
        language = ['C Sharp (programming language)', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Comparison of programming languages (basic instructions)', 'Ruby (programming language)']
        assert random_article(3, language) == 'Lua (programming language)'
        assert random_article(0, language) == 'C Sharp (programming language)'
        assert random_article(6, language) == ''

    def test_favorite_article(self):
        language = ['C Sharp (programming language)', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Comparison of programming languages (basic instructions)', 'Ruby (programming language)']
        assert favorite_article('Java', language) == False
        assert favorite_article('Python (programming language)', language) == True
        assert favorite_article('Java (programming language)', language) == False
    
    def test_multiple_keywords(self):
        titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        assert multiple_keywords('', titles) == ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        assert multiple_keywords('God', titles) == ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        assert multiple_keywords('1922', titles) == ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', '1922 in music']


    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'dog'
        advanced_option = 6

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_1_dog(self, input_mock):
        keyword = 'dog'
        advanced_option = 1
        output = get_print(input_mock, [keyword, advanced_option, 15])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "15\n" + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Dalmatian (dog)', 'Guide dog', 'Endoglin', 'Sun dog', 'The Mandogs', 'Landseer (dog)']\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_2_ball(self, input_mock):
        keyword = 'ball'
        advanced_option = 2
        output = get_print(input_mock, [keyword, advanced_option, 20])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "20\n" + "\nHere are your articles: ['USC Trojans volleyball', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Mets de Guaynabo (volleyball)', 'Georgia Bulldogs football under Robert Winston']\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_3_music(self, input_mock):
        keyword = 'music'
        advanced_option = 3
        output = get_print(input_mock, [keyword, advanced_option, 4])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "4\n" + "\nHere are your articles: 1986 in music\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_4_musician(self, input_mock):
        keyword = 'mUsIcIaN'
        advanced_option = 4
        output = get_print(input_mock, [keyword, advanced_option, 'bad'])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "bad\n" + "\nHere are your articles: ['List of Canadian musicians', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Joseph Williams (musician)', 'David Levi (musician)', 'George Crum (musician)', 'Charles McPherson (musician)', 'Paul Carr (musician)', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)']\n" + "Your favorite article is not in the returned articles!\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_5_musician(self, input_mock):
        keyword = 'mUsIcIaN'
        advanced_option = 5
        output = get_print(input_mock, [keyword, advanced_option, 'KeViN'])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + 'KeViN\n' + "\nHere are your articles: ['List of Canadian musicians', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Joseph Williams (musician)', 'David Levi (musician)', 'George Crum (musician)', 'Charles McPherson (musician)', 'Paul Carr (musician)', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Kevin Cadogan']\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_6_musician(self, input_mock):
        keyword = 'mUsIcIaN'
        advanced_option = 6
        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['List of Canadian musicians', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Joseph Williams (musician)', 'David Levi (musician)', 'George Crum (musician)', 'Charles McPherson (musician)', 'Paul Carr (musician)', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)']\n"
        self.assertEqual(output, expected)


# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
