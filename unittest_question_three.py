import unittest
import question_three


class TestQuestionThree(unittest.TestCase):
    def test_question_three(self):
        Trees = question_three.Tree
        result = question_three.foundation.leftNode = Trees(2)
        self.assertEqual(result.key, 2)


if __name__ == '__main__':
    unittest.main()