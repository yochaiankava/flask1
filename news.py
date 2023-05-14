from flask import Blueprint
from flask import Blueprint, render_template

news_pb = Blueprint("news", __name__, url_prefix="/news")

@news_pb.route("/")
def news():
    # return render_template("news.html")
    news_array = ["Champions league starting at 12",
    "Be Ready",
    "eurovision is starting",
    "traffic jam in ayalon"
    ]
    return render_template("news.html", news_arr=news_array)
    # <p> **** This is the NEWS ****</p>"

@news_pb.route("/global")
def news_global():
    return "<p>This is the GLOBAL NEWS</p>"
