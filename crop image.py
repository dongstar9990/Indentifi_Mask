from PIL import Image
import os
import pandas
# this function helps programer cut image
def crop_img(image_path , x_min , y_min , x_max , y_max):
  """
  this function takes an image path
  """

  x_shift=(x_max-x_min)*0.1
  y_shift=(y_max-y_min)*0.1
  img=Image.open(image_path)
  cropped=img.crop((x_min-x_shift , y_min -y_shift , x_max+x_shift , y_max+y_shift))
  return cropped

def extract_faces(image_name, image_info):
  faces=[]
  df_one_img = image_info[image_info['file_name'] == image_name[:-4]][['xmin', 'ymin', 'xmax', 'ymax', 'label']]
    #print(df_one_img)
  for row_rum in range(len(df_one_img)):
    x_min , y_min , x_max , y_max ,label=df_one_img.iloc[row_rum]
    image_path=os.path.join(input_data_path , image_name)
    faces.append((crop_img(image_path , x_min , y_min ,x_max , y_max), label , f'{image_name[:-4]}_{(x_min , y_min)}'))
    return faces

#
cropped_faces=[extract_faces(img, df) for img in images]

flat_cropped_faces=sum(cropped_faces , [])