import numpy as np 
import cv2 
import matplotlib.pyplot as plt

img = cv2.imread("data/map.png")
img = np.array(img)

def find_red_pixels(img, upper_threshold=100, lower_threshold=50):
    """
    This is a functions that detects the red pixels from a picture and returnes a 2D array with the detected red pixels 
    in white(1) and the rest of the pixels are turned black(0) 
    Argument(s) : 
    ---------------
    - img : The picture that user uploads in the program
    - upper_threshold : a variable used for detecting the color type of the red pixels (how red it is) and is predefined as 100
    - lower_threshold : a variable used for detecting the color type of the blue and green pixels (how blue or green exists in red) and is predefined as 50
    ---------------
    Note(s) : This program will convert the detected red pixels into white and rest in black resulting in a black and white picture 
    ---------------
    Return(s) : This function return's a 2D array worth of red and black pixels 
    """
    
    output_pixels = np.zeros((img.shape[0], img.shape[1]))
    for i in range(img.shape[0]): 
        for j in range(img.shape[1]):
            if img[i,j,2] > upper_threshold and img[i,j,1] < lower_threshold and img[i,j,0] < lower_threshold:
                output_pixels[i,j] = 255

    return output_pixels 
"""
img = find_red_pixels(img)
plt.imshow(img, cmap = "gray")
plt.draw()
plt.show()
cv2.waitKey(0)
"""
mg = cv2.imread("data/map.png")
img = np.array(img)

def find_cyan_pixels(img, upper_threshold=100, lower_threshold=50):
    """
    This is a functions that detects the cyan pixels from a picture and returnes a 2D array with the detected cyan pixels 
    in white(1) and the rest of the pixels are turned black(0) 
    Argument(s) : 
    ---------------
    - img : The picture that user uploads in the program
    - upper_threshold : a variable used for detecting the color type of the cyan pixels (how blue it is) and is predefined as 100
    - lower_threshold : a variable used for detecting the color type of the red and green pixels (how red or green exists in cyan)) and is predefined as 50
    ---------------
    Note(s) : This program will convert the detected cyan pixels into white and rest in black resulting in a black and white picture 
    ---------------
    Return(s) : This function return's a 2D array worth of cyan and black pixels 
    """
    output_pixels = np.zeros((img.shape[0], img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j,0] > upper_threshold  and img[i,j,1] > upper_threshold and img[i,j,2] < lower_threshold:
                output_pixels[i,j] = 255

    return output_pixels 

"""
img = find_cyan_pixels(img)
plt.imshow(img, cmap = "gray")
plt.draw()
plt.show()
cv2.waitKey(0)
"""

def detect_connected_components(img):
    """
    This is a functions that detects connected components from the outputs of the previous functions (find_red_pixels and find_cyan_pixels)
    and the number of pixels that exists in that connected component and returns the result 
    
    Argument(s) : 
    ---------------
    - img : the output of the previous functions (find_red_pixels and find_cyan_pixels) which user shall choose which one to pass to the function 
    ---------------
    Note(s) : the user decides to determine wether the red or cyan pixels should be the input of this function 
    ---------------
    Return(s) : a list of all connected components with the number of pixels whithin that connected component 
    ---------------
    Algorithm : The algorithm described in the Assessment Information pdf is the same as this algorithm 
    except for one change, instead of the for loop (for each 8-neighbour n(s,t) of q(m,n) do...) and the if condition after it 
    I used 8 if conditions to detect the 8 neighbour of the q . 
    """
    img = np.array(img, dtype=int)
    Mark = np.zeros_like(img,dtype=int)
    q = []
    connected_components = []
    region_color = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] == 255.0 and Mark[i,j] == 0:
                region_color += 1
                Mark[i,j] = region_color
                q.append([i,j])
                count = 0
                while len(q) != 0 : 
                    count += 1
                    [s,t] = q[0]
                    s = q[0][0]
                    t = q[0][1]
                    q.pop(0)
                    
                    if s != 0 and t != img.shape[1]-1 and img[s-1,t+1] == 255 and Mark[s-1,t+1] == 0 :
                        Mark[s-1,t+1] = region_color
                        q.append([s-1,t+1])
                    if s != 0 and img[s-1,t] == 255 and Mark[s-1,t] == 0:
                        Mark[s-1,t] = region_color
                        q.append([s-1,t])
                    if s != 0 and t != 0 and img[s-1,t-1] == 255 and Mark[s-1,t-1] == 0 :
                        Mark[s-1,t-1] = region_color
                        q.append([s-1,t-1])
                    if t != img.shape[1]-1 and img[s,t+1] == 255 and Mark[s,t+1] == 0 :
                        Mark[s,t+1] = region_color
                        q.append([s,t+1])
                    if t != 0 and img[s,t-1] == 255 and Mark[s,t-1] == 0 :
                        Mark[s,t-1] = region_color
                        q.append([s,t-1])
                    if s != img.shape[0]-1 and t != img.shape[1]-1 and img[s+1,t+1] == 255 and Mark[s+1,t+1] == 0:
                        Mark[s+1,t+1] = region_color
                        q.append([s+1,t+1])
                    if s != img.shape[0]-1 and img[s+1,t] == 255 and Mark[s+1,t] == 0 :
                        Mark[s+1,t] = region_color
                        q.append([s+1,t])
                    if s != img.shape[0]-1 and t != 0 and img[s+1,t-1] == 255 and Mark[s+1,t-1] == 0 :
                        Mark[s+1,t-1] = region_color
                        q.append([s+1,t-1])
                connected_components.append(count)
            
    with open('cc-output-2a.txt', 'w') as file : 
        for m in range(len(connected_components)) : 
            file.write(f" Connected Component {m+1}, number of pixels = {connected_components[m]}\n")
        file.write(f"Total number of connected components = {len(connected_components)}")
    
    detect_connected_components_sorted(Mark) 
 

def detect_connected_components_sorted(Mark):
    """
    This is a functions that sorts the detects connected components from the output of the previous functions (detect_connected_components)
    and returns a list with the sorted connected components based on the number of pixels on them 
    
    Argument(s) : 
    ---------------
    - Mark : the sorted list of the connected components 
    ---------------
    Note(s) : this is a function that will only sort the list of connected components and doesn't add or remove anything from the input 
    ---------------
    Return(s) : a list of all sorted connected components based on the number of pixels within that connected component
    """
    
    my_list = list(np.unique(Mark, return_counts=True))
    my_list_2 = my_list[1].sort()
    

    
    #with open('cc-top-2b.txt', 'w') as file : 
       

img = find_red_pixels(img) 
detect_connected_components(img)

    
