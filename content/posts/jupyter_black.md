+++
title = 'Automatically clean up your Jupyter Notebooks with Jupyter Black'
date = 2024-06-07T13:22:00+08:00
draft = false
+++

One of my biggest gripes about Jupyter Notebooks is that it's so EASY to write dirty and messy code. 

Every other IDE has some kind of autoformatter to speed up cleaning your code like in Pycharm and VS Code but Jupyter? No. At least by default No.

Thankfully there's this extension called Jupyter black -- basically when you have it set up it automatically formats a code cell as soon as you run it just like that

Setting it up is really easy just run:
```shell
pip install jupyter underscore black
```

and then somewhere in the notebook you add 

```python
%load_ext jupyter_black
```

and then you're done! That's it. 

If you don't like the default settings it's also easily configurable -- just check out the [docs](https://pypi.org/project/jupyter-black/); 