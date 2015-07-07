# gitlabpy: gitlab api client
## Features:
  * [requests](http://docs.python-requests.org/en/latest/) for http IO
  * Useful return values (requests.Response instances)
  * 2.7 & 3.4 compatible

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
baseurl = 'https://git.mydomain.net'
sess = gitlabpy.Session(baseurl, token)

# If you need to add a non-Trusted cert, you can pass a 'verify' keyword arg
sess = gitlabpy.Session(baseurl, token, verify='/path/to/a/cert.crt')
```


## Conventions:
####Grok these conventions to understand how gitlabpy maps to the Gitlab API
1. API calls are made from gitlabpy.Session objects by a [resource](https://github.com/gitlabhq/gitlabhq/tree/master/doc/api#resources), method pair
  ```python
  # pattern is "session.resource.method"
  sess.users.list
  sess.groups.members
  ```

2. API method parameters are passed via keyword arguments
  ```python
  # get a list of users
  responses = sess.users.list()
  ```

3. The keyword arguments accepted by an API method are exactly the ones listed in its corresponding documentation.
  ```python
  # e.g. takes 'id' keyword arg
  sess.users.single(id=144)
  ```
  Compare to the corresponding [documentation](https://github.com/gitlabhq/gitlabhq/blob/master/doc/api/users.md#single-user)

4. API method docstrings are the corresponding markdown header in the Gitlab API's README.md
  ```python
  # https://github.com/gitlabhq/gitlabhq/blob/master/doc/api/projects.md#list-owned-projects
  sess.groups.owned.__doc__ == 'List owned projects'
  ```

## TODO:
* OAuth support
* {Integration, Unit} Tests
