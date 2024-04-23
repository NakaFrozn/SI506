# SI 506 SWAPI Caching

## Topics

1. Data caching
2. `five_oh_six` cache
3. Deep copies of mutable objects

## 1.0 Data caching

Data caching is an optimization strategy designed to reduce duplicate data requests by storing
the data retrieved locally. If the data is again required it can be fetched from the local cache,
which typically results in a performance boost.

:bulb: Web browsers cache text, images, CSS styles, scripts, and media files in order to reduce
load times whenever you revist a page.

A cache is usually designed to hold data temporarily; cached data is allowed to "expire" after a
given interval and is either refreshed or removed from storage. Cache controls and expiration
policies help to reduce the chance that data held in the cache no longer matches the origin data.

Python provides a number of built-in caching options including a "Least Recently Used" (LRU)
memoization strategy implemented by the
[`functools.lru_cache`](https://docs.python.org/3/library/functools.html) or the third-party
[`cachetools`](https://cachetools.readthedocs.io/en/latest/) package. However, the "five_oh_six"
caching infrastructure will employ a Python dictionary.

## 2.0. The `five_oh_six` cache

The SWAPI caching implementation involves the following objects:

| Object | Module | Type | Description |
| :----- | :----- | :--- | :---------- |
| `cache` | `si506_week_14.py` | `dict` | Serves as a temporary in-memory cache. |
| `create_cache` | `five_oh_six.py` | `function` | Attempts to retrieve cache contents written to the file system. If successful the cache contents from the previous script run are returned to the caller as the new cache. If unsuccessful an empty cache is returned to the caller. |
| `create_cache_key` | `five_oh_six.py` | `function` | Formats a URL encoded string comprising the base URL, resource path, and querystring (if provided) that serves as a key to which the corresponding SWAPI resource is mapped. |
| `get_resource` | `five_oh_six.py` | `function` | Returns a dictionary representation of a JSON document retrieved from the web. |
| `get_swapi_resource` | `si506_week_14.py` | `function` | Retrieves a dictionary representation of one or more SWAPI entities stored either remotely or locally in the `cache`. Resources retrieved via HTTP GET requests are stored in the local `cache`. The function delegates to `create_cache_key` the task of manufacturing keys to be used in the cache and to `get_resource` the task of retrieving remote resources. |

The following example illustrates the caching workflow. When retrieving a SWAPI representation of a
person, the opportunity exists to retrieve additional relevant information since certain values
stored in the JSON document are in the form of URLs that can be used to retrieve representations of
SWAPI planets, species, starships, vehicles, and films. Each URL is an identifier that represents an
object that can be retrieved from a particular location (e.g.,`https://swapi.py4e.com`).

SWAPI data structures like that of the Corellian smuggler
[Han Solo](https://en.wikipedia.org/wiki/Han_Solo) and his partner the Wookiee
[Chewbacca](https://en.wikipedia.org/wiki/Chewbacca) are inspired by
[linked data](https://www.w3.org/standards/semanticweb/data) design principles that undergird the
[semantic web](https://www.w3.org/standards/semanticweb/).

Han Solo's and Chewbacca's SWAPI JSON documents contains a number of links that associate the
smugglers with other Star Wars entities:

```json
[
   {
    "name": "Han Solo",
    ...
    "homeworld": "https://swapi.py4e.com/api/planets/22/",
    "films": [
        "https://swapi.py4e.com/api/films/1/",
        "https://swapi.py4e.com/api/films/2/",
        "https://swapi.py4e.com/api/films/3/",
        "https://swapi.py4e.com/api/films/7/"
    ],
    "species": [
        "https://swapi.py4e.com/api/species/1/"
    ],
    ...
    "starships": [
        "https://swapi.py4e.com/api/starships/10/",
        "https://swapi.py4e.com/api/starships/22/"
    ],
    ...
    "url": "https://swapi.py4e.com/api/people/14/"
  },
  {
    "name": "Chewbacca",
    ...
    "homeworld": "https://swapi.py4e.com/api/planets/14/",
    "films": [
      "https://swapi.py4e.com/api/films/1/",
      "https://swapi.py4e.com/api/films/2/",
      "https://swapi.py4e.com/api/films/3/",
      "https://swapi.py4e.com/api/films/6/",
      "https://swapi.py4e.com/api/films/7/"
    ],
    "species": [
          "https://swapi.py4e.com/api/species/3/"
      ],
    ...
    "starships": [
      "https://swapi.py4e.com/api/starships/10/",
      "https://swapi.py4e.com/api/starships/22/"
    ],
    ...
    "url": "https://swapi.py4e.com/api/people/13/"
  }
]
```

Both data structures share links to three films and two starships. If you were to retrieve Han's and
Chewie's linked data from SWAPI, five of the HTTP GET requests would duplicate previous calls.
Five unnecessary API requests is something to avoid. Luckily, we can implement a simple cache in
order to optimize our interactions with SWAPI.

The `five_oh_six` cache stores data in a dictionary named `cache`. Below is the caching workflow:

1. Check if `cache` contents have been saved to the file system; if true seed the in-memory
   cache with content stored previously; otherwise return an empty `cache` to the caller.

2. Before every HTTP GET request, check `cache` for the desired resource. This step requires
   generating a key based on the URL and any querystring parameters before checking whether or not
   the key is found in the `cache` dictionary's current set of keys.

3. If the desired resource is mapped to a key stored in the `cache`, retrieve it from the `cache`
   (do not issue the HTTP GET request).

4. If the resource is _not_ stored in the `cache`, issue the HTTP GET request and retrieve the
   resource from the remote service.

5. Generate a key for the resource and update the `cache` with a deep copy of the resource retrieved
   from the remote service.

6. Persist the mutated `cache` by writing the cache dictionary to a JSON file.

Vital to this caching strategy is the generation of purpose-built "cache" keys that
facilitate discovery and retrieval of cached content. The HTTP GET request URL and parameters
(if any) can be used to construct a unique key to which the associated SWAPI resource can be mapped.

Creating such keys can be done using the Python standard Library's
[`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse) module
and two of its functions: `urlencode` and `urljoin`. You can call the `urlencode` function to
convert the `params` dictionary passed to the function `get_swapi_resource` into a
[URL encoding](https://en.wikipedia.org/wiki/Percent-encoding)
[querystring](https://en.wikipedia.org/wiki/Query_string).

URL encoding involves "encoding" or replacing certain characters such as a space with a special
character sequence such as '%20' or '+'. After encoding the querystring, the `urljoin` function is
called to combine the SWAPI base URL (consisting of a scheme, host, and path) and the querystring
(preceded by the `?` separator) for use as a key.

:bulb: The cache key is itself a valid URL.

```python
def create_cache_key(url, params=None):
    """..."""

    if params:
        return urljoin(url, f"?{urlencode(params, quote_via=quote)}").lower()
    else:
        return url.lower()
```

If you need to retrieve the SWAPI representation of Anakin Skywalker and store the response in the
cache, passing `'https://swapi.py4e.com/api/people/'` and `{'search': 'Anakin Skywalker'}` to
`create_cache_key` will return the "key"
`'https://swapi.py4e.com/api/people/?search=anakin%20skywalker'`.

The remaining steps can be implemented in a few lines of code. The function `get_swapi_resource`
is refactored to permit the necessary change in workflow required by the addition of an in-memory
cache. Its new task is to check the cache for the desired resource and, if located, a "deep"
copy of the resource will be returned to the caller. If the resource is not stored in the cache,
the function will delegate to the utility function `get_resource` the task of issuing an HTTP GET
request to retrieve the resource from SWAPI. Once the resource is retrieved a deep copy of the
resource is mapped to the `key` and deposited in the cache before being returned to the caller.

### Program/script

```python
def get_swapi_resource(url, params=None, timeout=10):
    """..."""

    key = utl.create_cache_key(url, params)
    if key in cache.keys():
        return copy.deepcopy(cache[key]) # recursive copy of objects
    else:
        resource = utl.get_resource(url, params, timeout)
        cache[key] = copy.deepcopy(resource) # recursive copy of objects
        utl.write_json('./stu-cache.json', cache) # persist mutated cache

        return resource
```

### five-oh-six module

```python
def get_resource(url, params=None, timeout=10):
    """..."""

    if params:
        return requests.get(url, params, timeout=timeout).json()
    else:
        return requests.get(url, timeout=timeout).json()
```

Data stored in the cache dictionary replicates the decoded JSON documents returned by SWAPI. Recall
that SWAPI "searches" return a JSON document comprising four key-value pairs. The decoded
document&mdash;a dictionary comprising four key-value pairs&mdash; is stored in the cache:

```python
{
      'https://swapi.py4e.com/api/people/?search=anakin%20skywalker': {
          'count': 1,
          'next': None,
          'previous': None,
          'results': [
              {
                  'name': 'Anakin Skywalker',
                  ...
              }
          ]
      }
}
```

If a SWAPI representation of Anakin was retrieved employing `https://swapi.py4e.com/api/people/11/`
the decoded document would be stored in the cache as follows:

```python
{
    'https://swapi.py4e.com/api/people/11/': {
        'name': 'Anakin Skywalker',
         ...
    }
}
```

From the caller's perspective interacting with the function `get_swapi_resource` remains unchanged.
The function's "signature", the mix of required and optional parameters defined for it, has not
changed. Implementing the new workflow involves code changes that are all "under the hood."

## 3.0 Deep copies of mutable objects

When working with mutable objects such as lists one must approach copy operations carefully,
especially when working with nested lists. Recall that variables are nothing more than pointers to
objects. Objects can hold references to other objects and if the various object types are _mutable_
working with (faux) object "copies" can result in unintended mutations of the original object.

You may have noticed when reviewing the refactored function `get_swapi_resource` that a resource
_assigned to_ the cache or _returned from_ the cache are "deep" copies of the resource created using
the standard library's `copy` module. The module provides a `copy.deepcopy()` function that returns
a new compound object that contains copies of (rather than references to) objects contained in the
original.

Python permits both "shallow" and "deep" copying. The
[official documentation](https://docs.python.org/3/library/copy.html) distinguishes between the two
operations as follows:

> A shallow copy constructs a new compound object and then (to the extent possible) inserts
> references into it to the objects found in the original.
>
> A deep copy constructs a new compound object and then, recursively, inserts copies into it of the
> objects found in the original.

The following example using the Python shell illustrates the concern and remedy nicely.

```commandline
>>> import copy

>>> nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> nums
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

>>> nums2 = nums # not a copy

>>> nums2.append([10, 11, 12])
>>> nums2
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

>>> nums
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

>>> nums3 = nums.copy() # shallow copy

>>> nums3.append([13, 14, 15])
>>> nums3
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

>>> nums
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

>>> nums3[0][0] = 1000
>>> nums3
[[1000, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

>>> nums
[[1000, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

>>> nums4 = copy.deepcopy(nums)
>>> nums4
[[1000, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

>>> nums4[0][1] = 2000
>>> nums4
[[1000, 2000, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

>>> nums
[[1000, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
```

### Observations

1. `nums2` is _not_ a copy of `nums`. `nums2` is nothing more than a second pointer/label/name to
   the `list` (also) known as `nums`.

2. Mutating `nums2` mutates the `list` named `nums`.

3. `nums3` is a _shallow copy_ of `nums`. This means that while you can add _new_ elements to
   `nums3` without mutating `nums`, you cannot mutate _nested_ list elements derived from `nums`
   without also mutating `nums`.  Shallow copies contain _references_ to objects inserted into it
   _not_ copies.

4. `nums4` is a _deep copy_ of nums returned by passing `nums` to the `copy` module's `deepcopy`
   function. `nums4` is a true copy of `nums` without residual references to the original list.
   Mutating `nums4` element values does not mutate the values contained in the original list.
