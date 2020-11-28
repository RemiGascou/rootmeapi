# RootMe API

[![Build Status](https://travis-ci.org/RemiGascou/rootmeapi.svg?branch=master)](https://travis-ci.org/RemiGascou/rootmeapi)
[![PyPi Version](https://badge.fury.io/py/rootmeapi.svg)](https://badge.fury.io/py/rootmeapi.svg)

## Installation

```python
python3 -m pip install rootmeapi
```

## Requirements

You need to have a valid account on https://www.root-me.org

## Quick examples

If you want to be able to connect to CTF-ATD rooms from a VPS, you need to be connected so your IP is whitelisted. To do this, you can use this oneliner :

```
python3 -c "__import__('rootmeapi').RootMeAPI().login('YourUsername')"
```

It will prompt you for you password.
