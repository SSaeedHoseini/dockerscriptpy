import docker
import os
import shutil

import progress as output

client = docker.from_env()
client.images.prune()
total = len(client.images.list())
number = 0

output.printProgressBar(0, total, prefix = 'Main Progress:', suffix = 'Complete', autosize = True)

image_path = '{}/image/'.format(os.getcwd()).replace('\\','/')
if not os.path.exists(image_path):
        os.mkdir(image_path)

for image_tag in client.images.list():
        number = number+1

        file_path = '{}{}.tar'.format(image_path,str(image_tag.tags[0]).replace('/','-').replace(':','-'))
        
        if not os.path.isfile(file_path):
                img = client.images.get(str(image_tag.tags[0]))
                try:
                        res = img.save(chunk_size=None,named=True)
                        with open(file_path, 'w+b') as f:
                                try:
                                        for chunk in res:
                                                f.write(chunk)
                                except:
                                        os.remove(file_path)
                                        raise
                except:
                        raise
        output.printProgressBar(number, total, prefix = 'Main Progress:', suffix = 'Complete', autosize = True)
        
