import os
import codecs
from datetime import datetime
from markdown import markdown

def get_md_content(permalink, ismd=True):

    path = "%s/posts/%s.md" % (os.getcwd(), permalink)
    content = codecs.open(path, mode="r", encoding="utf-8").read()

    return markdown(content) if ismd else content


def write_md_content(permalink, content):
    
    path = "%s/posts/%s.md" % (os.getcwd(), permalink)
    file = codecs.open(path, mode="w", encoding="utf-8")
    file.write(content)
    file.close()


def filter_datetime(date, fmt='%c'):
    try:
        date = datetime.strftime(date, "%B %d, %Y")
    except Exception, e:
        pass
    
    return date
    
