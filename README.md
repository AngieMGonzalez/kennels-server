# kennels-server

## Get Started
- run `python3 --version` if you do not get a number that starts with at least 3.9, you need to upgrade
- install pylint?

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
- check your virtualenvs if theyre active `pipenv --venv`
- start env with the shell for libraries + packages with `pipenv shell`
- end env with `pipenv --rm`
- in VSCode run the debugger
- Debugger also starts the server
- [Debug reference for VSCode](https://www.youtube.com/watch?v=scAOUwa9XvM)

- `option + shift + f` auto formats to PEP 8 standards
- [f strings vid](https://www.youtube.com/watch?v=o0mvgsPQ8Jg) also see hello world

## Magic import
- A package in Python is just a directory with a certain file in it.
- That directory needs to have a file called `__init__.py` in it.
- It's that file, with its weird name, that magically makes a directory into a package.

## Tuples 
- https://www.youtube.com/watch?v=NI26dqhs2Rk

## JSON in Python
- https://www.youtube.com/watch?v=pTT7HMqDnJw 

# Don't forget to refresh the Debugger

## Register for customer 
- [kennel-client](https://github.com/AngieMGonzalez/kennel-client/blob/main/src/components/auth/Register.js)

## Enumerate
- https://www.youtube.com/watch?v=-MZiQaNI0QA

## Pop List
- [python 3.7](https://www.youtube.com/watch?v=SUOX1-gMWPw)
- removes obj from a list and returns that single obj to us + changes list to not have that element we "popped" out
- auto pops last item in list or you can provide index argument

## 204 No Content HTTP Response Status Code
- the server has fulfilled the request but does not need to return an entity-body, and might want to return updated meta-information
- the 204 response MUST NOT include a message-body, and thus is always terminated by the first empty line after the header fields

## UPDATE: PUT vs PATCH HTTP methods used to updated a resource on a server
- PUT REPLACES the ENTIRE resource with the new data provided in the request body
- PATCH is used to UPDATE a part of a resource. AKA you only need to provide the changes you want to make, and the server will apply those changes to the existing resource. In Postman, you can use the PATCH method to update a resource by sending a request with only the changed properties in the request body. 
