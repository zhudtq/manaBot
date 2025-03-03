import os
from paddleocr import PaddleOCR

def init_ocr():
    currentDir = os.path.dirname(os.path.abspath(__file__))
    modelDir = os.path.join(currentDir, 'models')
    os.makedirs(modelDir, exist_ok=True)
    ocr = PaddleOCR(lang="ch", det_model_dir=f"{modelDir}/det", rec_model_dir=f"{modelDir}/rec")
    return ocr

def getTexts(ocr):
    results = ocr.ocr('./screenshots/aaa.webp', det=True, rec=True, cls=True)
    for line in results[0]:
        bbox, (text, _) = line  # 喵～忽略置信度
        x1, y1 = bbox[0]
        x2, y2 = bbox[2]
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        print(f"文字：{text}，位置：({center_x:.0f}, {center_y:.0f})")


    a = [[ 
          [[[294.0, 242.0], [454.0, 242.0], [454.0, 263.0], [294.0, 263.0]], ('游', 0.998370349407196)], 
          [[[194.0, 298.0], [424.0, 298.0], [424.0, 371.0], [194.0, 371.0]], ('不让玩', 0.9972876906394958)], 
          [[[461.0, 298.0], [677.0, 298.0], [677.0, 375.0], [461.0, 375.0]], ('你直说', 0.9882798194885254)], 
          [[[252.0, 404.0], [595.0, 406.0], [595.0, 429.0], [252.0, 427.0]], ("If", 0.8971909284591675)]
        ]]