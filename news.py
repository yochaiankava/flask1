from flask import Blueprint
news_pb = Blueprint("news", __name__, url_prefix="/news")

@news_pb.route("/")
def news():
    return "<p>This is the NEWS</p>"

@news_pb.route("/global")
def news_global():
    return "<p>This is the GLOBAL NEWS</p>"
