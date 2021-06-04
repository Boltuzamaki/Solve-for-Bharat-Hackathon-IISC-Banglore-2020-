# Steps to run it on Raspi

## In short 
<img src="https://github.com/Boltuzamaki/Solve-for-Bharat-Hackathon-IISC-Banglore-2020-/blob/master/pic/solveforbharat.gif" height="400" width="600" />

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

## Step4 -
Install git using 

```sh
pip3 install  python-git
```

## Step5- 
Clone this repo

```sh
git clone "https://github.com/Boltuzamaki/Solve-for-Bharat-Hackathon-IISC-Banglore-2020-.git"
```

## Step6- 
Connect Pi cam to you Raspi and in setting activate Pi cam. (Watch tutorial or blog there are plenty on internet)

## Step7- 
Now install all additional libraries by

```sh
pip3 install requirements.txt
```

## Step8- 
At last run main.py 
```sh
python3 main.py
```


### If anyone is facing any problem they can raise an issue cheers!
