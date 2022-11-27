import os
import glob
import face_recognition
import time


start = time.time()
faces_folder_path = './orl_faces'
cnt = 0

for f in glob.glob(os.path.join(faces_folder_path, "*.jpg")):
    print("Processing file: {}".format(f))
    #загрузка фото
    img = face_recognition.load_image_file(f)
    #обнаружение лица на фотро
    face_locations = face_recognition.face_locations(img)
    #подсчет
    # face_locations - список элементов (лиц)
    # в списке столько элементов, сколько лиц на фото
    print("Number of myfaces detected: {}".format(len(face_locations)))
    if len(face_locations) != 0: 
        cnt += 1

print(f'total myfaces detected {cnt}')
print(f'total seconds spent {int(time.time() - start)}')