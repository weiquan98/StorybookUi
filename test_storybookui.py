# test_storybookui.py
"""
Tests for StorybookUi module.
"""

import unittest
from storybookui import StorybookUi

class TestStorybookUi(unittest.TestCase):
    """Test cases for StorybookUi class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StorybookUi()
        self.assertIsInstance(instance, StorybookUi)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StorybookUi()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
