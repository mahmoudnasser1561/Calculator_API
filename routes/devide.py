from flask import jsonify, request
from flask_restful import Resource
from logic.devide import devide_numbers
from utils.checkPostedData import ValidatePostedData

class Devide(Resource):
    def post(self):
        if request.is_json:
            postedData = request.get_json()
        else:
            postedData = request.args.to_dict()

        status_code = ValidatePostedData(postedData)

        if (status_code != 200):
            if (status_code == 301):
                Message = "Missing Parameter"
            elif (status_code == 302):
                Message = "Parameters Must be intergers"
            retJson = {
                "Message": Message,
                "Status Code":status_code
            }
            return jsonify(retJson)
        
        try:
            x = int(request.args.get("x"))
            y = int(request.args.get("y"))
        except (KeyError, TypeError, ValueError):
            return jsonify({
                "Message": "Invalid input. 'x' and 'y' must be numbers.",
                "Status Code": 400
            })
        
        result = devide_numbers(x, y)
        return jsonify({
            "Message": result,
            "Status Code": 200
        })