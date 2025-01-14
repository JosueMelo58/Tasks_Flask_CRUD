from flask import Flask
from models.task import Task


app = Flask(__name__)

#definir a rota raiz (Página inicial) e a função que será executada ao ser requisitada






if __name__=="__main__":
    app.run(debug=True)