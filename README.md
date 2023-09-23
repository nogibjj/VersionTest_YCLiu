[![Python 3.9 Setup and Integration Test](https://github.com/nogibjj/VersionTest_YCLiu/actions/workflows/TestPython39.yml/badge.svg)](https://github.com/nogibjj/VersionTest_YCLiu/actions/workflows/TestPython39.yml)
[![Python 3.8 Setup and Integration Test](https://github.com/nogibjj/VersionTest_YCLiu/actions/workflows/TestPython38.yml/badge.svg)](https://github.com/nogibjj/VersionTest_YCLiu/actions/workflows/TestPython38.yml)

## Python Version Testing Using Github Actions

This repository demonstrates how to **leverage GitHub actions** to _**test**_ compatibility of scrpits with **different versions of python**.

Below is an overview of the project:

1. **Github Actions Setup to test different python versions**
  <br>a. _.github/workflows/.ymlFiles_ : In the YAML(.yml) files, I setup enviroment using **different versions of python** for later actions. The actions are triggered when pushed/ pulled to main branch. After setting up the enviroment, actions of **installing packages**, **linting**, **testing**, **formatting** would be executed in order (specified in Makefile). Below is an example code block for setting up python versions in a YAML file.

```
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.8"]
    steps:
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with: python-version: ${{ matrix.python-version }}
```
2. **Example of problematic scripts across different python versions**
   <br>b. _main.py_: main function of the **prblematic script**.
   <br>c. _test_main.py_: test functions for the main function.

3. **Other files for development environment settings**:
  <br>d. _.devcontainer_: contains devcontainer (used CodeSpace python default), setting up the environment for development.
  <br>e. _.gitignore_: specifies information to ignore (used GitHub default).
  <br>f. _requirements.txt_: lists required packages for the project.

4. **Description of the project**
   <br>g. _README.md_: THIS FILE, explaining the purpose of the directory.

From the status badges shown above, we can see that the **python scripts can function properly** on **python 3.9** but _**fail**_ to function with **pythonn 3.8**.

