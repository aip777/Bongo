import unittest
import question_two


class TestQuestionTwo(unittest.TestCase):

    def test_question_two(self):
        result = question_two.Person("Islam","Shaiful","Korim")
        res = result.first_name, result.last_name, result.father
        self.assertEqual(res, ('Islam', 'Shaiful', 'Korim'))

    def question_two(self):
        result = question_two.print_depth()
        self.assertEqual(result['key1'], 1)
        self.assertEqual(result['key2'], 1)
        self.assertEqual(result['key3'], 2)
        self.assertEqual(result['key4'], 2)
        self.assertEqual(result['key5'], 3)
        self.assertEqual(result['user'], 3)
        self.assertIn(4, result['first_name'])
        self.assertIn(5, result['first_name'])
        self.assertIn(4, result['last_name'])
        self.assertIn(5, result['last_name'])
        self.assertIn(4, result['father'])
        self.assertIn(5, result['father'])


if __name__ == '__main__':
    unittest.main()