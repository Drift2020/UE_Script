import os

def WriteFiles(elem,OldText,NewText):
    with open(elem, encoding='utf-8', errors='ignore') as file_in:
        text = file_in.readlines()
    text = ''.join(text)
    text = text.replace(OldText, NewText)

    with open(elem, "w", errors='ignore') as file_out:
        file_out.write(text)


def FileFiend(Directory,files,OldText,NewText):
    for elem in files:
        if(elem.find(".")== -1):
             SubFiles = os.listdir(Directory+"\\"+elem)
             FileFiend(Directory+"\\"+elem,SubFiles,OldText,NewText)
        else:
            WriteFiles(Directory+"\\"+elem,OldText,NewText)


Directory  = input("Write your path:")
files = os.listdir(Directory)

OldText = input("Write your old text for replace:")
NewText = input("Write your new text for replace:")

FileFiend(Directory,files,OldText,NewText)
       
   



