ECEN 314-200: Signals and Systems, Fall 2021   
Final Project: Image Editing through Fourier Transform Filtering   
Tyler Nichols   

Abstract   
My project focuses on the relationship between an image's typical time-domain form and its frequency-domain Fourier transform. By converting an input image to its Fourier
transform, altering that transform, then converting it back to the time domain, I examine the relationship between the forms and structures of both representations.

Python Files & Descriptions   
ecen314-200-FinalProject-NicholsTyler.py: Contains the final code to be run, which facilitates user inputs.   
ecen314-200-FP-filters.py: Defines the functions used to edit the Fourier transformations.   
ecen314-200-FP-masks.py: Defines the functions used to edit the selected image based on the user’s inputs and display the results of the edit.   

Other Files & Descriptions      
ecen314-200-FP-Report-NicholsTyler.docx: Word document containing information on this project and its final results.   
img1.png: Image file, square and dark with some prominent vertical and horizontal lines.   
img2.png: Image file, square and colorful with many small vertical and horizontal lines.   
img2-tall.png:  Image file, the same as img2.png, but edited to be rectangular in shape.   
img3.jpg: Image file, rectangular and colorful with few harsh lines.   
lines-dlr.png: Image file, square with only white and black diagonal lines from the top left to the bottom right.   
lines-drl.png: Image file, square with only white and black diagonal lines from the top right to the bottom left.   
lines-h.png: Image file, square with only white and black horizontal lines.   
lines-v.png: Image file, square with only white and black vertical lines.   

Usage Directions   
The following is a general guide to running the code; more detailed instructions are provided when the code is run.   
1.	Input name of desired image, including its file extension.   
2.	Input whether you want the transformation done in color or grayscale.   
3.	Input the filter you want to apply to the image (options provided by the code and in the Capabilities section below).   

Usage Restrictions   
Input images must be .png or .jpg files; other file formats are not expected and could result in unexpected outputs.   
Input file names must include the file extension.   
Input images must be stored within the same directory as the code, or the path to the image must be input instead of its name.   
Inputting a color choice aside from those listed in the code will cause it to transform the image in grayscale.   
Inputting a filter choice aside from those listed in the code will cause it to output the message "Filter not recognized; exiting", then exit.   

Capabilities
1.	Weaken vetical lines   
2.	Weaken horizontal lines   
3.	Blur the image (lowpass filter)   
4.	Reduce the image to a very general outline (highpass filter)   
5.	Reduce the image to a very general, blurry outline (bandpass filter)   
6.	Blur the image, but keep its outline relatively clear (bandcut filter)   
Note: the term "weaken" is used here to describe reducing and blurring the appearance of the weakened feature.   

Demonstration Videos   
Part 1: https://www.youtube.com/watch?v=MusWC2mM-8o   
Part 2: https://www.youtube.com/watch?v=_eD6WYHbX3k   
