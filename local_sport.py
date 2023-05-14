from flask import Blueprint
from flask import Blueprint, render_template

local_sport_pb = Blueprint("local sport", __name__, url_prefix="/sport/local_sport")
local_sport_array = ["what_is_new",
    "basketball",
    "football",
    "tennis",
     ] 
@local_sport_pb.route("/")
def local_sport():          
    return render_template("local_sport.html", sport_arr=local_sport_array)

