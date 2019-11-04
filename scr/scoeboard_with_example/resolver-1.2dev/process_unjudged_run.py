import xml.dom.minidom
import os

if __name__ == "__main__":

    xmlpath = os.path.abspath("ext2.xml")
    domobj = xml.dom.minidom.parse(xmlpath)
    elementobj = domobj.documentElement

    runs = elementobj.getElementsByTagName("run")
    for run in runs:
        runid = run.getElementsByTagName("id")[0].firstChild.data
        judged = run.getElementsByTagName("judged")
        if len(judged) == 0 :
            elementobj.removeChild(run)

    fp = open("out.xml", 'w', encoding='utf8')
    elementobj.writexml(fp, indent='  ')


    
