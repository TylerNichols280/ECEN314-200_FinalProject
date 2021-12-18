import ecen314_FP_masks as masks

from skimage.io import imread
from skimage.color import rgb2gray

"""======================= VARIABLES & INPUTS ======================="""
run = True  # for controlling image transformation & execution
filterOps = ['v', 'h', 'vh', 'lp', 'hp', 'bp', 'bc']  # filter options

imgName = input("Image file name (.png included): ")  # input image's name
imgColor = input("Color(c) or Greyscale(g)? ")  # input image's color type
print("Filter Options: weaken vertical lines (v), weaken horizontal lines (h), "
      "weaken vertical and horizontal lines (vh), lowpass filter (lp), "
      "highpass filter (hp), bandpass filter (bp), and bandcut filter (bc).")
feature = input("Filter choice: ")
img = imread(imgName)
for i in range(len(filterOps)):  # check validity of input feature
    if feature == filterOps[i]:
        break
    if i == (len(filterOps) - 1):
        print("Filter not recognized; exiting")
        run = False
"""======================= EXECUTION ======================="""
if run:  # exit if invalid feature was input
    if imgColor == "g":  # check validity of input color
        imgGrey = rgb2gray(img)  # convert image to greyscale, then mask
        masks.fourier_masker_grey(imgGrey, feature, 1)    
    elif imgColor == "c":
        masks.fourier_masker_color(img, feature, 1)
    else:  # default to grayscale if input color was invalid
        print("Color not recognized; executing in grayscale")
        imgGrey = rgb2gray(img)  # convert image to greyscale, then mask
        masks.fourier_masker_grey(imgGrey, feature, 1)   
