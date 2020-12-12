import dropbox
import shutil
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token      

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AnSc7swjbAXFyD9_2Mamq0Ok4CQpeO36NQzA2KW9It5lLnYEQ9L-LcDS-RZ_QXJhhuiJivEWEKShUX90GEa3EA8FZxKG8WWZLF0wRIEmRXAUaOt3c4pj4sOr-eTbvURirRVY7dA'
    transferData = TransferData(access_token)
    path = 'D:/Coding Class/Python/c101 homework/test1'
    folder = 'test1'
    dat = os.walk(path)
    for i in dat:
        data = i
        print("Data - ",data)
        file_ = str(data[0])
        print("File_ - ",file_)
        newPath = os.path.join(folder,file_)
        print("New Path - ",newPath)
        AllFiles = os.listdir(newPath)
        print("All Files - ",AllFiles)

    for i in AllFiles:
        file_from = newPath+'/'+i
        print("File From - ",file_from)
        file_to = '/Dropbox/test1/'+i
        print("File to - ",file_to)
        transferData.upload_file(file_from,file_to)
        print("Files uploaded")
        

if __name__ == '__main__':
    main()