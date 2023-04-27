import os

# image paths
paths = ['./test/hotdog/', './test/notdog/',
         './train/hotdog/','./train/notdog/']

# rename test hotdog images
for path in paths:
    for i, filename in enumerate(os.listdir(path)):
        os.rename(path + filename, path + path.split('/')[1] + '_' + path.split('/')[2] + '_' + str(i)+'.jpg')