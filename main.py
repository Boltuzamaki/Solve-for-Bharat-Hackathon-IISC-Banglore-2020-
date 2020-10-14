from tkinter import *
import speech_recognition as sr
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import subprocess
from PIL import Image
import pytesseract
import pyttsx3
import requests
  


def barcode():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
            help="path to output CSV file containing barcodes")
    args = vars(ap.parse_args())

    # initialize the video stream and allow the camera sensor to warm up
    print("[INFO] starting video stream...")
    # vs = VideoStream(src=0).start()
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)

    # open the output CSV file for writing and initialize the set of
    # barcodes found thus far
    csv = open(args["output"], "w")
    found = set()

    # loop over the frames from the video stream
    while True:
            # grab the frame from the threaded video stream and resize it to
            # have a maximum width of 400 pixels
            frame = vs.read()
            frame = imutils.resize(frame, width=400)

            # find the barcodes in the frame and decode each of the barcodes
            barcodes = pyzbar.decode(frame)

            # loop over the detected barcodes
            for barcode in barcodes:
                    # extract the bounding box location of the barcode and draw
                    # the bounding box surrounding the barcode on the image
                    (x, y, w, h) = barcode.rect
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                    # the barcode data is a bytes object so if we want to draw it
                    # on our output image we need to convert it to a string first
                    barcodeData = barcode.data.decode("utf-8")
                    barcodeType = barcode.type
                    if barcodeData == 8904109464867:
                        print("This is Dant Kanti toothpaste")

                    if barcodeData == "":
                        continue
                    else:
                        url = "http://172.27.74.255//dashboard//save_image.php"
                        files = {'image':open(frame,'rb')}
                        try:
                                response = requests.post(url,files= files, timeout = 60)
                                print (response)
                        except:
                                pass
                        
                        
                        



                        

                    # draw the barcode data and barcode type on the image
                    text = "{} ({})".format(barcodeData, barcodeType)
                    cv2.putText(frame, text, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                    # if the barcode text is currently not in our CSV file, write
                    # the timestamp + barcode to disk and update the set
                    if barcodeData not in found:
                            csv.write("{},{}\n".format(datetime.datetime.now(),
                                    barcodeData))
                            csv.flush()
                            found.add(barcodeData)

            # show the output frame
            cv2.imshow("Barcode Scanner", frame)
            key = cv2.waitKey(1) & 0xFF
     
            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                    break
              

    # close the output CSV file do a bit of cleanup
    print("[INFO] cleaning up...")
    csv.close()
    cv2.destroyAllWindows()
    vs.stop()



def Audio_text(sound):
    AUDIO_FILE = (sound) 
      
    # use the audio file as the audio source 
      
    r = sr.Recognizer() 
      
    with sr.AudioFile(AUDIO_FILE) as source: 
        #reads the audio file. Here we use record instead of 
        #listen 
        audio = r.record(source)   
      
    try: 
        print( r.recognize_google(audio)) 
      
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
      
    except sr.RequestError as e: 
         print("Could not request results from Google Speech  Recognition service {0}".format(e))

    return r.recognize_google(audio)

root = Tk()
root.geometry("1480x1400")

def detection_algo():
    
    # Path to a Python interpreter that runs any Python script
    # under the virtualenv /path/to/virtualenv/
    python_bin = "/home/pi/tflite/tflite1-env/bin/python3"

    # Path to the script that must run under the virtualenv
    script_file = "/home/pi/tflite/script.py"

    subprocess.Popen([python_bin, script_file])
   


def detect():
    Audio_text("1.wav")
    detection_algo()
    
def describe():
     k = Audio_text("6.wav")
     if(k=="advantage"):
         barcode()
         
def descibe_obj():
    
     # initialisation 
    engine = pyttsx3.init() 
      
    # testing O
    engine.say("A laptop also laptop computer, often called a notebook, is a small, portable personal computer") 
    engine.say("Say Interested for more information") 
    engine.runAndWait() 
        
def text():
    img =Image.open ("sample.png")
    text = pytesseract.image_to_string(img, config="")
    print (text)


   
    
# Creating button 
b1 = Button(root, text = "Object Detection", fg = "red", command = detect)
b2 = Button(root, text = "Product Information", fg = "blue", command = describe)
b4 = Button(root, text = "Text Extract", fg = "green", command = text)
b5 = Button(root, text = "Product info voice", fg = "black", command = descibe_obj)




b1.pack(side =LEFT , anchor = "nw")
b2.pack(side =LEFT , anchor = "nw")
b4.pack(side =LEFT , anchor = "nw")
b5.pack(side =LEFT , anchor = "nw")



root.mainloop()

