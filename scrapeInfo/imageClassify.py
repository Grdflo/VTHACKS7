from google.cloud import vision
import io
import os

# Set API credentials from json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\sesch\\Desktop\\GitHub\\VTHACKS7\\scrapeInfo\\image-classification-json.json"

def detect_labels(path):
    labelsList = []
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    for label in labels:
        labelsList.append(label.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return labelsList


def detect_landmarks(path):
    landmarksList = []
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations

    for landmark in landmarks:
        landmarksList.append(landmark.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return landmarksList


def getAssociations(path):
    labels = detect_labels(path)
    landmarks = detect_landmarks(path)
    totalAssociations = labels + landmarks
    return totalAssociations