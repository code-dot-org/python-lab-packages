# pythonlab-packages
This repository consists of packages for use in Python Lab. This can contain any library we want to expose to
students or any patches we want to apply to student code. Here are the current packages:

### pythonlab_setup
This package handles setup and teardown for Python Lab. For setup, it patches libraries for use in Python Lab.
The current patches are:
- We patch `matplotlib` in order to display graphs correctly. The patch updates the `show` method to send
  a base64 encoded string for display in Python Lab.
- We patch `requests` in order to route requests through code.org's request proxy. This protects students
  by only allowing requests to an allow-list of urls.

We run `setup_pythonlab()`, a method this package exposes, before each student run, which only applies
the matplotlib patch for now. We also run `teardown_pythonlab()` after each run, which flushes stdout and
changes directory to the home folder.

## unittest_runner
This tests adds some customization to the output of unit tests, and has a function to either run validation tests
(more customized) or student tests (less customized).

## Setup
- Install `pyenv`. 
    - See instructions [here](https://github.com/pyenv/pyenv?tab=readme-ov-file#getting-pyenv)
- Install python.
    ```
    pyenv install $(cat .python-version)
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
From the folder containing code and tests, run `pipenv run python -m unittest`. This will look for tests in all files that start with `test`.

# Lint your code
We use [ruff](https://docs.astral.sh/ruff/installation/) for linting. It is a dev dependency of all of our packages. You can install it on
your editor of choice for inline suggestions (for example, [VS Code](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)),
and run it on the command line via `ruff check`. It also runs as part of the PR check process.
