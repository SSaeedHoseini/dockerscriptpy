import docker
import os
import shutil


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', autosize = False):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        autosize    - Optional  : automatically resize the length of the progress bar to the terminal window (Bool)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    styling = '%s |%s| %s%% %s' % (prefix, fill, percent, suffix)
    if autosize:
        cols, _ = shutil.get_terminal_size(fallback = (length, 1))
        length = cols - len(styling)
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s' % styling.replace(fill, bar), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

client = docker.from_env()
client.images.prune()
total = len(client.images.list())
number = 0

printProgressBar(0, total, prefix = 'Main Progress:', suffix = 'Complete', autosize = True)

image_path = '/home/{}/image'.format(os.environ.get('USER'))
if not os.path.exists(image_path):
        os.mkdir(image_path)

for image_tag in client.images.list():
        number = number+1

        file_path = '/home/{}/image/{}.tar'.format(os.environ.get('USER'),str(image_tag.tags[0]).replace('/','-'))
        
        if not os.path.isfile(file_path):

                img = client.images.get(str(image_tag.tags[0]))
                url = client.api._url('/images/{0}/get', img.id)
                res = client.api._get(url, stream=True ,timeout=1000)

                with open(file_path, 'w+b') as f:
                        try:
                         for chunk in res.iter_content(chunk_size=None):
                                f.write(chunk)
                        except:
                                os.remove(file_path)
                                raise
        
        printProgressBar(number, total, prefix = 'Main Progress:', suffix = 'Complete', autosize = True)
        
