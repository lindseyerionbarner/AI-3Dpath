
import numpy as np
import tifffile 
import cv2

def nuc_cyto_rgb(nuc, cyto, file_name, save_path):
    """Convert nuc/cyto enface images to RGB-stacked image for deep learning algorithm
    Save resulting .tiff image to desired path

    Parameters
    ----------
    nuc : np.ndarray, 16-bit
    cyto : np.ndarray, 16-bit

    Returns
    -------
    np.ndarray, 3 channel 16-bit

    """

    im = np.zeros((nuc.shape[0],nuc.shape[1],3), dtype = 'uint16')
    im[:,:,0] = nuc
    im[:,:,1] = cyto
    tifffile.imwrite(save_path + file_name + '.tiff', im, photometric = 'rgb')

    return im


def pyr_rgb(im, img_resolution, file_name, save_path):

    """Save nuc-cyto_RGB image into pyramidal format for deep learning algorithm
    Save resulting .tif image to desired path

    Parameters
    ----------
    im : np.ndarray, 3-channel 16-bit
    img_resolution: float, indicates sampling in um/px of im
    file_name : str
    save_path: str

    Returns
    -------
    saves np.ndarray (3 channel uint8)

    """

    im = im.astype('float64')

    ## Scale channel 0 to 0-255 (without clipping)
    im[:,:,0] = im[:,:,0]/np.max(im[:,:,0])
    im[:,:,0] = im[:,:,0]*255
    ## Scale channel 1 to 0-255 (without clipping)
    im[:,:,1] = im[:,:,1]/np.max(im[:,:,1])
    im[:,:,1] = im[:,:,1]*255

    ## Set as uint8
    im = im.astype('uint8')

    h, w, s = im.shape
    px_per_cm = 10000/img_resolution #inverse of image resolution in cm/px
    level = 0


    with tifffile.TiffWriter(save_path + file_name + '.tif', bigtiff=True) as tif: #we want the file to safe as .tif, not .tiff
        while True:    
            options = dict(tile = (int(256/2**level),int(256/2**level)))
            tif.write(im, software='Glencoe/Faas pyramid', metadata=None,
                resolution=(px_per_cm/(2**level), px_per_cm/(2**level), 'CENTIMETER'),
                **options)
            tif.write(im[::2,::2,:], subfiletype=1, **options)
            if max(w, h) < 256 or level >= 4: #Not sure why it only works for levels 1-4. should troubleshoot this later
    #                     print(level)
                break
            level += 1
            w //= 2
            h //= 2
            im = cv2.resize(im, dsize=(w, h), interpolation=cv2.INTER_LINEAR)