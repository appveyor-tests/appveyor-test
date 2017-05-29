import os
import socket
import unittest


class Test(unittest.TestCase):
    def test_UNC_path(self):
        # Create the UNC path, like \\myhost\c$\foo\bar.
        path = os.path.dirname(os.path.abspath(__file__))
        self.assertIn(os.path.basename(__file__), os.listdir(path))
        hn = socket.gethostname()
        drive = path[0]
        unc = "\\\\%s\\%s$"%(hn, drive)
        unc += path[2:]
        self.assertIn(os.path.basename(__file__), os.listdir(unc))


if __name__ == '__main__':
    unittest.main()
