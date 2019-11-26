# Finding the black shapes
In this we’ll learn how to use create a simple Python + OpenCV script to Finding the black shapes in the given image.  

**inRange:**  
Detecting these black shapes is actually very easy using the cv2.inRange  function: we define a lower  and an upper  boundary points in the BGR color space. Remember, OpenCV stores images in BGR order rather than RGB.

Our lower  boundary consists of pure black, specifying zeros for each of the Blue, Green, and Red channels, respectively.

And our upper  boundary consists of a very dark shade of gray, this time specifying 15 for each of the channels.


**commands to run**
- python finding_shapes.py -i finding_shapes_example.png