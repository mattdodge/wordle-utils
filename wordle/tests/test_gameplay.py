from unittest import TestCase
from wordle.core.gameplay import get_result, filter_word_list
from wordle.core.result import ensure_result


class TestGameplay(TestCase):

    def test_get_result(self):
        self.assertEqual(get_result('brain', 'could'), ensure_result('_____'))
        self.assertEqual(get_result('brain', 'treat'), ensure_result('_!?__'))
        # First O is a wrong spot, second is a miss
        self.assertEqual(get_result('robot', 'broth'), ensure_result('???_?'))

    def test_filter_word_list(self):
        words = ['claim', 'email', 'image', 'sigma', 'swami']
        new_words = filter_word_list(words, 'stain', ensure_result('__!!_'))
        self.assertEqual(new_words, ['claim', 'email'])
