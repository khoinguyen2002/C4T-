import game_object
def genarate_map(json_file_url):
    text = open(json_file_url,'r').read()
    print(text)

if __name__== '__main__':
    genarate_map('../‪C:\\Users\\HP\\Downloads\\Khôi Nguyên_files\\map1-11111 (1).jso')