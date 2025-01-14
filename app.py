from flask import Flask

app = Flask(__name__)

#definir a rota raiz (Página inicial) e a função que será executada ao ser requisitada




@app.route('/')
def hello_world():
    return "Hello World! muito bom!"


if __name__=="__main__":
    app.run(debug=True)