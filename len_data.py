from sklearn.model_selection import train_test_split
#get data

with_mask=[(img , image_name) for img , label , image_name in flat_cropped_faces if label=="with_mask"]
mask_weared_incorrect=[(img , image_name) for img, label , image_name in flat_cropped_faces if label=="mask_weared_incorrect"]
without_mask=[(img , image_name) for img, label , image_name in flat_cropped_faces if label =="without_mask"]


#plot data
print(f"số hình ảnh có khẩu trang : {len(with_mask)}")
print(f"số hình ảnh không có khẩu trang : {len(without_mask)}")
print(f"số hình ảnh đeo khẩu trang không hợp lệ: {len(mask_weared_incorrect)}")
print(f"số hình ảnh có khẩu trang : {len(with_mask) +  len(with_mask) + len(mask_weared_incorrect)}")




train_with_mask , test_with_mask=train_test_split(with_mask  , test_size=0.2 , random_state=42)
test_with_mask , val_with_mask=train_test_split(test_with_mask , test_size=0.6  ,random_state=43)

train_without_mask , test_without_mask= train_test_split(without_mask , test_size =.2 , random_state=40)
test_without_mask , val_without_mask= train_test_split(test_without_mask , test_size=.6 , random_state=40)

train_mask_weared_incorrect , test_mask_weared_incorrect = train_test_split(mask_weared_incorrect , test_size=.2 , random_state=40)
test_mask_weared_incorrect , val_mask_weared_incorrect = train_test_split(test_mask_weared_incorrect , test_size=.5 , random_state=40)
