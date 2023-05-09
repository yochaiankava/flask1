from flask import Blueprint
sport_pb = Blueprint("sport", __name__, url_prefix="/sport")

@sport_pb.route("/")
def sport():
    return "<p>This is the SPORT section</p>"

@sport_pb.route("/local")
def sport_local():
    return "<p>This is the LOCAL SPORT UPDATE</p>"