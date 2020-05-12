#=========================================
# Y. TCHABI - M. DENONCIN
#
# Image Inpainting
#
#=========================================

"""

We use CIFAR10 Extraction Method


"""

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict