#-*- coding:utf-8 -*-
"""
执行用例，生产测试报告
"""

import unittest
import HTMLTestRunner
import os

casedir = os.path.join(os.getcwd(),"testCases")

reportdir = os.path.join(os.getcwd(),"report")

def import_case():
    allcase = unittest.defaultTestLoader.discover(casedir,pattern = '*Case.py')
    return allcase

if __name__ == '__main__':
    reportpath = os.path.join(reportdir,"caserepot.html")
    try:
        with open(reportpath,'wb') as f:
            runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                                   title="测试报告",
                                                   description="执行情况")
            runner.run(import_case())
    except Exception as e:
        print(e)
    
    