import gensim.downloader as api


def main():
    model = api.load("word2vec-google-news-300")
    print(model.most_similar("cat"))

if __name__ == '__main__':
    main()
