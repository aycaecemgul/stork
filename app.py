from flask import Flask, request, Response, send_file
import traceback
import gc
import json
import uuid
import os
import time
import cv2
import waitress
from lookalike import get_sources


# Create the Flask app
app = Flask(__name__)
APP_ROOT_LOOKALIKE = os.getenv('APP_ROOT_LOOKALIKE', '/lookalike')
HEALTH_CHECK_APP_ROOT = os.getenv('HEALTHCHECK_APP_ROOT', '/healthcheck')
HOST = '0.0.0.0'
PORT_NUMBER = 5000


@app.route(APP_ROOT_LOOKALIKE, methods=["POST"])
def __lookalike__() -> Response:

    if request.method == 'POST':

        mom_image, dad_image, child_image = get_sources(request)

        if mom_image is None or dad_image is None or child_image is None:
            print("Couldn't get source images!")
            json_dump = json.dumps({"success": False, "status": 400})
            return Response(json_dump, status=400, mimetype='application/json')

        print("Process started. Calculating the percentages...")


        try:
            pass
        except:
            pass

        response = ""  # TODO: return json response

        return response

    else:
        return Response({"success": False, "message": "Request must be POST."}, status=400, mimetype='application/json')


@app.route(HEALTH_CHECK_APP_ROOT, methods=["GET"])
def __healthcheck__():
    return Response({"success"}, status=200, mimetype='application/json')


if __name__ == '__main__':
    waitress.serve(app, host=HOST, port=PORT_NUMBER)
    app.run(host=HOST, port=PORT_NUMBER, debug=False)

