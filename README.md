# RootMe API

[![Build Status](https://api.travis-ci.org/RemiGascou/rootmeapi.svg?branch=main)](https://api.travis-ci.org/RemiGascou/rootmeapi.svg?branch=main)
[![PyPi Version](https://d25lcipzij17d.cloudfront.net/badge.svg?id=py&type=6&v=1.1&x2=0)](https://pypi.org/project/rootmeapi/)

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
