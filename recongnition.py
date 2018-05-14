#! python2
# coding=utf-8  
# 导入识别库
import face_recognition
# 加载已有的图片作为图像库
known_obama_image = face_recognition.load_image_file("obama.jpeg")
known_biden_image = face_recognition.load_image_file("trump.jpeg")
# 编码加载的图片
obama_face_encoding = face_recognition.face_encodings(known_obama_image)[0]
biden_face_encoding = face_recognition.face_encodings(known_biden_image)[0]
known_encodings = [
    obama_face_encoding,
    biden_face_encoding
]
# 加载要识别的图片并编码
image_to_test = face_recognition.load_image_file("oba.jpeg")
image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]
# 计算该图片与已有图片的差别值
face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)
# 自行设定同一张面孔的分界值，输出比对结果 
for i, face_distance in enumerate(face_distances):
    print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    print()