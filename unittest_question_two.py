import unittest
import question_two


class TestQuestionTwo(unittest.TestCase):

    def test_question_two(self):
        result = question_two.Person("Islam","Shaiful","Korim")
        res = result.first_name, result.last_name, result.father
        self.assertEqual(res, ('Islam', 'Shaiful', 'Korim'))


if __name__ == '__main__':
    unittest.main()