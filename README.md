# Strip-The-Text - Frontend

---

## Setting up and Using the Project

Before you can run the project, some preparations need to be made first. These are described in the following.

### Cloning the Project

To open the project yourself in any IDE, the project must first be cloned. To do this, enter the following command in a
terminal:

```shell
git https://github.com/StripTheText/TextStrip-Frontend.git
```

### Setting Up the Project

After successfully cloning the project, a folder named **TextStrip - Frontend** should now be located in the current
terminal directory. The project is now located in this folder. The structure of the project is as follows:

```text
|- TextStrip-Frontend
|  |- functions
|  |  |- .gitkeep
|  |- models
|  |  |- whisper
|  |  |  |- .gitkeep
|  |- pages
|  |  |- .gitkeep
|  |  |- 2_Demo.py
|  |  |- 4_Handbook.py
|  |- .gitignore
|  |- Dockerfile
|  |- environment.yml
|  |- Introduction.py
|  |- LICENSE
|  |- README.md
|  |- requirements.txt
```

The **functions** folder contains all supporting functions that arise during the execution of the project. The **models** 
folder contains all trained models, which are needed on the different pages (**pages**). A detailed guide on how to
use it can be found on the Pages - Handbook page once the app is running.

### Installing the Project Dependencies

Before you can run the project, the project's dependencies must first be installed. There are the following options for
this: **[pip](https://pip.pypa.io/en/stable/)**, **[conda](https://docs.conda.io/en/latest/)** and **[venv](https://docs.python.org/3/library/venv.html)**. All three options are described below, but require an installed
version of Python (This project was developed with Python 3.11.*). If there is no suitable version of Python installed,
yet, it can be downloaded from the official **[Python website](https://www.python.org/downloads/)**.

**Note:** In addition to the project's dependencies, there are other dependencies defined by the operating system.
Please pay attention to the corresponding error messages.

#### Installation with pip

To install the dependencies with pip, the following command must be entered into a terminal:

```shell
pip install -r requirements.txt
```

**Note:** This method installs the packages globally. If this is not desired, one of the other methods should be used.

#### Installation with conda

Before you can install the individual dependencies, conda must first be installed and active. Please refer to the
official documentation of **[conda](https://docs.conda.io/en/latest/)**. After conda has been set up, it makes sense to
create a separate environment for this project, where only the required libraries are installed. To do this, follow
these steps:

```shell
conda create --name <Name of the Environment> python=3.11
```

After creating the environment, it must first be activated by the following step.

```shell
conda activate <Name of the Environment>
```

**Note:** If the environment is no longer needed, it can be deactivated again with the following command. It may also be
necessary to reactivate the environment at each new session.

```shell
conda deactivate
```

After the environment has been activated, the dependencies can now be installed. To do this, the following command must
be entered into a terminal (with activated environment):

```shell
conda install --file requirements.txt
```

#### Installation with venv

To install the dependencies with venv, a new environment must also be created by the following command in a terminal:

```shell
python -m venv <Name of the Environment>
```

After the environment has been created, it must first be activated by the following step.

```shell
<Name of the Environment>\Scripts\activate.bat
```

**Note:** If the environment is no longer needed, it can be deactivated again with the following command. It may also be
necessary to reactivate the environment at each new session.

```shell
deactivate
```

After the environment has been activated, the dependencies can now be installed. To do this, the following command must
be entered into a terminal (with activated environment):

```shell
pip install -r requirements.txt
```

With that, all dependencies are now installed and the project can be executed.

Natürlich, hier ist ein zusätzlicher Abschnitt, der beschreibt, wie man das Projekt über ein Docker-Image ausführt.

### Running the Project Using a Docker Image

If you want to run this project using a Docker container, you can do so using the provided Docker image. This can be
particularly useful as it abstracts away dependency management and provides a self-contained environment for running the
application.

First, you need to have Docker installed on your machine. If you don't, you can download it from the official Docker
website: **[Docker](https://www.docker.com/get-started)**.

Once Docker is installed and running, you can pull the Docker image for this project using the following command in your
terminal:

```shell
docker pull tkister/strip_the_text_frontend
```

After successfully pulling the image, you can run the container with the following command:

```shell
docker run -p 8501:8501 tkister/strip_the_text_frontend
```

The `-p` option maps port 8501 in the container to port 8501 on your local machine, which is the default port for
Streamlit applications.

Now, you should be able to access the Streamlit application in your web browser at `http://localhost:8501`.

Remember, any changes made inside the container will not be persistent. If you want to modify the application code or
add your own files, consider building your own Docker image or directly running the application on your local machine.

### Running the Project

To run the project, the environment in which the dependencies have been installed must first be activated. The project
can then be run with the following command:

```shell
streamlit run Introduction.py
```

---

### How to Use the Frontend
# [Navigating and Using Text Classification and Summarization Features in the Demo](https://app.tango.us/app/workflow/107e9d05-7a02-4166-ab9a-a5ebc8b83733?utm_source=markdown&utm_medium=markdown&utm_campaign=workflow%20export%20links)

__Creation Date:__ July 24, 2023  
__Created By:__ Tobias Kister  
[View most recent version on Tango.us](https://app.tango.us/app/workflow/107e9d05-7a02-4166-ab9a-a5ebc8b83733?utm_source=markdown&utm_medium=markdown&utm_campaign=workflow%20export%20links)



***




## # [Open the Strip-The-Text Frontend App](http://localhost/)


### 1. Navigate to the Demo - Page
![Step 1 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/da2763d9-e502-4224-bf2e-038e17a3d9d4/a7114b30-5b6c-4fdd-929a-1a1aa9077953.png?crop=focalpoint&fit=crop&fp-x=0.1513&fp-y=0.2039&fp-z=1.7212&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=22&mark-y=246&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz01ODAmaD03NCZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


## # Custom User-Input


### 2. Enter your custom Text
![Step 2 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/6f4ea164-c9f7-4ab5-89f3-a14d1c13fde9/fd159d6b-4bf5-4a08-b22d-1cf97c68ddac.png?crop=focalpoint&fit=crop&fp-x=0.2813&fp-y=0.5263&fp-z=1.2279&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=102&mark-y=66&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz02MjUmaD02NzQmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


## # Microphone


### 3. Umschalten auf Microphone
![Step 3 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/a4995d11-90b5-4c89-993b-abaf8221c731/5a79e2b9-ddeb-4651-8e01-facea009f8c6.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n)


### 4. Record your Text
![Step 4 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/c223e343-861e-40ed-bcdf-29c216f8ec05/01d80436-5d69-44b7-90c4-933361826ac3.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n)


## # File Upload


### 5. Select File Upload Option
![Step 5 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/d2f90688-1a83-43cb-b6da-3c94b44f29f3/0d006660-ede0-4e30-9fa7-f5c5839bc6d7.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n)


### 6. Select File to Upload
![Step 6 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/3414d93e-0d88-4cf8-8a9f-507cebc920ce/7b0fa720-b71f-49c3-896e-7082c4f87f2a.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n)


## # Weiterverarbeitung


### 7. Adjust the Compression Rate
![Step 7 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/d7b4b936-d6d3-44a7-b22c-16a0614ea124/8a69db32-23c2-429d-8190-d4412fc490a6.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n)


### 8. Select your desired Activity
![Step 8 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/f0faf03b-6dd9-44c8-b2ff-71d20e9cb737/f75a9453-0f88-4605-a0fe-84f73fe8ce09.png?crop=focalpoint&fit=crop&fp-x=0.1866&fp-y=0.9099&fp-z=2.9760&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=536&mark-y=515&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMjkmaD0xNDkmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 9. Click on Go!
![Step 9 screenshot](https://images.tango.us/workflows/107e9d05-7a02-4166-ab9a-a5ebc8b83733/steps/1f5e058d-084c-4f4c-b3fa-6508603c5aa6/ac2201e6-4e51-4a54-9e45-e6fe0f14346f.png?crop=focalpoint&fit=crop&fp-x=0.2810&fp-y=0.9099&fp-z=2.2889&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=412&mark-y=582&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0zNzYmaD0xMTUmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 10. View your Results

<br/>

***
Created with [Tango.us](https://tango.us?utm_source=markdown&utm_medium=markdown&utm_campaign=workflow%20export%20links)
