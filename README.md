# cursor2000
This is a system that I have wrote in Python/Opencv that if you leave the room with the lights on its gonna curse at you.(pretty interesting)

So I've used the Opencv's own pre-trained person detection model to see if anyone is in the room or not and I used contours in the binary threshold to figure out if the lights are on or off.

Dependencies

First of all Opencv should be installed
pip install opencv-python

After installing Opencv install playsound package for playing mp3 files
pip install playsound

And lastly you have to install imutils package, this package is extra tools for working with videos and pictures
pip install imutils

Usage

cd into the files where you have stored it
cd cursor2000

then run the program
python3 shtV1.py

Extra Information

I've used opencv's own pre-trained person detection model and using this model has its own pros and cons.
the pros are that its very simple to use, but it has some cons that makes the system hard to work like it glitches sometimes and for no reason it doesn't detects the person the person that is in the room and that trigers the curse function.
And I have used the contours in the binary threshold method to figure out if the light is on or off which turned out to work fine but there is a main problem with it, when you turn the lights off cause your(almost everyones) camera is rolling shutter sometimes it will still curse at you :)
I'm going to improve this code and maybe make a V2 version of it where I've bought some sensors to detect the entrance and exit of people.
And as you can see I've imported the threading package but I have never used it, I'm going to upgrade the code and use the package in the next upgrades I was just to lazy to remove(and forgot).
