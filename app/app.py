

from celery import Celery
import feedparser


app = Celery()

@app.task
def read_feed(url):
    feed = feedparser.parse(url)


def main():

    # args = ['worker', '--loglevel=INFO']
    # app.worker_main(argv=args)
    app.worker_main()


if __name__ == '__main__':
    main()
