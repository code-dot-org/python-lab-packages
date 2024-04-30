# pythonlab-packages
Packages for use in Python Lab

## Setup
- Install `pyenv`. 
    - See instructions [here](https://github.com/pyenv/pyenv?tab=readme-ov-file#getting-pyenv)
- Install python.
    ```
    pyenv install 3.12.2
    ```
    After install, run `python --version`, which should output `3.12.2`.
- Install [pipenv](https://pipenv.pypa.io/en/latest/).
    ```
    pip install --user pipenv
    ```
- Install all required packages for the package you are working on. Navigate to the folder of the package (for example, `packages/pythonlab_setup`), and run:
    ```
    pipenv install
    ```

## Building a package
From the package folder containing `pyproject.toml`, run `python -m build`. The generated `.whl` file will be in the `dist` folder.

## Run tests
From the folder containing code and tests, run `python -m unittest`. This will look for tests in all files that start with `test`.