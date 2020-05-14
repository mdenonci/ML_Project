#=========================================
# Y. TCHABI - M. DENONCIN
#
# Image Inpainting
#
#=========================================

"""

We use CIFAR10 Extraction Method


"""

import numpy as np

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


def extractBatch(batchNb):
    # Each Batch contains 10000 images
    batch = unpickle("data_batch_"+str(batchNb))
    return batch


def extractData(batch):
    data = batch[b'data']
    return data

def extractImage(imageIndex,data):
    imageVector = data[imageIndex]
    redVector = imageVector[0:1024]
    greenVector = imageVector[1024:2048]
    blueVector = imageVector[2048:3072]
    image = []
    for y in range(0,32):
        image.append([])
        for x in range(0,32):
            image[y].append([])
            image[y][x] = [redVector[(32*y)+x], greenVector[(32*y)+x], blueVector[(32*y)+x]]

    image = np.array(image)
    return image

