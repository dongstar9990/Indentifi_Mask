import glob

dataset =[parse_annotation(anno) for anno in glob.glob(annotations_path + '/*.xml')]
# dau ra cua parse la mot danh sach cua danh sach
# nen can lam phang mat cat
# chuyen cac danh sach thanh hinh anh
full_dataset=sum(dataset ,[])
# full_dataset
df=pd.DataFrame(full_dataset)
# hien thi kich thuoc du lieu
df.shape
