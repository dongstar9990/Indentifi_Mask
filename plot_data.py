#remove image
final_test_image='maksssksksss2' # chon hinh anh
# tao mot khung du lieu rieng chi chua nhung nguoi cu the nay
df_final_test=df.loc[df["file"]==final_test_image]
# xoa hinh anh khoi bo du lieu day du
images.remove(f'{final_test_image}.png')
# xoa thong tin cua hinh anh khoi bo du lieu day du
df= df.loc[df["file"]!= final_test_image]


df.rename(columns ={'file':'file_name','name':'label'} , inplace=True)
df_final_test.rename(columns={'file':'file_name' , 'name':'label'} , inplace=True)

df["label"].value_counts()
df["label"].value_counts().plot(kind="barh")
plt.xlabel("Count " , fontsize=20  , fontweight="bold")
plt.ylabel("Label " , fontsize=20  , fontweight="bold")

labels=df["label"].unique()
directory=["train","test","val"]

output_data_path="."
# path to src image

import os
for label in labels:
  for d in directory:
    path=os.path.join(output_data_path , d, label)
    # print(path)
    if not os.path.exists(path):
      os.makedirs(path)

# print(os.makedirs(path))