import os
import webbrowser

class template:

    def __init__(self):
        self.path = os.getcwd
        self.demo_path = None #demo dosya konumu değiştirilebilir

    def temp_init(self, adi):
        try:
            os.mkdir(adi)
        except:
            pass
        os.chdir(adi)
        index = open("index.html", "w")
        self.demo_path = self.demo_path = os.getcwd()
        index.write("""<html>
<head>
<title>"""+adi+"""</title>
</head>""")
        
    #Bug fixlendi
    def sayfa(self, adi):
        sayfa2 = open(adi + ".html", "w")
        os.chdir(self.demo_path)
        with open("index.html", "a") as index:
            index.write('\n<a href="'+adi+'.html">'+adi+'</a>')
        sayfa2.write("""<html>
<head>
<title>"""+adi+""" Sayfası</title>
</head>""")

    def yazi(self, dosya, yazi):
        os.chdir(self.demo_path)
        with open(dosya + ".html", "a") as dos:
            dos.write("""\n<body>
"""+yazi+"""\n</body>""")

