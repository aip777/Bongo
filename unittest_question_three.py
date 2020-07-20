import unittest
import question_three


class TestQuestionThree(unittest.TestCase):
    def test_question_three(self):
        Trees = question_three.Tree
        result = question_three.foundation.leftNode = Trees(2)
        self.assertEqual(result.key, 2)

    def question_three(self):
        result_1 = question_three.lca(node1=6, node2=7)
        self.assertEqual(result_1, 3)
        result_2 = question_three.lca(node1=3, node2=7)
        self.assertEqual(result_2, 3)

if __name__ == '__main__':
    unittest.main()