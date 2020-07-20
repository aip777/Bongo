import unittest
import question_one


class TestQuestionOne(unittest.TestCase):

    def test_question_one(self):
        result = question_one.dictionary
        rps = result['key2']['key3']
        self.assertEqual(rps, 1)

    def question_one(self):
        dictionary = question_one.dictionary
        results = question_one.print_depth(dictionary)
        self.assertEqual(results['key1'], 1)
        self.assertEqual(results['key2'], 1)
        self.assertEqual(results['key3'], 2)
        self.assertEqual(results['key4'], 2)
        self.assertEqual(results['key5'], 3)
        self.assertEqual(results['key6'], 3)
        self.assertEqual(results['key7'], 4)

if __name__ == '__main__':
    unittest.main()