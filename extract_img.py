from idlelib import __main__
import os
from PIL import Image
def crop_img(image_path , x_min , y_min , x_max ,y_max):
  '''
  This function takes an image path + x and y coordinates of two opposite corners of the rectangle
  and returns a cropped image
  '''
  x_shift=(x_max-x_min)*0.1
  y_shift=(y_max-y_min)*0.1

  img=Image.open(image_path)
  cropped=img.crop((x_min-x_shift , y_min-y_shift , x_max+x_shift, y_max+y_shift))
  return cropped

def extract_faces(image_name, image_info):
  '''
  Hàm này lấy tên hình ảnh + khung dữ liệu với thông tin về hình ảnh
  và chia hình ảnh thành tất cả các khuôn mặt khác nhau. tên hình ảnh có chứa
  tọa độ phía trên bên trái của mỗi khuôn mặt để chúng ta có thể phân biệt nó sau này
  '''
  faces=[]
  df_one_img=image_info[image_info["file_name"]==image_name[:-4]][["xmin","ymin","xmax","ymax" ,"label"]]
  # print(df_one_image)
  for row_num in range(len(df_one_img)):
    x_min, y_min , x_max ,y_max, label =df_one_img.iloc[row_num]
    image_path = os.path.join(input_data_path, image_name)
    faces.append((crop_img(image_path , x_min , y_min , x_max , y_max), label , f'{image_name[:-4]}_{(x_min,y_min)}'))
  return faces
# this function cut image

cropped_faces=[extract_faces(img , df) for img in images]

# sum of image
flat_cropped_faces=sum(cropped_faces , [])
flat_cropped_faces