import os,json

SchoolNameDict = {}

def init() :
    file = open('info.json', 'r', encoding='utf-8')
    content = file.read()
    content = json.loads(content)
    for item in content:
        SchoolNameDict[item['schoolName'][0]] = item['schoolName'][1]

if __name__ == '__main__':
    #init()
    file = open("ext.xml","r",encoding='utf-8')
    Content = file.read()
    Outfile = open("ext2.xml","w+", encoding='utf-8')
    Content = Content.split('\n')
    dictOfRun={}
    i=0
    while i<len(Content) :
        line=Content[i]
        if line.find("<name>") != -1 :
            SplitAll = line.split(')')
            if len(SplitAll) >=2:
                SplitAll = SplitAll[0]
                SplitAll = SplitAll.split('(')[-1]

                Out = "      <name>%s</name>" % SplitAll
            else :
                Out = line
            Outfile.write(Out + "\n")
            i=i+1
        else :
            if line.find("<problem/>")!=-1:
                line="    <problem />"
            elif line.find("<reset/>")!=-1:
                line="  <reset />"
            Outfile.write(line + "\n")
            i=i+1