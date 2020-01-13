import sys
import argparse
import os
import docker


import progress as output

client = docker.from_env()

parser = argparse.ArgumentParser()

parser.add_argument("--path", "-p", help="set path that contains image")
parser.add_argument("--image", "-i", help="image name that need to load")

args = parser.parse_args()

if not args.path:
    args.path = '{}/image/'.format(os.getcwd()).replace('\\','/')

if not args.image:
    image_list = [i for i in os.listdir(args.path) if i.endswith('.tar')]
else:
    if args.image.endswith('.tar'):
        image_list = [args.image,]

total = len(image_list)
number = 0

result= dict()

if total is not 0:
    output.printProgressBar(number, total, prefix = 'Progress:', suffix = 'Complete', autosize = True)

    for img_name in image_list:
        number = number + 1
        try:
            full_path = '{}{}'.format(args.path,img_name)
            
            if os.path.isfile(full_path):
                with open(full_path, 'rb') as f:
                    client.images.load(f)
                result[img_name] = 'Ok.'
                output.printProgressBar(number, total, prefix = 'Progress:', suffix = img_name, autosize = True)
        except:
            result[img_name] = 'Fail.'
            raise
    print('')
    for k , v in result.items():
        print(k+' => '+v)
else:
    print('tar file not found in directory {}'.format(args.path))