# git add .
# git commit -m "message"
# git push origin main

from inference import get_model
import supervision as sv
from inference.core.utils.image_utils import load_image_bgr
 
image = load_image_bgr("https://media.discordapp.net/attachments/1286060182866104423/1344380810509287564/image.jpg?ex=67c0b3b2&is=67bf6232&hm=1c170ff57b0a03efc390bdcc140b8c39438feff7527ed152879a6970fa8e13fa&=&format=webp&width=556&height=741")
model = get_model(model_id="yolov8n-640")
results = model.infer(image)[0]
results = sv.Detections.from_inference(results)
annotator = sv.BoxAnnotator(thickness=2)
annotated_image = annotator.annotate(image, results)
annotator = sv.LabelAnnotator(text_scale=1, text_thickness=1)
annotated_image = annotator.annotate(annotated_image, results)
sv.plot_image(annotated_image)
