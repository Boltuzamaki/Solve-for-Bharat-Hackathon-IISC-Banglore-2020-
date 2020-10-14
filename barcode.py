# USAGE
# python barcode_scanner_image.py --image barcode_example.png

# import the necessary packages
from pyzbar import pyzbar
import argparse
import cv2
import requests
url = "http://172.27.74.255//dashboard//save_image.php"



file = ['ean.png','images.png']

for image1 in file:
        #load the input image
        image = cv2.imread(image1)

        # find the barcodes in the image and decode each of the barcodes
        barcodes = pyzbar.decode(image)

        # loop over the detected barcodes
        for barcode in barcodes:
                # extract the bounding box location of the barcode and draw the
                # bounding box surrounding the barcode on the image
                (x, y, w, h) = barcode.rect
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # the barcode data is a bytes object so if we want to draw it on
                # our output image we need to convert it to a string first
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type
                if barcodeData == "9783981305449":
                        print("It is a box of dry milk")
                else:
                        files = {'image':open(image1,'rb')}
                        try:
                                response = requests.post(url,files= files, timeout = 60)
                                print (response)
                        except:
                                pass

                # draw the barcode data and barcode type on the image
                text = "{} ({})".format(barcodeData, barcodeType)
                cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 255), 2)

        # show the output image
        cv2.imshow("Image", image)
        cv2.waitKey(3)
        continue
