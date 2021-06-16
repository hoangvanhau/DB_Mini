import os

# ./datasets/train/img/1.jpg	./datasets/train/gt/gt_1.txt
dataset_folder = 'datasets/'

test_folder = dataset_folder + 'test/'
train_folder = dataset_folder + 'train/'

test_file = dataset_folder + 'test.txt'
train_file = dataset_folder + 'train.txt'

test_img    = test_folder + 'img/'
test_gt     = test_folder + 'gt/'
train_img   = train_folder + 'img/'
train_gt    = train_folder + 'gt/'

def buildDatasetMap(image_folder=test_img, groundTruth_folder=test_gt, map_file = test_file):

    assert(os.path.isdir(image_folder))
    img_extensions = {'.jpg', '.bmp', '.png', '.jpeg', '.rgb', '.tif', '.tiff', '.gif', '.GIF'}
    
    dataset_dir = os.path.dirname(os.path.dirname(os.path.dirname(image_folder)))
    f_obj = open(map_file, 'w')
    for file in os.listdir(image_folder):
        file_path = os.path.join(image_folder, file)
        if os.path.isfile(file_path) and os.path.splitext(file)[1] in img_extensions:
            id, img_extensions = os.path.splitext(file)
            img = image_folder + id + img_extensions
            gt  = groundTruth_folder + 'gt_' + id + '.txt'
            f_obj.write(img + '\t' + gt + '\n')
    f_obj.close()


buildDatasetMap(image_folder=test_img, groundTruth_folder=test_gt, map_file=test_file)
buildDatasetMap(image_folder=train_img, groundTruth_folder=train_gt, map_file=train_file)
