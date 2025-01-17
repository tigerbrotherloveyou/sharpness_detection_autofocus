'''
@name    img_util.py
@brief   OpenCV Image processing utility functions
@author  Russell Wong, 2017
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
@name       usingCV2
@brief      Check whether the current OpenCV version is 2
@return     bool: True if the current version is 2
'''
def usingCV2():
    return checkCVVersion('2.')


'''
@name       usingCV3
@brief      Check whether the current OpenCV version is 3
@return     bool: True if the current version is 3
'''
def usingCV3():
    return checkCVVersion('3.')


'''
@name       checkCVVersion
@brief      Checks if the current OpenCV version is of a specified number
@param[in]  version: The version number to check
@return     bool: Whether the current version belongs to param version number
''' 
def checkCVVersion(version):
    return cv2.__version__.startswith(version)


'''
@name       plot
@brief      Uses matplotlib to plot and show image
@param[in]  img: The image to be plotted
@param[in]  title: The title of the image
@param[in]  cmap: Matplotlib colour options (e.g. cmap='gray')
                  Plots a colour image when cmap=None
@param[in]  maximize: Whether to maximize the window
'''
def plot(img, title, cmap=None, maximize=True):
    plt.switch_backend('TkAgg')
    if (maximize):
        fig_manager = plt.get_current_fig_manager()
        fig_manager.resize(*fig_manager.window.maxsize())
    plt.imshow(img, cmap=cmap)
    plt.title(title)
    plt.xticks([]), plt.yticks([])
    plt.show()


def plotPoints(points, title, maximize=True):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.switch_backend('TkAgg')
    if (maximize):
        fig_manager = plt.get_current_fig_manager()
        fig_manager.resize(*fig_manager.window.maxsize())
    plt.title(title)
    plt.scatter(x, y)
    plt.show()


def plotParabolas(coefficients, x_vals, title, max_x, max_y, maximize=True):
    x = []
    y = []
    y_vals = []
    for i in range(len(x_vals)-1):
        y_vals.append(coefficients[3*i]*x_vals[i]**2 + coefficients[3*i+1]*x_vals[i] + coefficients[3*i+2])
        for x_val in range(x_vals[i],x_vals[i+1]):
            x.append(x_val)
            y_val = coefficients[3*i]*x_val**2 + coefficients[3*i+1]*x_val + coefficients[3*i+2]
            y.append(y_val)
    y_vals.append(coefficients[3*i]*x_vals[len(x_vals)-1]**2 + coefficients[3*i+1]*x_vals[len(x_vals)-1] + coefficients[3*i+2])
    plt.switch_backend('TkAgg')
    if (maximize):
        fig_manager = plt.get_current_fig_manager()
        fig_manager.resize(*fig_manager.window.maxsize())
    plt.title(title)
    plt.scatter(x,y)
    plt.plot(x_vals, y_vals, color='r')
    plt.plot(max_x, max_y, 'bo')
    plt.show()

'''
@name       plotCubic
@brief      Plot cubic splines
@param[in]  coefficients: vector of coefficients of cubic equations
            x_vals: focus distance values from data points
            title: title of the plot
            max_x: x value of the maximum of the cubic spline
            max_y: y value of the maximum of the cubic spline
            maximize: whether the plot window is maximized
'''
def plotCubic(coefficients, x_vals, title, max_x, max_y, maximize=True):
    x = []
    y = []
    y_vals = []
    for i in range(len(x_vals)-1):
        y_vals.append(coefficients[4*i]*x_vals[i]**3 + coefficients[4*i+1]*x_vals[i]**2 + coefficients[4*i+2]*x_vals[i] + coefficients[4*i+3])
        for x_val in range(x_vals[i],x_vals[i+1]):
            x.append(x_val)
            y_val = coefficients[4*i]*x_val**3 + coefficients[4*i+1]*x_val**2 + coefficients[4*i+2]*x_val + coefficients[4*i+3]
            y.append(y_val)
    y_vals.append(coefficients[4*i]*x_vals[len(x_vals)-1]**3 + coefficients[4*i+1]*x_vals[len(x_vals)-1]**2 + coefficients[4*i+2]*x_vals[len(x_vals)-1] + coefficients[4*i+3])
    plt.switch_backend('TkAgg')
    if (maximize):
        fig_manager = plt.get_current_fig_manager()
        fig_manager.resize(*fig_manager.window.maxsize())
    plt.title(title, fontsize=36)
    plt.xlabel('Focus Distance [mm]', fontsize=24)
    plt.ylabel('Relative Sharpness Value', fontsize=24)
    plt.tick_params(labelsize=20)
    plt.scatter(x,y)
    plt.plot(x_vals, y_vals, color='r')
    plt.plot(max_x, max_y, 'bo')
    plt.show()

'''
@name       saveImageRGB
@brief      Writes an RGB image to a file
@param[in]  name: String representing relative file path and name for the image
@param[in]  img: RGB image to be saved
'''
def saveImageRGB(name, img):
    cv2.imwrite(name, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))


'''
@name       saveImageBW
@brief      Writes a black and white image to a file
@param[in]  name: String representing relative file path and name for the image
@param[in]  img: BW image to be saved
'''
def saveImageBW(name, img):
    cv2.imwrite(name, img)


'''
@name       readImageRGB
@brief      Reads an image to an RGB cv2 matrix
@param[in]  name: String representing relative file path and name for the image
@return     np.array: RGB image
'''
def readImageRGB(name):
    return cv2.cvtColor(cv2.imread(name, cv2.IMREAD_COLOR), cv2.COLOR_RGB2BGR)


'''
@name       readImageBW
@brief      Reads an image to a black and white cv2 matrix
@param[in]  name: String representing relative file path and name for the image
@return     np.array: BW image
'''
def readImageBW(name):
    return cv2.imread(name, cv2.IMREAD_GRAYSCALE)