import cv2
import Image
import ImageDraw

def detectFaces(image_name):
    img = cv2.imread(image_name)
    #face_cascade = cv2.CascadeClassifier("/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml")
    face_cascade = cv2.CascadeClassifier("C:/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml")	
    if img.ndim == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img 
	#if no-gray for 3, gray for 2

    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    #1.3~5 detect range
    result = []
    for (x,y,width,height) in faces:
        result.append((x,y,x+width,y+height))
    return result

def saveFaces(image_name):
    faces = detectFaces(image_name)
    if faces:
        #save face to sace_dir
        save_dir = image_name.split('.')[0]+"_faces"
        os.mkdir(save_dir)
        count = 0
        for (x1,y1,x2,y2) in faces:
            file_name = os.path.join(save_dir,str(count)+".jpg")
            Image.open(image_name).crop((x1,y1,x2,y2)).save(file_name)
            count+=1
	
def drawFaces(image_name):
    faces = detectFaces(image_name)
    if faces:
        img = Image.open(image_name)
        draw_instance = ImageDraw.Draw(img)
        for (x1,y1,x2,y2) in faces:
            draw_instance.rectangle((x1,y1,x2,y2), outline=(255, 0,0))
        img.save('drawfaces_'+image_name)

drawFaces('Oceans-Eleven.jpg')
			