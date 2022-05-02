# -*- coding: utf-8 -*-
"""
Similar to soup package, we have define crawl function to
do them automatically using sselenium

Created by Kunhong Yu
Date: 2022/04/25
"""


# Finally, we combine them together
def crawl_all(limit = 50,
              scrape_each_author = True,
              subject = ['Computer Science', 'Physics', 'Mathematics'],
              ssubject = ['Computing Research Repository', 'Physics', 'Mathematics'],
              sssubject = ['Computer Vision and Pattern Recognition', 'Machine Learning',
                          'Applied Physics', 'functional analysis']):
    """This function is used to combine all together
    Unlike Beautiful Soup, we can not print information SEQUENTIALLY,
    since scrapy runs with multithreads, so we tend to print each item
    after we scrape everything!
    Args :
        --limit: upper limit of scrapy, default is 50
        --subject: main subject
        --ssubject: subsubject
        --sssubject: subsubsubject
    return :
        --author_links
    """
    pass # TODO



# Unit test
if __name__ == '__main__':
    crawl_all(limit = 10,
              scrape_each_author = True)