# SenseHat Sandbox

## Table of Contents

### Games

- Slug v1 - based on the tutorial `slug.py`

### Misc

- Clear LED display `clear.py`

## Installation

### Raspberry Pi

Just in case if it's not included

```shell
sudo apt-get install sense-hat
```

For real Hat:

```python
from sense_hat import SenseHat
```

For emulator:

```python
from sense_emu import SenseHat
```

### Emulator on macOS

Install required packages:

```shell
brew install pygobject3 gtk+3
```

Install emulator library

```shell
pip install sense-emu
```

### Dependencies

Install

```shell
pip install -r requirements.txt
```

Update

```shell
pip freeze > requirements.txt
```

### Virtual Environment

Setup

```shell
python3 -m venv --system-site-packages venv
```

Activate

```shell
source venv/bin/activate
```

Deactivate

```shell
deactivate
```
