from flask import Flask, request, jsonify
app =Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data= {
        "User_id":user_id,
        "name": "John Doe",
        "E-mail":"john.doe@example.com"


    }
    extra = request.args. get("extra")
    if extra :
        user_data["extra"]=extra
    return jsonify(user_data),200
@app.rputr("/create_user",methods = ["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201

    



if __name__ =="_main_":
    app.run(debug= True)
