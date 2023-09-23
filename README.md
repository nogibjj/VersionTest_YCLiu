[![Python 3.9 Setup and Integration Test](https://github.com/nogibjj/VersionTest_YCLiu/actions/workflows/TestPython39.yml/badge.svg)](https://github.com/nogibjj/VersionTest_YCLiu/actions/workflows/TestPython39.yml)
[![Python 3.8 Setup and Integration Test](https://github.com/nogibjj/VersionTest_YCLiu/actions/workflows/TestPython38.yml/badge.svg)](https://github.com/nogibjj/VersionTest_YCLiu/actions/workflows/TestPython38.yml)

## Python Version Testing Using Github Actions

This repository demonstrates how to **leverage GitHub actions** to _**test**_ if the code is compatible with **different versions of python** setup.


Below is an overview of the project:

1. **Github Actions Setup to test different python versions**
  <br>a. _Makefile_: In the Makefile, actions were specified to **test** the scripts **with different versions of python**. The actions are triggered when pushed/ pulled to main branch. In addition to version testing, **installing packages**, **linting**, **testing**, **formatting** would be executed in order.

2. **Example of problematic scripts across different python versions**
   <br>b. _main.py_: main function of the **prblematic script**.
   <br>c. _test_main.py_: test functions for the main function.

3. **Other files for development environment settings**:
  <br>d. _.devcontainer_: contains devcontainer (used CodeSpace python default), setting up the environment for development.
  <br>e. _.gitignore_: specifies information to ignore (used GitHub default).
  <br>f. _requirements.txt_: lists required packages for the project.

4. **Description of the project**
   <br>g. _README.md_: THIS FILE, explaining the purpose of the directory.

This repository demonstrates how **python scripts can function properly** on **one version** but _**fail**_ to function with **another version**.
