from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()


def ObjectDet(filename):

    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(execution_path, "yolo.h5"))

    detector.loadModel()
    detections = detector.detectObjectsFromImage(display_object_name=False, display_box=False, extract_detected_objects=True, display_percentage_probability=False,input_image=os.path.join(execution_path, filename), output_image_path = os.path.join(execution_path, "output.jpg"))

ObjectDet("CHS-Bus-Stop-The-43.jpg")