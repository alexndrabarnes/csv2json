# test_tokenhaven.py
"""
Tests for TokenHaven module.
"""

import unittest
from tokenhaven import TokenHaven

class TestTokenHaven(unittest.TestCase):
    """Test cases for TokenHaven class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenHaven()
        self.assertIsInstance(instance, TokenHaven)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenHaven()
        self.assertTrue(instance.run())

    def test_multiple_instances_share_single_handler(self):
        """Each TokenHaven must not attach another StreamHandler."""
        import logging
        logger = logging.getLogger("tokenhaven")
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
        TokenHaven()
        TokenHaven()
        TokenHaven()
        self.assertEqual(len(logger.handlers), 1)

if __name__ == "__main__":
    unittest.main()
