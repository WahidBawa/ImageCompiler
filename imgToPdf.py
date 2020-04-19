from fpdf import FPDF
from PIL import Image
import glob

pdf = FPDF()
imgType = input("Please enter image extension (png, jpeg, jpg): ")

imageList = glob.glob("*." + imgType)

if len(imageList) > 0:
	for image in imageList:
		cover = Image.open(image)
		width, height = cover.size
		width, height = float(width * 0.264583), float(height * 0.264583)

		pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}

		orientation = 'P' if width < height else 'L'

		width = width if width < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
		height = height if height < pdf_size[orientation]['h'] else pdf_size[orientation]['h']

		pdf.add_page(orientation=orientation)

		pdf.image(image, 0, 0, width, height)
	pdf.output("newPdf.pdf", "F")
	print("file created")
else:
	print("This type of image does not exist within this directory!!")