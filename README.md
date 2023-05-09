# ScientificDev (YouTube channel)

**Author**: Artur Zacniewski  
**WWW #1**: [Official website](https://scientificdev.net/)    
**WWW #2**: [Website with resources](https://zacniewski.github.io/)  



---
## Table of contents

### Series #1 - [Images with Python](https://github.com/zacniewski/ScientificDevYouTube/tree/master/01-Images-with-Python/001-load-display-and-write-images)  
### Series #2 - coming soon ...

---
## How to run the code  
1. Clone the repo:  
    ```bash
    git clone git@github.com:zacniewski/ScientificDevYouTube.git
    ```

2. Create and activate the virtual environment:
    ```bash
    python3 -m venv my_env
    source my_env/bin/activate
    ```
    > Working with virtualenvs on different operating systems is described in [official documentation](https://docs.python.org/3/library/venv.html). 

3. Install required packages:
  - from `requirements` file with given versions:
    ```bash
    pip install -r reqiuirements.txt
    ```
  - the newest versions:  
    ```bash
    pip install opencv-python opencv-contrib-python
    ```
    
4. Run the program:
    ```bash
    python3 name_of_the_script.py
    ```

  - if program requires an image, it should be started as follows:  
    ```bash
    python3 name_of_the_script.py -i path_of_the_image
    ```