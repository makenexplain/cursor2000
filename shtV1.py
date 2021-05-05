"""MIT License

Copyright (c) 2021 makenexplain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import cv2
import threading
from playsound import playsound
from time import sleep
import imutils


vid = cv2.VideoCapture(0)
aud = ["dshit.mp3", "die.mp3", "dum.mp3"]
#The main function that will process all the stuff(duh)
def main():
    
    audnm = 0
    sleep(2)

    while True:
        _, frame = vid.read()        #Reading the camera feed we stored in vid variable

        cnt = []
        ppl = ()

        frame = imutils.resize(frame, width=450)
        gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, th1 = cv2.threshold(gr, 127, 255, cv2.THRESH_BINARY)        

        hog = cv2.HOGDescriptor()        #Using the opencv pre-trained person detection model
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        cnt, hi = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for ar in cnt:
            area = cv2.contourArea(ar)

        ppl, wgh = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)
        print(ppl)
        person = 0
        
        for x, y, w, h in ppl:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        cv2.imshow("frame", frame)
        cv2.imshow("th1", th1)

        if cv2.waitKey(1) == ord("q"):
            cv2.destroyAllWindows()
            break

        if cnt != [] and ppl == ():
            sleep(1)
            if area >=1000:
                playsound(aud[audnm])
                cnt = []
                ppl = ()
                if audnm == 2:
                    audnm = 0
                else:
                    audnm = audnm+1  

main()