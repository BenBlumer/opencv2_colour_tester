
# Colour track tester. 
# Copyright (C) 2014 Benjamin Blumer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import cv2
import numpy as np


def get_trackbar_positions(cam1_window_name):
    """ Get the positions of the h,s,v, and switch trackbars in cam1_window_name.

    args:
        cam1_window_name: The name of the OpenCV Window we want the trackbars on.

    returns:
        h_min, s_min, v_min, h_max, s_max, v_max: the min/max hue saturation
         vals.
        switch: 0 or 1. 0 if the user wants the original image, 1 if the user
          wants an image filtered to be between the HSV values.
    """

    h_min = cv2.getTrackbarPos('H_min', cam1_window_name)
    s_min = cv2.getTrackbarPos('S_min', cam1_window_name)
    v_min = cv2.getTrackbarPos('V_min', cam1_window_name)
    switch = cv2.getTrackbarPos(
        '0 : Original \n1 : Thresholded', cam1_window_name)
    h_max = cv2.getTrackbarPos('H_max', cam1_window_name)
    s_max = cv2.getTrackbarPos('S_max', cam1_window_name)
    v_max = cv2.getTrackbarPos('V_max', cam1_window_name)
    return h_min, s_min, v_min, h_max, s_max, v_max, switch


def create_hsv_sliders(cam1_window_name):
    """
    Add HSV min/max and a switch slider to cam1_window_name.

    args:
        cam1_window_name: an openCV window name. The window must already exist!
    returns: None.
    """
    cv2.createTrackbar('H_min', cam1_window_name, 0, 180, nothing)
    cv2.createTrackbar('S_min', cam1_window_name, 0, 255, nothing)
    cv2.createTrackbar('V_min', cam1_window_name, 0, 255, nothing)
    cv2.createTrackbar('H_max', cam1_window_name, 0, 180, nothing)
    cv2.createTrackbar('S_max', cam1_window_name, 0, 255, nothing)
    # create switch for ON/OFF functionality
    cv2.createTrackbar('V_max', cam1_window_name, 0, 255, nothing)
#     switch = '0 : Original \n1 : Thresholded'
    cv2.createTrackbar(
        '0 : Original \n1 : Thresholded', cam1_window_name, 0, 1, nothing)
    return None


def return_thresholded_image(org_img, h_min, s_min, v_min, h_max, s_max, v_max):
    """ Filter everything out of the h,s,v ranges on org_img.

    args:
        org_img: an RGB image captured from a webcam.
        h_min, s_min, v_min, h_max, s_max, v_max: the min/max hue, saturation
          and val values.
    returns:
        threshold_img: an image that has had all HSV values outside of the range
          filtered out.

    """
    blur = cv2.medianBlur(org_img, 5)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    color = cv2.inRange(
        hsv, np.array((h_min, s_min, v_min)), np.array((h_max, s_max, v_max)))
    img_erode = cv2.erode(color, None, iterations=3)
    threshold_img = cv2.dilate(img_erode, None, iterations=3)
    return threshold_img


def return_camera_image(camera, cam1_window_name):
    """ Return either the original camera image, or one thresholded to the HSV
        values set on the sliders in cam1_window_name. These sliders must already be
        added using create_hsv_sliders().
        """
    h_min, s_min, v_min, h_max, s_max, v_max, switch = get_trackbar_positions(
        cam1_window_name)
    _,org = camera.read()
    if switch == 0:
        return org
    else:
        return return_thresholded_image(
            org, h_min, s_min, v_min, h_max, s_max, v_max)
def prepare_cv2_window(window_name):
    """Create a window named window_name and add min/max H,S,V sliders and 
    a original/threshold switch"""
    cv2.namedWindow(window_name)
    create_hsv_sliders(window_name)

def nothing(x):
    """Dummy function to call when an OpenCV slider changes"""
    pass

cam1_window_name = "camera_1"
#cam2_window_name = "camera_2"
prepare_cv2_window(cam1_window_name)
#prepare_cv2_window(cam2_window_name)

cam1 = cv2.VideoCapture(0)
#cam2 = cv2.VideoCapture(1)


while(1):

    cam1_img = return_camera_image(cam1, cam1_window_name)
#    cam2_img = return_camera_image(cam2, cam2_window_name)
    cv2.imshow(cam1_window_name, cam1_img)
    cv2.imshow(cam2_window_name, cam2_img)
#    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()
