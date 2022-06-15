import re
from zipfile import ZipFile

def zipper():
    with ZipFile('access.log.zip', 'r') as zip:
        zip.extract('access.log.txt')
        print('File is unzipped in temp folder')


def main():
    #zipper()
    filtered_urls = []
    regex = re.compile('.*?\[((0[7]\/Mar\/2009:((1[2]:((3[4]:2[6-9])|(3[5-9]:\d{2})))|(1[3-9]|2[0-4]):\d{2}:\d{2}))|'
            '(0[8]\/Mar\/2009:((([0-1][0-9]|2[0-2]):\d{2}:\d{2})|((2[3]:[0-3][0-3]:\d{2})|(2[3]:3[4]:(0[1-9]|1[0-1]))))))'
            '.*GET.*?([T][W]iki).*?"\s200')

    with open('access.log.txt', 'r') as file:
        for line in file:
            if regex.search(line) is not None:
                #print(line)
                filtered_urls.append(line)


    for i in filtered_urls:
        print(i)

if __name__ == '__main__':
    main()
