#Image Processing

##Image read/display
###1. cv2.imread()

img1 = cv2.imread(path.join(IMG_FOLDER, "template.jpg"),cv2.IMREAD_GRAYSCALE)

cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
Note Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.

import matplotlib.pyplot as plt
plt.imshow(img1,cmap='Greys_r'),plt.show()

###2.Draw line and Circles


###3. Match Features
Python: cv2.ORB.detectAndCompute(image, mask[, descriptors[, useProvidedKeypoints]]) → keypoints, descriptors
Parameters:	
image – The input 8-bit grayscale image.
mask – The operation mask.
keypoints – The output vector of keypoints.
descriptors – The output descriptors. Pass cv::noArray() if you do not need it.
useProvidedKeypoints – If it is true, then the method will use the provided vector of keypoints instead of detecting them.

Keypoint is a class
1) print kp1[0].pt Location of the keypoint

DMatch is struct
    struct DMatch
    {
        DMatch() : queryIdx(-1), trainIdx(-1), imgIdx(-1),
                   distance(std::numeric_limits<float>::max()) {}
        DMatch( int _queryIdx, int _trainIdx, float _distance ) :
                queryIdx(_queryIdx), trainIdx(_trainIdx), imgIdx(-1),
                distance(_distance) {}
        DMatch( int _queryIdx, int _trainIdx, int _imgIdx, float _distance ) :
                queryIdx(_queryIdx), trainIdx(_trainIdx), imgIdx(_imgIdx),
                distance(_distance) {}

        int queryIdx; // query descriptor index
        int trainIdx; // train descriptor index
        int imgIdx;   // train image index

        float distance;

        // less is better
        bool operator<( const DMatch &m ) const;
    };

##Warp and Prospective
###cv2.warpPerspective()
warped_image = cv2.warpPerspective(image,new_matrix,size)










Others:
1. for i,layer in enumerate(gaussPyrMask):
