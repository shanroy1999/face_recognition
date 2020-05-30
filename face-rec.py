from PIL import Image, ImageDraw
import face_recognition
import cv2
import os

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
    #pil_image.show()
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

obama = face_recognition.load_image_file(r"C:\Users\Lenovo\Desktop\New folder\python\face_rec\Known Faces\obama.jpg")
ronaldo = face_recognition.load_image_file(r"C:\Users\Lenovo\Desktop\New folder\python\face_rec\Known Faces\r5.jpg")
obama_encoding = face_recognition.face_encodings(obama)[0]
ronaldo_encoding = face_recognition.face_encodings(ronaldo)[0]

face_locations = face_recognition.face_locations(obama)
# face_locations is now an array listing the co-ordinates of each face!

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:
  top, right, bottom, left = face_location

  obama_face_image = obama[top:bottom, left:right]
  pil_image = Image.fromarray(obama_face_image)
  pil_image.show()

img_of_Ronaldo = face_recognition.load_image_file(r"C:\Users\Lenovo\Desktop\New folder\python\face_rec\Known Faces\r5.jpg")
ronaldo_face_encodings = face_recognition.face_encodings(img_of_Ronaldo)[0]

img_of_Messi = face_recognition.load_image_file(r"C:\Users\Lenovo\Desktop\New folder\python\face_rec\Known Faces\m1.jpg")
messi_face_encodings = face_recognition.face_encodings(img_of_Messi)[0]

img_of_Federer = face_recognition.load_image_file(r"C:\Users\Lenovo\Desktop\New folder\python\face_rec\Known Faces\rf1.jpg")
federer_face_encodings = face_recognition.face_encodings(img_of_Federer)[0]

img_of_Bill = face_recognition.load_image_file(r"C:\Users\Lenovo\Desktop\New folder\python\face_rec\Known Faces\Bill Gates.jpg")
bill_face_encodings = face_recognition.face_encodings(img_of_Bill)[0]

img_of_Steve = face_recognition.load_image_file(r"C:\Users\Lenovo\Desktop\New folder\python\face_rec\Known Faces\Steve Jobs.jpg")
steve_face_encodings = face_recognition.face_encodings(img_of_Steve)[0]

img_of_Obama = face_recognition.load_image_file(r"C:\Users\Lenovo\Desktop\New folder\python\face_rec\Known Faces\obama.jpg")
obama_face_encodings = face_recognition.face_encodings(img_of_Obama)[0]

known_face_encodings = [

ronaldo_face_encodings,
messi_face_encodings,
federer_face_encodings,
bill_face_encodings,
steve_face_encodings,
obama_face_encodings

]

known_face_names = [
"Cristiano Ronaldo",
"Roger Federer",
"Bill Gates",
"Steve Jobs",
"Barack Obama"
]

test_image = face_recognition.load_image_file(r"C:\Users\Lenovo\Desktop\New folder\python\face_rec\Unknown Faces\1.jpg")
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

pil_image = Image.fromarray(test_image)
draw = ImageDraw.Draw(pil_image)

for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown Person"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))

    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom-text_height-10), (right, bottom)), fill=(0, 0, 0), outline=(0, 0, 0))
    draw.text((left+6, bottom-text_height-5), name, fill=(255,255,255,255))

del draw

pil_image.show()

