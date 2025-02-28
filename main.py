from ultralytics import YOLO
import requests
import cv2
import numpy as np

model = YOLO('yolo11n.pt')

def get_image_from_url(url):
    try:
        response = requests.get(url)
        image_array = np.asarray(bytearray(response.content), dtype=np.uint8) # numpy image byte array
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        return image

    except Exception as e:
        print(e.args[0])

def get_objects(url, showimage=True):
    results = model.predict(source=get_image_from_url(url), conf=0.4, save=False, stream=False)

    if showimage == True:
        annotated_image = results[0].plot()
        cv2.imshow("Detection Image", annotated_image)
        cv2.waitKey(0) # wait until key press to close iagmae
        cv2.destroyAllWindows()

    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0]) 
        class_id = int(box.cls[0]) 
        confidence = box.conf[0].item() 
        print(f"Detected: {results[0].names[class_id]}, BBox: ({x1}, {y1}, {x2}, {y2})")

    return results

get_objects("https://media.discordapp.net/attachments/1286060182866104423/1344380810509287564/image.jpg?ex=67c0b3b2&is=67bf6232&hm=1c170ff57b0a03efc390bdcc140b8c39438feff7527ed152879a6970fa8e13fa&=&format=webp&width=556&height=741")

