# -*- coding: utf-8 -*-
"""
Main function for sselenium

Created By Kunhong Yu(444447)
Date: 2022/04/26
"""
from sselenium.crawl import crawl_all
from processing.process import procedure

def mainSelenium(opt):
    # main function

    # we start crawling
    if opt.crawl:
        print('*' * 50)
        print('Start crawling using sscrapy...')
        crawl_all(subject = opt.subject,
                  ssubject = opt.ssubject,
                  sssubject = opt.sssubject,
                  limit = opt.limit,
                  scrape_each_author = opt.scrape_each_author)

    if opt.analyse:
        # if analyses all information
        print('*' * 50)
        print('Start analysing...')
        if opt.scrape_each_author:
            procedure(mode = 'sselenium', for_author = False) # for all the papers
            procedure(mode = 'sselenium', for_author = True) # for all the authors
        else:
            procedure(mode = 'sselenium', for_author = False)
        print('*' * 50)

    print('*' * 50)