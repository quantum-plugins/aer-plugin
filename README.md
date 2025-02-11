# AER Quantum Server Plugin

![build, test and publish](https://github.com/github/Dpbm/aer_plugin/workflows/build_test_publish.yml/badge.svg)

This is the AER plugin for quantum local server. With it, you can easily run your AER jobs in a local server outside your own computer.

## Functionalities

In this early stage, this plugin manages the following backends:

- AER (pure AER implementation)

and to them you can submit jobs to get: `counts`, `quasi distributions` and `expectation values`.

Even thought it's very limited for now, in future versions we aim to make more backends available.

## No Server

Although this is meant to be used inside a docker container as a plugin for quantum local server, you can run it locally without it.

To do that, simply install the dependencies:

```bash
pip install -r requirements
```


and then import the `aer_plugin` module inside your python script:

```python
#main.py

from aer_plugin import Plugin

p = Plugin()

# your qiskit code
# remember to export 
# your circuit to a 
# .qasm file
# ...

target_backend = "aer"
qasm_file_path = "<qasm_file_path>"
metadata = {"shots":1000}
result_type = "counts"

result = p.execute(
    target_backend, 
    qasm_file_path, 
    metadata, 
    result_type)

print(result) # e.g.: {'0':1000}

```


## Dev

For developers. There's some dependencies you need to have installed before adding any code. To ease this installation, you can use conda/mamba/conda-lock to load everything in the correct version.

```bash
# using conda/mamba/conda-lock
mamba env create -f environment.yml
conda env create -f environment.yml
conda-lock install -n aer-plugin conda-lock.yml

# then activate your environment
conda activate aer-plugin
mamba activate aer-plugin

# however, if you prefere, you can use pip as well
# make sure to use a virtual environment to avoid conflicts
pip install -r requirements.txt -r dev-requirements.txt

```

In this project are being used `3` check stages to ensure code quality, which are:

- linting/code style: using `pylint`/`black`
- types: using `mypy`
- tests: using `pytest`

To manage all this, we're using `tox`, for `3` python versions: `3.10`, `3.11` and `3.12`, expecting more versions in the future.

During development, ensure to run tox regularly to ensure that everything is behaving as expected. 

to learn more about tox check their [wiki here](https://tox.wiki/).


## Contributing

To start contributing for this project, make sure to:

- open an issue explaining what you have in mind
- follow the [dev section](#dev)
- add as many tests as you can on [./tests](./tests/)
- use a different branch for you modifications
- add comments explaining parts of your code that can be directly understand without deep investigation
- create readable code

Ensuring that, you're ready to open a pull request and be part of this community :)