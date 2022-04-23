import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)  
        file = open(file_from, 'rb')
        dbx.files_upload(file.read(), file_to)

    

def main():
    access_token = 'sl.BGRs4mwNDlU-0-hvLcTZHzYe_fXsqId2p3ynqAfOS_r71tzmexCS8jBcwbgBlGk64X32_zqn189AEOherh3I7d8Z_o1QLEQKzGbVpf0bpzRK75CLudEMviJ4Noqfi8e8GR5PAmFGzBs'
    transfer_data = TransferData(access_token)
    
    file_from = "D:/Dakshiin/WhitHatJr/C101Project/Trial_text.txt"
    
    file_to = "/Class_Projects/Trial_text.txt"
    
    transfer_data.upload_file(file_from, file_to)
    print("Files has been moved")

main()