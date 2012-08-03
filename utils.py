import markdown, codecs, os

def get_md_content(permalink, ismd=True):

    path = os.getcwd()+'/posts/'+permalink+'.md'
    content = codecs.open(path, mode="r", encoding="utf-8").read()
    if ismd: content = markdown.markdown(content)

    return content

def write_md_content(permalink, content):

    path = os.getcwd()+'/posts/'+permalink+'.md'
    print path, content
    file = codecs.open(path, mode="w", encoding="utf-8")
    file.write(content)
    file.close()

    return file

