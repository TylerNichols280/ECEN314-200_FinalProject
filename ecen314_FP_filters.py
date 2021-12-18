import numpy as np
from PIL import Image, ImageDraw

def shrink_lines(fourier, feature, h, w, i):
    # shrinks vertical lines
    if feature == "v":  # wipe fourier's central horizontal line
        fourier[(h-3):(h+3), :(w-5)] = i
        fourier[(h-3):(h+3),-(w-5):] = i
    elif feature == "h":  # wipe fourier's central vertical line
        fourier[:(h-5), (w-3):(w+3)] = i
        fourier[-(h-5):, (w-3):(w+3)] = i
    elif feature == "vh":   # both previous changes
        fourier[(h-3):(h+3), :(w-5)] = i
        fourier[(h-3):(h+3),-(w-5):] = i
        fourier[:(h-5), (w-3):(w+3)] = i
        fourier[-(h-5):, (w-3):(w+3)] = i
    return fourier

def lowpass_filter(img, fourier, i, big=False):
    # filter fourier by multiplying it w/ image of filled circle
    if big:  # creates larger filter
        h = int((np.shape(img)[0])*3/4)
        w = int((np.shape(img)[1])*3/4)
    else:
        h = int((np.shape(img)[0])/3)
        w = int((np.shape(img)[1])/3)
    imgNp = np.array(img)
    x,y = imgNp.shape[1], imgNp.shape[0]
    # size of circle
    rad = min(h, w)
    e_x,e_y = rad, rad
    # create filter by drawing a circle
    circle=((x/2)-(e_x/2),(y/2)-(e_y/2),(x/2)+(e_x/2),(y/2)+(e_y/2))
    # inside circle = 1; outside = 0
    lowpass = Image.new("L",(imgNp.shape[1], imgNp.shape[0]),color=0)
    draw1 = ImageDraw.Draw(lowpass)
    draw1.ellipse(circle, fill=1)
    # multiply fourier & filter; leaves only what's inside circle
    filtered = np.multiply(fourier,np.array(lowpass))
    return filtered

def highpass_filter(img, fourier, i, big=False):
    # filter fourier by multiplying it w/ image of blank circle
    if big:  # creates larger filter
        h = int((np.shape(img)[0])*3/4)
        w = int((np.shape(img)[1])*3/4)
    else:
        h = int((np.shape(img)[0])/3)
        w = int((np.shape(img)[1])/3)
    imgNp = np.array(img)
    x,y = imgNp.shape[1], imgNp.shape[0]
    # size of circle
    rad = min(h, w)
    e_x,e_y = rad, rad
    # create filter by drawing circle
    circle=((x/2)-(e_x/2),(y/2)-(e_y/2),(x/2)+(e_x/2),(y/2)+(e_y/2))
    # inside circle = 0; outside = 1
    highpass = Image.new("L",(imgNp.shape[1],imgNp.shape[0]),color=1)
    draw1 = ImageDraw.Draw(highpass)
    draw1.ellipse(circle, fill=0)
    # multiply fourier & filterl leaves only what's outside circle
    filtered = np.multiply(fourier,np.array(highpass))
    return filtered