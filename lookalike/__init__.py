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


def detect_face(image: np.ndarray) -> bool:
    # TODO: mediapipe. check if there is only 1 face
    pass


def align_face(image: np.ndarray) -> np.ndarray:
    pass


def preprocess(images: [np.ndarray]) -> np.ndarray:
    # TODO: lambda func for preprocess

def get_representation(image: np.ndarray):
    global model
    # TODO: lambda func for representation
    pass


def find_percentage(parent, child):
    pass


def analyze(mom_image, dad_image, child_image):


    images = preprocess([mom_image, dad_image, child_image])
    representations = get_representation(images)
    mom_rep, dad_rep, child_rep = representations[0], representations[1], representations[2]
    mom_percentage = find_percentage(mom_rep, child_rep)
    dad_percentage = find_percentage(dad_rep, child_rep)

    return mom_percentage, dad_percentage