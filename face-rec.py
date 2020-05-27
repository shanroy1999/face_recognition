from PIL import Image
import face_recognition

image = face_recognition.load_image_file(r"C:\Users\Lenovo\Desktop\New folder\python\face_rec\team.jpg")
image

#Automatically find all faces in the image
face_locations = face_recognition.face_locations(image)
face_locations
# face_locations is now an array listing the co-ordinates of each face!

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:
    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

for face_location in face_locations:
    top, right, bottom, left = face_location
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
    #pil_image.save(f'{top}.jpg')

face_landmarks_list = face_recognition.face_landmarks(image)
face_landmarks_list

print(len(face_landmarks_list))
print(face_landmarks_list[0]['left_eye'])     #Location, outline of first person's left eye
print(face_landmarks_list[12]['nose_tip'])    #Location, outline of thirteenth person's nose tip

picture_of_me = face_recognition.load_image_file(r"C:\Users\Lenovo\Desktop\New folder\python\face_rec\screen.jpg")
picture_of_me

my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
print(my_face_encoding)

image_encoding = face_recognition.face_encodings(picture_of_me)[0]
print(my_face_encoding)

my_face_locations = face_recognition.face_locations(picture_of_me)
# face_locations is now an array listing the co-ordinates of each face!
print("I found {} face(s) in this photograph.".format(len(my_face_locations)))

for face_location in my_face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

for face_location in my_face_locations:
  my_face_image = picture_of_me[top:bottom, left:right]
  pil_image = Image.fromarray(my_face_image)
  pil_image.show()

print(my_face_encoding.shape, image_encoding.shape)

#Comparing the two faces
results = face_recognition.compare_faces([my_face_encoding], image_encoding)

if(results[0]==True):
  print("It is a picture of me")
else:
  print("It is a different picture")

obama = face_recognition.load_image_file(r"C:\Users\Lenovo\Desktop\New folder\python\face_rec\obama.jpg")
biden = face_recognition.load_image_file(r"C:\Users\Lenovo\Desktop\New folder\python\face_rec\biden.jpg")
obama_encoding = face_recognition.face_encodings(obama)[0]
biden_encoding = face_recognition.face_encodings(biden)[0]

face_locations = face_recognition.face_locations(obama)
# face_locations is now an array listing the co-ordinates of each face!

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:
  top, right, bottom, left = face_location

  obama_face_image = obama[top:bottom, left:right]
  pil_image = Image.fromarray(obama_face_image)
  pil_image.show()
