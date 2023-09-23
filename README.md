## Python Version Testing Using Github Actions

This repository demonstrates how to **leverage GitHub actions** to **_test_** if the code is compatible with **different versions of python** setup.

Below is an overview of the project:

1. **Github Actions Setup to test different python versions**
  <br>a. **Makefile**: In the Makefile, actions were specified to **test** the scripts **with different versions of python**. The actions are triggered when pushed/ pulled to main branch. In addition to version testing, **installing packages**, **linting**, **testing**, **formatting** would be executed in order.

2. **Example of problematic scripts across different python versions**
   <br>b. **main**.py: main function of the **prblematic script**.
   <br>c. **test_main**.py: test functions for the main function.

3. **Other files for development environment settings**:
  <br>d. **.devcontainer**: contains devcontainer (used CodeSpace python default), setting up the environment for development.
  <br>e. **.gitignore**: specifies information to ignore (used GitHub default).
  <br>f. **requirements**.txt: lists required packages for the project.

4. **Description of the project**
   <br>g. **README**.md: THIS FILE, explaining the purpose of the directory.

This repository demonstrates how **python scripts can function properly** on **one version** but **_fail_** to function with **another version**.
