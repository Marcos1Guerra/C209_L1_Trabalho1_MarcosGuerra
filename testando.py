from PIL import Image
import pytesseract
import cv2
import numpy as np

# Carregue a imagem
image = Image.open('texto2.png')

# Converta a imagem do formato PIL para numpy array (OpenCV)
image_cv = np.array(image)

# Converta a imagem para o formato BGR (caso não esteja no formato correto)
if image_cv.shape[-1] == 3:  # Verifique se a imagem já está no formato BGR
    pass
else:  # Converta para BGR
    image_cv = cv2.cvtColor(image_cv, cv2.COLOR_RGB2BGR)

# Use o Tesseract para detectar caixas delimitadoras de texto
detections = pytesseract.image_to_boxes(image_cv)

# Desenhe as caixas delimitadoras na imagem
for detection in detections.splitlines():
    detection = detection.split()
    x, y, w, h = int(detection[1]), int(detection[2]), int(detection[3]), int(detection[4])
    cv2.rectangle(image_cv, (x, y), (w, h), (0, 255, 0), 2)

# Imprima o texto reconhecido
text = pytesseract.image_to_string(image)
print("Texto Reconhecido:")
print(text)

# Exiba a imagem com as caixas delimitadoras
Image.fromarray(image_cv).show()