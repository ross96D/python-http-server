# Build a simple http server

## Setup

run the following commands

```shell
    # Creates a virtual enviroment. Usefull to set the dependencies of the project in isolation to the system dependencies
    python -m venv .venv

    # Activate the python of the virtual enviroment on your current command line.
    # If you are using powershell the script is Activate.ps1 instead
    .venv\Scripts\activate.bat

    # Install the required dependencies
    pip install -r requirements.txt
```

## Run the tests

```shell
    python -m pytest .
```
