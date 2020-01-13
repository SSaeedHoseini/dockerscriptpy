# dockerscriptpy
dockerscriptpy is a project that  use docker-py to deal with docker-engine to save/load image automatically and use offline.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and useing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

First create ٰvirtualenv with Python 3
```
virtualenv -p python3 env
```

Then enable env and install the requirements
```
pip install -r requirements.txt
```

## Use

how to use?

### Save image

To save images in local storage

```
$ python save_image.py path_to_save_images
```
If you do not enter a path_to_save_images, the images are stored in current directory in image folder 

### Load image

To load images from local storage

```
python load_image.py -p path_to_load_images
```
or, to load one image use
```
python load_image.py -i image_path
```
If you do not enter a path_to_load_images, the script search in current directory in image folder 
## Authors

* **SSaeedHoseini** - *Initial work* - [SSaeedHoseini](https://github.com/SSaeedHoseini)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
