from flask import Blueprint
from flask import Blueprint, render_template

sport_pb = Blueprint("sport", __name__, url_prefix="/sport")

sport_array = ["what_is_new",
    "local_sport",
    "global_sport",
     ]

@sport_pb.route("/")
def sport():     
    return render_template("sport.html", sport_arr=sport_array)
    # return "<p>This is the SPORT section</p>"
    # return render_template("sport.html")

