import flask
from newsApi import getNews
from datetime import datetime

app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template("home.html")

@app.route('/news')
def news():
    search = flask.request.args.get("search")
    if isinstance(search, str) and search.strip() != "":
        raw = getNews(search, "relevancy", 10)
        articles = []

        for a in raw["articles"]:
            dt = datetime.fromisoformat(a["publishedAt"].replace("Z", ""))
            published = dt.strftime("%B %d, %Y")

            articles.append({
                "title": a["title"],
                "author": a["author"],
                "source": a["source"]["name"],
                "description": a["description"],
                "url": a["url"],
                "urlToImage": a["urlToImage"],
                "publishedAt": published,
                "content": a["content"]
            })

        return flask.render_template(
            "news.html",
            articles=articles,
            search=search
        )

    else:
        return flask.render_template("search.html")
    

if __name__ == '__main__':
    app.run()