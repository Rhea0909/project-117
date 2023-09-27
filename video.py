import os
import cv2

path = "Images/"
images = []

for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    
    if ext in ['.gif', '.png', '.jpeg', '.jpg', '.jfif']:
        filename = path + "/" + file
        images.append(filename)

count = len(images)
 
frame = cv2.imread(images[0])
height,width,layers = frame.shape
size = (width,height)

out = cv2.VideoWriter('album.avi', cv2.VideoWriter_fourcc(*'DIVX'),0.8, size)
for i in range(0,count):
    frame = cv2.imread(images[i])
    out.write(frame)
out.release()
print("Done")

