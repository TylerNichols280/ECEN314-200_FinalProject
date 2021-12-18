import ecen314_FP_filters as filt

import numpy as np
import matplotlib.pyplot as plt

def fourier_masker_grey(img, feature, i): 
    # find image's dimensions
    h = int((np.shape(img)[0])/2)
    w = int((np.shape(img)[1])/2)
    # find image's fourier
    fourierOrig = np.fft.fftshift(np.fft.fft2(img))
    fourier = np.fft.fftshift(np.fft.fft2(img))
    # filter fourier
    if feature == "lp":
        fourier = filt.lowpass_filter(img, fourier, i)
    elif feature == "hp":
        fourier = filt.highpass_filter(img, fourier, i)
    elif feature == "bp":
        fourier = filt.lowpass_filter(img, fourier, i, big=True)
        fourier = filt.highpass_filter(img, fourier, i)
    elif feature == "bc":
        fourierCenter = filt.lowpass_filter(img, fourier, i)
        fourier = filt.highpass_filter(img, fourier, i, big=True)
        fourier = fourier + fourierCenter
    else:
        fourier = filt.shrink_lines(fourier, feature, h, w, i)
    fig, ax = plt.subplots(2,2,figsize=(15,15))
    # display original & filtered images
    ax[0, 0].imshow(img, cmap = 'gray')
    ax[0, 0].set_title('Original Image', fontsize = 15);
    ax[1, 0].imshow(abs(np.fft.ifft2(fourier)), cmap='gray')
    ax[1, 0].set_title('Filtered Image', fontsize = 15);
    # display original & filtered fouriers
    ax[0, 1].imshow(np.log(abs(fourierOrig)), cmap='gray')
    ax[0, 1].set_title('Original Fourier', fontsize = 15)
    ax[1, 1].imshow(np.log(abs(fourier)), cmap='gray')
    ax[1, 1].set_title('Filtered Fourier', fontsize = 15);
    
def fourier_masker_color(img, feature, i):  
    # find image's dimensions
    h = int((np.shape(img)[0])/2)
    w = int((np.shape(img)[1])/2)
    transformed_channels = []
    for j in range(3):  # transform each color separately
        # defined & filter fourier
        fourier = np.fft.fftshift(np.fft.fft2((img[:, :, j])))
        if feature == "lp":
            fourier = filt.lowpass_filter(img, fourier, i)
        elif feature == "hp":
            fourier = filt.highpass_filter(img, fourier, i)
        elif feature == "bp":
            # big lowpass + small highpass = bandpass
            fourier = filt.lowpass_filter(img, fourier, i, big=True)
            fourier = filt.highpass_filter(img, fourier, i)
        elif feature == "bc":
            # big highpass + small lowpass = bandcut
            fourierCenter = filt.lowpass_filter(img, fourier, i)
            fourier = filt.highpass_filter(img, fourier, i, big=True)
            fourier = fourier + fourierCenter
        else:
            fourier = filt.shrink_lines(fourier, feature, h, w, i)
        transformed_channels.append(abs(np.fft.ifft2(fourier)))
    # combine each color's filtered fouriers
    final_image = np.dstack([transformed_channels[0].astype(int), 
                             transformed_channels[1].astype(int), 
                             transformed_channels[2].astype(int)])
    
    fig, ax = plt.subplots(1, 2, figsize=(15, 15))
    # show original image
    ax[0].imshow(img)
    ax[0].set_title('Original Image', fontsize = 15)
    ax[0].set_axis_off()
    # show filtered image
    ax[1].imshow(final_image)
    ax[1].set_title('Filtered Image', fontsize = 15)
    ax[1].set_axis_off()
    fig.tight_layout()  # display images in tight layout