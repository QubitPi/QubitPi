Fork Sync
=========

![Python Version Badge]
[![Apache License Badge]][Apache License, Version 2.0]

### Creating an Isolated Environment

It is strongly recommended to work in an isolated environment. Install virtualenv and create an isolated Python
environment by

```console
python3 -m pip install --user -U virtualenv
python3 -m virtualenv .venv
```

To activate this environment:

```console
source .venv/bin/activate
```

or, on Windows

```console
./venv\Scripts\activate
```

> [!TIP]
> 
> To deactivate this environment, use
> 
> ```console
> deactivate
> ```

### Installing Dependencies

```console
pip3 install -r requirements.txt
```

```console
python3 sync.py
```

License
-------

The use and distribution terms for [fork-sync]() are covered by the [Apache License, Version 2.0].

[Apache License Badge]: https://img.shields.io/badge/Apache%202.0-F25910.svg?style=for-the-badge&logo=Apache&logoColor=white
[Apache License, Version 2.0]: https://www.apache.org/licenses/LICENSE-2.0

[Python Version Badge]: https://img.shields.io/badge/Python-3.10-FFD845?labelColor=498ABC&style=for-the-badge&logo=python&logoColor=white
