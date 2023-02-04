def clip_values(x, min_val=None, max_val=None):
    """
    Return a new array with the values clipped. 
    If min_val is set, all values < min_val will be set to min_val
    If max_val is set, all values > max_val will be set to max_val
    Remember to return a new array, NOT to modify the input array. 
    Inputs: 
        x: the n-dimensional array to be clipped
        min_val : the minimum value in the returned array (if not None)
        max_val : the maximum value in the returned array (if not None)
    returns: an array with the same dimensions of X with values clipped
             to (min_val, max-val)
    """

    or_shape = x.shape
    new = x.flatten()
    if max_val is not None:
        for x in np.where(new > max_val)[0]:
            new[x] = max_val
    if min_val is not None:
        for x in np.where(new < min_val)[0]:
            new[x] = min_val
    return new.reshape(or_shape)
        


#############################################################
###                                                       ###
###                    Testing code.                      ###
###    !!! DO NOT MODIFY ANY CODE BELOW THIS POINT !!!    ###
###                                                       ###
#############################################################

import sys
import numpy as np
sys.path.append('../')

import test_utils as utils

def test_clip_values():

    x = np.linspace(0, 2, 10)
    x_orig = x.copy()

    ### Check for modification of input array
    recreate_msg = utils.gen_recreate_msg('clip_values', 1, 1.8)
    
    result = clip_values(x, min_val=1, max_val=1.8)
    
    utils.check_none(result, recreate_msg)
    utils.check_is_ndarray(result, recreate_msg)

    assert np.allclose(x, x_orig), \
        "\n Input array was modified.\n\n" + recreate_msg

    ### Check minimum value
    recreate_msg = utils.gen_recreate_msg('clip_values', 1)

    result = clip_values(x, min_val=1)
    
    utils.check_none(result, recreate_msg)
    utils.check_is_ndarray(result, recreate_msg)

    assert np.min(result) == 1.0,\
        "\n The minimum value of the array is not 1.0\n\n" \
        + recreate_msg

    ### Check maximum value
    recreate_msg = utils.gen_recreate_msg('clip_values', None, 1)

    result = clip_values(x, max_val=1)
    
    utils.check_none(result, recreate_msg)
    utils.check_is_ndarray(result, recreate_msg)

    assert np.max(result) == 1.0, \
        "\n The maximum value of the array is not 1.0\n\n" \
        + recreate_msg
    
    ### Check Both
    recreate_msg = utils.gen_recreate_msg('clip_values', 1.0, 1.5)

    result = clip_values(x, min_val=1.0, max_val=1.5)
    
    utils.check_none(result, recreate_msg)
    utils.check_is_ndarray(result, recreate_msg)

    assert np.max(result) == 1.5, \
    "\n The maximum value of the array is not 1.5\n\n"\
        + recreate_msg

    assert np.min(result) == 1.0, \
    "\n The minimum value of the array is not 1.0\n\n"\
        + recreate_msg
        