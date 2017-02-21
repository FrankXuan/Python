def read_rext():
    quotes = open("C:\OOP\movie_quotes.txt")
    contents_of_files = quotes.read()
    print (contents_of_files)
    quotes.close()


read_rext()
