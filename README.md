# Quantum Server Plugin

![build, test and publish](https://github.com/github/Dpbm/quantum-server-plugin-template/workflows/build_test_publish.yml/badge.svg)

To create a plugin for [local-quantum-server](https://github.com/Dpbm/local-quantum-server), `start by using this template` and then follow the steps below.

## Setup your plugin

1. Setup your `requirements.txt`

In your plugin, you'll probably need some external dependencies, like `qiskit`, `cirq`, `pennylane`, `numpy`, etc. List every required dependency inside the [requirements.txt file](./requirements.txt), line by line.

2. Create a virtual environment

To keep your work clean, make sure to use a virtual environment, this way your work won't get conflicted with pre-installed system dependencies.

Also, using environment managers allows you to easily change python versions. By default I'm using the `python 3.12.8`, however it maybe not the perfect match for your plugin. So remember to change it and explicit it on your project.

3. Add your code

After that, update the folder [example_plugin](./example_plugin/) to your plugin's name and start adding your code.

Inside [example_plugin](./example_plugin/) directory, you'll find some files:

- [interface.py](./example_plugin/interface.py): that's the file that creates the abstract class `Plugin`, which your project must use to ensure the correct usability. 
Don't change this file. Only `import` the `types`, `classes` and `functions` you need.
- [plugin.py](./example_plugin/plugin.py): that's the plugin starting point. In it, you may list the backends names your plugin can access. Also, you need to add some logic to handle the user input inside the `execute` method. By default, the class uses a decorator (`@check_backend`) to ensure that only defined backends can be accessed. However, you're free to implement your logic and do further checks.

Besides that, you're allowed to add new files and create your structure. But, keep in mind that, more complex projects may need additional configurations on either [setup.py](./setup.py) or [pyproject.toml](./pyproject.toml).

Also, you need to ensure the correct handling of the `result_types`, the possible inputs are: `'quasi_dist', 'counts', 'expval'` for now.

4. Add tests

Inside [tests directory](./tests/) add your tests using pytest. Although it's not mandatory, it's a nice practice to make your project easier to manipulate.

By default, `tox` is configured to run lint and type checks, as well as code tests. so remember to install the `dev-dependencies` and run tox:

```bash
pip install -r dev-requirements.txt
tox
```

5. Update the [setup.py](./setup.py)

With your code done, start adding your info to [setup.py](./setup.py). If you have a more complex structure, you may need to add more configurations to that, so remember to check the [setuptools guide](https://setuptools.pypa.io/en/latest/index.html).

6. Update the [LICENSE](./LICENSE)

The License for plugins is always `MIT`. So before proceeding, remember to update the [LICENSE file](./LICENSE) adding the year and your name.

6. Update the [README.md file](./README.md)

Doing that, delete everything in this very `README.md` file and describe your project.

7. Update GH Actions workflow

To be an accepted plugin, your must have your code on github. Due to that, it's possible to run some CI workflows to ensure you're code is correct and ready to be distributed.

So, to do that, go to [.github/workflows/build_test_publish.yml](./.github/workflows/build_test_publish.yml) and them ensure to update what's being required inside.

For plugins, every time it's pushed to the main branch, the code is built, tested and them published to PYPI automatically. To ensure that everything is going to go well, create and account at [pypi.org](https://pypi.org/) and setup a [Trusted publisher](https://docs.pypi.org/trusted-publishers/) mapping to your github workflow.

8. Request your plugin to be added to the list

After that, open an issue on [github.com/quantum-plugins/plugins-list](https://github.com/quantum-plugins/plugins-list) requesting your plugin to be added on the official plugins list. 

As soon as possible we'll see that and procede with the addition and your plugins will be called official 😊

## CONGRATS!!!

Now, you have a quantum plugin!!!!

Thank you so much for joining this amazing community🎉🎉🎉