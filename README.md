# Albumy

*Capture and share every wonderful moment.*

> Example application for *[Python Web Development with Flask](https://helloflask.com/en/book/1)* (《[Flask Web 开发实战](https://helloflask.com/book/1)》).

Demo: http://albumy.helloflask.com

![Screenshot](https://helloflask.com/screenshots/albumy.png)

## Installation

clone:
```
$ git clone https://github.com/greyli/albumy.git
$ cd albumy
```
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```
or with Pipenv:
```
$ pipenv install --dev
$ pipenv shell
```
generate fake data then run:
```
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```
Test account:
* email: `admin@helloflask.com`
* password: `helloflask`

## Machine Learning Features  

This project has been extended to automatically generate **photo descriptions** and **tags** for uploaded images using **Hugging Face Transformers**.  

- **Automatic Alternative Text**:  
  When a user uploads a photo, the system generates an automatic description (alt text) if the user does not provide one. This improves accessibility and allows visually impaired users to understand the content of images.  

- **Automatic Tags for Image Search**:  
  The system identifies objects in images and generates tags automatically. These tags are stored in the database and used to enable **searching images by keywords**, improving discoverability.  

- **Enhanced Search**:  
  Users can now search for images by keywords that match **either the photo description or generated tags**, making it easier to find relevant images even if the user did not manually add tags.  

- **Implementation**:  
  - Transformers models used:
    - `Salesforce/blip-image-captioning-base` for captions/descriptions  
    - `google/vit-base-patch16-224` classifier for object tags  
  - The models run **locally**, no API keys or external services are required.  
  - Integration is done in `main.py` during photo upload:  
    - `generate_alt_text(path)` → sets `photo.description`  
    - `detect_objects(path)` → adds `photo.tags`  
  - Search feature updated in `main.py` to query **tags AND descriptions**.  


## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
