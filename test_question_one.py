import unittest
import question_one


class TestQuestionOne(unittest.TestCase):

    def test_question_one(self):
        result = question_one.dictionary
        rps = result['key2']['key3']
        self.assertEqual(rps, 1)

if __name__ == '__main__':
    unittest.main()