from os import get_terminal_size
import urllib.request

gutenberg_projects = [
                        # "https://www.gutenberg.org/cache/epub/84/pg84-images.html",
                        # "https://www.gutenberg.org/cache/epub/1342/pg1342-images.html",
                        # "https://www.gutenberg.org/cache/epub/25344/pg25344-images.html"
                        "https://www.gutenberg.org/cache/epub/98/pg98-images.html"
                    ]
for i in range(len(gutenberg_projects)):
    fp = urllib.request.urlopen(gutenberg_projects[i])
    mybytes = fp.read()

    project_html = mybytes.decode("utf8")
    fp.close()

    # if(i==0):
    #     filename = "gutenberg/1.html"
    # elif(i==1):
    #     filename = "gutenberg/2.html"
    # elif(i==2):
    #     filename = "gutenberg/3.html"

    file = open("gutenberg/3.html", "w")
    file.write(project_html)
    file.close()