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

The **functions** folder contains all supporting functions that arise during the execution of the project. The **models
** folder contains all trained models, which are needed on the different pages (**pages**). A detailed guide on how to
use it can be found on the Pages - Handbook page once the app is running.

### Installing the Project Dependencies

Before you can run the project, the project's dependencies must first be installed. There are the following options for
this: **[pip](https://pip.pypa.io/en/stable/)**, **[conda](https://docs.conda.io/en/latest/)** and *
*[venv](https://docs.python.org/3/library/venv.html)**. All three options are described below, but require an installed
version of Python (This project was developed with Python 3.11.*). If there is no suitable version of Python installed
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

The `-p` option maps the port 8501 in the container to port 8501 on your local machine, which is the default port for
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
