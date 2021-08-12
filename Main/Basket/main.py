import wget
import os
import time

def download_file():
    os.remove("D:/SMU/Year 2 Term 2/Spreadsheet/Group project/Main/Basket/basket-sg-en-es3.csv")
    url = "https://www.ssga.com/sg/en/individual/etfs/library-content/products/fund-data/etfs/apac/basket-sg-en-es3.csv"
    wget.download(url, "D:/SMU/Year 2 Term 2/Spreadsheet/Group project/Main/Basket/basket-sg-en-es3.csv")
    
if __name__ == "__main__":
    while True:
        print("Retrieving the file")
        download_file()
        time_wait = 24
        print(f'\nWaiting {time_wait} hours')
        time.sleep(time_wait*60*60)


