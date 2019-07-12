import requests as r 

class Translate:
    def __init__(self,target,string,source):
        self.target = target
        self.string = string
        string = string.replace(" ","%20")
        self.response = r.get("https://systran-systran-platform-for-language-processing-v1.p.rapidapi.com/translation/text/translate?source={}&target={}&input={}".format(source,target,string),
                            headers={"X-RapidAPI-Host": "systran-systran-platform-for-language-processing-v1.p.rapidapi.com",
                            "X-RapidAPI-Key": "c4648c305dmsh6584a65ddde721fp1a2753jsn42dd3fb7a27b"})
    def json(self):
        json = self.response.json()
        output = json["outputs"]
        return output
    def getOutput(self):
        output = self.json()
        detect = output[0]
        res = detect["output"]
        return res

class File:
    def __init__(self,doc,target,source,targetF):
        self.doc = doc
        self.target = target
        self.source = source
        self.targetF = targetF
    def convert(self,doc):
        listOfString = []
        with open("{}.txt".format(doc)) as f:
            for line in f:
                listOfString.append(line)
        return listOfString
    def create(self):
        listString = self.convert(self.doc)
        with open("{}.txt".format(self.targetF),"w+") as f:
            for string in listString:
                tar = Translate(target=self.target,string=string,source=self.source)
                res = tar.getOutput()
                f.write(res)
