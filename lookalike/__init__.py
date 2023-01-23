import traceback
import numpy as np
import cv2


def get_sources(request) -> (np.ndarray, np.ndarray, np.ndarray):

    try:
        mom_array = np.frombuffer(request.files['mom'].read(), np.uint8)
        mom_image = cv2.imdecode(mom_array, cv2.IMREAD_COLOR)
        dad_array = np.frombuffer(request.files['dad'].read(), np.uint8)
        dad_image = cv2.imdecode(dad_array, cv2.IMREAD_COLOR)
        child_array = np.frombuffer(request.files['child'].read(), np.uint8)
        child_image = cv2.imdecode(child_array, cv2.IMREAD_COLOR)

        return mom_image, dad_image, child_image

    except:
        print(f"Error occurred while getting the source image. {traceback.format_exc()}")
        return None, None, None
