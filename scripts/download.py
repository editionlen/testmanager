'''
download test source
'''
import requests
import os
import sys

def download_source(url):
    r = requests.get(url, stream=True)
    filename = os.path.basename(url)
    with open(filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=512):
            f.write(chunk)
    return filename

def check_file_type(filename):
    try:
        return filename.split('.')[-1]
    except Exception as e:
        print(e)
        return None

def unzip(filename):
    pass

def main():
    url = sys.argv[1]
    filename = download_source(url)
    file_type = check_file_type(filename)
    if file_type == 'zip':
        # 解压文件
        unzip(filename)

if __name__ == '__main__':
    main()
