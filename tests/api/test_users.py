import unittest

import gitlabpy


class TestUsers(unittest.TestCase):
    def test_block_url(self):
        func = gitlabpy.api.users.block.api_method
        kwargs = {'uid': 1}
        actual, _ = func(**kwargs)
        expected = '/api/v3/users/1/block'
        self.assertEqual(actual, expected)

    def test_unblock_url(self):
        func = gitlabpy.api.users.unblock.api_method
        kwargs = {'uid': 1}
        actual, _ = func(**kwargs)
        expected = '/api/v3/users/1/unblock'
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
