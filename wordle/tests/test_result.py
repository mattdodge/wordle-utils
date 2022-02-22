from unittest import TestCase
from wordle.core.result import Result, ensure_result, is_winner


class TestResult(TestCase):

    def test_ensure_result(self):
        self.assertEqual(ensure_result('_'), Result.miss)
        self.assertEqual(ensure_result('?'), Result.wrong_spot)
        self.assertEqual(ensure_result('!'), Result.correct)
        self.assertEqual(ensure_result(Result.miss), Result.miss)
        self.assertEqual(ensure_result(Result.wrong_spot), Result.wrong_spot)
        self.assertEqual(ensure_result(Result.correct), Result.correct)

    def test_ensure_result_list(self):
        self.assertEqual(ensure_result('_?!_?'), [
            Result.miss,
            Result.wrong_spot,
            Result.correct,
            Result.miss,
            Result.wrong_spot,
        ])
        self.assertEqual(ensure_result([
            Result.miss,
            Result.wrong_spot,
            Result.correct,
            Result.miss,
            Result.wrong_spot,
        ]), [
            Result.miss,
            Result.wrong_spot,
            Result.correct,
            Result.miss,
            Result.wrong_spot,
        ])
        # allow mixed types too
        self.assertEqual(ensure_result([
            '_',
            Result.wrong_spot,
            '!',
            Result.miss,
            '?',
        ]), [
            Result.miss,
            Result.wrong_spot,
            Result.correct,
            Result.miss,
            Result.wrong_spot,
        ])

    def test_is_winner(self):
        self.assertTrue(is_winner(ensure_result('!!!!')))
        self.assertFalse(is_winner(ensure_result('!_?!')))
