# gitlabpy: gitlab api client for python:
  * [requests](http://docs.python-requests.org/en/latest/) for http verb methods
  * Useful return values

## Basic Usage:
```python
import gitlabpy

# create a gitlab session via login credentials:
sess = gitlabpy.Session.from_login(
    'https://git.mydomain.net',
    login='myusername',
    password='mysupersecretpassword')

# or alternately via token
token = gitlabpy.Token('EPZgnN5JK7C8FIG3C6xi')
host = 'https://git.mydomain.net'
sess = gitlabpy.Session(host, token)

# If you need to add a non-Trusted cert, you can pass a 'verify' keyword arg
sess = gitlabpy.Session(host, token, verify='/path/to/a/cert.crt')
```


## Conventions:
####Grok these conventions to develop an intuition for how gitlabpy maps to the Gitlab API
1. API calls are made from gitlabpy.Session objects by a Resource.Method pair
  ```python
  # pattern is "session.resource.method"
  sess.users.list
  sess.groups.members
  ```
  where 'resource' := [resource](https://github.com/gitlabhq/gitlabhq/tree/master/doc/api#resources)

2. API method parameters are passed via keyword arguments
  ```python
  # get a list of users
  response = sess.users.list(page=1, per_page=100)

  # get a list
  ```

3. The keyword arguments accepted by a API method are exactly the ones listed in its corresponding documentation.
  ```python
  # e.g. takes 'id' keyword arg, see: https://github.com/gitlabhq/gitlabhq/blob/master/doc/api/users.md#single-user
  sess.users.single
  ```
  Takes a single 'id' keyword argument, which matches what's described in the Parameters:' of its [documentation](https://github.com/gitlabhq/gitlabhq/blob/master/doc/api/users.md#single-user)

4. API method docstrings are the corresponding markdown header in the Gitlab API's README.md
  ```python
  # https://github.com/gitlabhq/gitlabhq/blob/master/doc/api/projects.md#list-owned-projects
  sess.groups.owned.__doc__ == 'List owned projects'
  ```

## TODO:
* OAuth support
* {Integration, Unit} Tests
* python3 support
