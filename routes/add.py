from flask import request, jsonify
from flask_restful import Resource
from logic.add import add_numbers
from utils.checkPostedData import ValidatePostedData

class Add(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = ValidatePostedData(postedData)
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)
        

        try:
            x = int(postedData["x"])
            y = int(postedData["y"])
        except (KeyError, ValueError, TypeError):
            return jsonify({
                "Message": "Invalid input. 'x' and 'y' must be numbers.",
                "Status Code": 400
            })
        
        result = add_numbers(x, y)

        return jsonify({
            "Message": result,
            "Status Code": 200
        })

        