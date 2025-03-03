import screenshot
import ocr

print('start running!')
ocrModel = ocr.init_ocr()
ocr.getTexts(ocrModel)
# screenshot.randomShot()