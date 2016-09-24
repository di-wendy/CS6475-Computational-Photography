def find_edges(image):
    # TODO: implement your own edge detector
    arrayx = a4.gradientX(image)
    arrayy = a4.gradientX(image)
    norm_img_x = a4.normalizeImage(arrayx)
    norm_img_y = a4.normalizeImage(arrayy)
    
    norm_img_x = supressedX(norm_img_x)
    norm_img_y = supressedY(norm_img_y)
    
    cv2.imwrite(path.join(IMG_FOLDER, "test.jpg"), norm_img_x)
    
    
    height, width = image.shape
    
    result = np.zeros(shape=(height,width),dtype=float)
    grad_x = norm_img_x.astype(np.float)
    grad_y = norm_img_y.astype(np.float)
    
    
    for i in range(height-1):
        for j in range(width-1):
            result[i][j] = np.sqrt(grad_x[i][j]**2+grad_y[i][j]**2)

    return result
