import unittest
from common.HTMLTestRunner import HTMLTestRunner
from datetime import datetime
from config.config import Config


def get_test_cases(path):
    test_cases = unittest.TestSuite()
    suites = unittest.defaultTestLoader.discover(path, 'test*.py', top_level_dir=path)
    for suite in suites:
        test_cases.addTests(suite)
    return test_cases


if __name__ == '__main__':
    base_path = Config().base_path
    testcase_path = base_path + '/testcase'
    testreport_path = base_path + '/testreport'

    cases = get_test_cases(testcase_path)
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = testreport_path + '/' + now + '-report.html'
    with open(filename, 'w', encoding='utf8') as f:
        runner = HTMLTestRunner(
            stream=f,
            title=u'Web自动化测试',
            description=u'详细测试结果如下:',
            verbosity=2
        )
        runner.run(cases)
