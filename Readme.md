# Steps to run it on Raspi

## Step1-
First follow this link to burn Raspbian with all the Computer Vision tool already installed. Because installing OpenCV and tensorflow is a messy thing to do on Raspberry Pi.
[Link](https://www.pantechsolutions.net/blog/pre-installed-os-for-raspberry-pi-for-free/)

## Step2 - 
Open Raspbian and locate home folder and create folder like this
"/home/pi/tflite/"

## Step3-
Open terminal. Move to "home/pi/tflite/" as a working directory by

```sh
cd "home/pi/tflite/"
```

## Step3 -
Install git using 

```sh
pip3 install  python-git
```

## Step4- Clone this repo

```sh
git clone "https://github.com/Boltuzamaki/Solve-for-Bharat-Hackathon-IISC-Banglore-2020-.git"
```

## Connect Pi cam to you Raspi and in setting activate Pi cam. (Watch tutorial or blog there are plenty on internet)

## Now install all additional libraries by

```sh
pip3 install requiremnts.txt
```

## At last run main.py 
```sh
pip3 install main.py
```


### If anyone if facing any problem they can raise an issue cheers!
