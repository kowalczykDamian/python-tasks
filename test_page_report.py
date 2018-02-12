import unittest
import page_report

class TestPageReport(unittest.TestCase):

    def test_parse_url(self):
        self.assertEqual(page_report.parse_url('10.4.180.222 [28/Jan/2018:10:02:32 +0100] "GET http://clearcode.cc/ HTTP/1.1" 200 1080'), 'clearcode.cc')
        self.assertEqual(page_report.parse_url('10.4.180.222 [28/Jan/2018:10:03:31 +0100] "GET http://www.clearcode.cc HTTP/1.1" 200 3056'), 'www.clearcode.cc')
        self.assertEqual(page_report.parse_url('10.4.180.222 [28/Jan/2018:10:05:30 +0100] "GET http://clearcode.cc/careers HTTP/1.1" 200 3056'), 'clearcode.cc/careers')
        self.assertEqual(page_report.parse_url('10.4.180.222 [28/Jan/2018:10:08:29 +0100] "GET http://clearcode.cc/careers/ HTTP/1.1" 200 3056'), 'clearcode.cc/careers')
        self.assertEqual(page_report.parse_url('10.4.180.222 [28/Jan/2018:10:13:29 +0100] "GET http://clearcode.cc/careers? HTTP/1.1" 200 3056'), 'clearcode.cc/careers')
        self.assertEqual(page_report.parse_url('10.4.180.222 [28/Jan/2018:10:21:27 +0100] "GET http://clearcode.cc/careers/? HTTP/1.1" 200 3056'), 'clearcode.cc/careers')
        self.assertEqual(page_report.parse_url('10.4.180.222 [28/Jan/2018:10:34:26 +0100] "GET http://clearcode.cc/careers?offer=internship&type=python HTTP/1.1" 200 4545'), 'clearcode.cc/careers')
        self.assertEqual(page_report.parse_url('10.4.180.222 [28/Jan/2018:10:55:25 +0100] "GET http://clearcode.cc/careers?type=frontend&offer=internship HTTP/1.1" 200 5454'), 'clearcode.cc/careers')



if __name__ == '__main__':
    unittest.main()
