
Colour track tester. 
Copyright (C) 2014 Benjamin Blumer

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.




OpenCV has wonderful features for tracking objects by colour. However, it can be tricky to figure out exactly which minimum and maximum HSV values you need to capture only the object you're trying to capture. That's what this is here for!

First of all: you require OpenCV2 to be installed. 

Then run this script (make sure your camera is plugged in!). You can toggle between the image that's filtered by the specified HSV values and the original camera image. 

You can also add additional cameras in case you're trying to do this for a system where you're looking at the same object from multiple cameras. Just look at the cam2 parts that I've commented out in the code.
