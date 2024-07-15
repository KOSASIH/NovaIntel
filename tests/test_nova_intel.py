import unittest
from src.core.nova_intel import NovaIntel

class TestNovaIntel(unittest.TestCase):
    def test_init(self):
        nova_intel = NovaIntel()
        self.assertIsInstance(nova_intel, NovaIntel)

    def test_add_adapter(self):
        nova_intel = NovaIntel()
        adapter = InterstellarCommunicationAdapter('localhost', 8080)
        nova_intel.add_adapter(adapter)
        self.assertIn(adapter, nova_intel.adapters)

if __name__ == '__main__':
    unittest.main()
