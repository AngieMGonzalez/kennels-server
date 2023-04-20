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

## Classes
- https://www.youtube.com/watch?v=apACNr7DC_s 
- we only used function based components in React Next.js
- now, class based component
- OOP object oriented programming = deals w/ class components and constructors
- re-usable data frameworks 
- a function inside a class is an initializer method or `init method` (sometimes called constructors)
- access last string in array with `[-1]`
- classes group together data in `fields`
- and they group together related functions called `methods` 
- it's like a factory or blueprint for many objects are `instances` 
- Functions need to be invoked for the plan to run. Classes need to be instantiated to create an object from its design

## SQL
- Structured Query Language
- https://www.youtube.com/watch?v=27axs9dO7AE
- [creating tables](https://www.youtube.com/watch?v=SPPTQwx4FfE&t=300s)
- sql reserve words: `CREATE TABLE`
- [inserting data](https://www.youtube.com/watch?v=3Qq93zqO3GE)
- [constraints](https://www.youtube.com/watch?v=9WP35xwZ3tk)
- keybinding shortcut: Sqlite: Run Selected Query = Hold down the Command key and tap R twice
- `cmd+shift+p` Sqlite: Open Database
- [SELECT](https://www.youtube.com/watch?v=YufocuHbYZo)
- [SELECT cont](https://www.youtube.com/watch?v=PkJKzR_sClM)
- [UPDATE](https://www.youtube.com/watch?v=cd-hSl7_pGQ) `SET` `WHERE` `IN()`
- [UPDATE and DELETE FROM](https://www.youtube.com/watch?v=rT7BhXLfhds) `OR` `AND`
