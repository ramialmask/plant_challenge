import numpy as np
import cv2
import os


def green_dominance(image:np.array) -> np.array:
    """
    Returns a mask of an image where all pixels for which greenval > blueval, redval
    Args:
        image (np.array)    : Input image
    Returns:
        mask                : Binary mask
    """
    gr = image[:,:,1] > image[:,:,0] # pixels where green > red
    gb = image[:,:,1] > image[:,:,2] # pixels where green > blue

    mask = gr * gb # mask where green pixels > red and blue
    return mask

