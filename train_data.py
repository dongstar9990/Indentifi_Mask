#  train set
for image, image_name in train_with_mask:
    save_image(image, image_name, output_data_path, "train", "with_mask")

for image, image_name in train_mask_weared_incorrect:
    save_image(image, image_name, output_data_path, "train", "mask_weared_incorrect")

for image, image_name in train_without_mask:
    save_image(image, image_name, output_data_path, "train", "without_mask")

# Test set

for image, image_name in test_with_mask:
    save_image(image, image_name, output_data_path, 'test', 'with_mask')

for image, image_name in test_mask_weared_incorrect:
    save_image(image, image_name, output_data_path, 'test', 'mask_weared_incorrect')

for image, image_name in test_without_mask:
    save_image(image, image_name, output_data_path, 'test', 'without_mask')

# Val set

for image, image_name in val_with_mask:
    save_image(image, image_name, output_data_path, 'val', 'with_mask')

for image, image_name in val_without_mask:
    save_image(image, image_name, output_data_path, 'val', 'without_mask')

for image, image_name in val_mask_weared_incorrect:
    save_image(image, image_name, output_data_path, 'val', 'mask_weared_incorrect')