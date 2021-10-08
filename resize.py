import cv2
import glob

dirs = glob.glob('*.jpg', recursive=False)
for item in dirs:
    getimg = cv2.imread(item,0)
    resized_getimg = cv2.resize(getimg,(100,100))
    print("Resized:",item," \n  Has new resolution:  ", resized_getimg.shape)
    cv2.imshow("Resized",resized_getimg)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+item,resized_getimg)
