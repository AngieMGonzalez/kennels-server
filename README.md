# kennels-server

## Get Started
- run `python3 --version` if you do not get a number that starts with at least 3.9, you need to upgrade

## Debugging
- https://www.youtube.com/watch?v=scAOUwa9XvM&feature=youtu.be 

## Directory and code setup
```
mkdir -p ~/workspace/kennels-server
cd ~/workspace/kennels-server
touch request_handler.py
curl -L -s 'https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore' > .gitignore
```

## ENV and then Debugger
- first make sure you are in the right project within workspace
- start env with the shell for libraries + packages with `pipenv shell`
- end env with `pipenv --rm`
- in VSCode run the debugger
- Debugger also starts the server
- [Debug reference for VSCode](https://www.youtube.com/watch?v=scAOUwa9XvM)

- `option + shift + f` auto formats to PEP 8
- [f strings vid](https://www.youtube.com/watch?v=o0mvgsPQ8Jg) also see hello world

## Magic import
- A package in Python is just a directory with a certain file in it.
- That directory needs to have a file called `__init__.py` in it.
- It's that file, with its weird name, that magically makes a directory into a package.

## Tuples 
- https://www.youtube.com/watch?v=NI26dqhs2Rk

##JSON in Python
- https://www.youtube.com/watch?v=pTT7HMqDnJw 

# Don't forget to refresh the Debugger
