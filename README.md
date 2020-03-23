# Testing nose2.plugins.attrib PluginThis repository is a very simple "Hello, World" python project that has a test with the categories `normal` and `fun`.To run all tests:```$ nose2 -v -s src/tests/ ```This repository, however, is meant to show the utility of the `attrib` plugin available in `nose2`. This plugin can be triggered from the command line:```$ nose2 -v --plugin=nose2.plugins.attrib -s src/tests/ -A "attributes"```It is also configured to run automatically due to the `unittest.cfg` file inthe main directory. If this config file is present, the command becomes:```$ nose2 -v -s src/tests/ -A "attributes"```This repository also has a `utils.py` file in `src/tests/` that allows for test decorators:```@category('category1', 'category2')```