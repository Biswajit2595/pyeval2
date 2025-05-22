from flask import Flask,request,jsonify,json

app=Flask(__name__)


def load_posts():
    try:
        with open("post.json","r") as file:
            post=json.load(file)
    except FileNotFoundError:
        post={}
    return post

def save_posts(post):
    with open("post.json","w") as file:
        json.dump(post,file,indent=4)
        
        

post=load_posts()

@app.route("/")
def home():
    return "Welcome to Social Media App"

@app.route("/get",methods=["GET"])
def get_posts():
    return jsonify(post)

@app.route("/create",methods=["POST"])
def create():
    data=request.get_json()
    username=data['username']
    new_post={"username":data['username'],"caption":data['caption']}
    post[username]=new_post
    save_posts(post)
    return jsonify({"msg":"new post has been created","post":new_post})
    
@app.route("/delete/<string:username>",methods=["DELETE"])
def deletepost(username):
    if username in post:
        del post["username"]
        return jsonify({"msg":"Post has been successfully deleted"})
    else:
        return jsonify({'msg':"No post found"})




if __name__=="__main__":
    app.run(debug=True)