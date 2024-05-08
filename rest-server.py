# flask server that links to a DAO
# author: Michael Allen

from flask import Flask, request, jsonify, abort
#from projectDAOskeleton import projectDAO
#import projectDAO
from projectDAO import projectDAO
#import deleteRow


app = Flask(__name__)

@app.route('/')
def index():
        return "Web Services and Applications Project"

# getall
# curl http://127.0.0.1:5000/project

@app.route('/project', methods=['GET'])
def getall():
        return jsonify(projectDAO.getAll())

# find by id
# curl http://127.0.0.1:5000/project/1

@app.route('/project/<int:id>', methods=['GET'])
def findbyid(id):
        return jsonify(projectDAO.findByID(id))

if __name__ == "__main__":
    app.run(debug = True)
