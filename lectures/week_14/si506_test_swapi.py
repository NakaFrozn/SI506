import requests


def get_swapi_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    content of one or more entities to be found in ["results"] list; otherwise, response
    object body is returned as a single dictionary representation of the SWAPI entity.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        Response: requests.Response object.
    """

    if params:
        return requests.get(url, params, timeout=timeout)
    else:
        return requests.get(url, timeout=timeout)


def main():
    """Program entry point. Orcheestrates flow of execution.

    Parameters:
        None

    Returns:
        None
    """

    # SWAPI resource URI (Uniform Resource Identifier)
    resource = "https://swapi.py4e.com/api/people/"

    # HTTP GET request / response
    response = get_swapi_resource(resource, {"search": "Darth Vader"})

    # Response object type (<class 'requests.models.Response'>)
    print(f"\nresponse = {type(response)}")

    # Decode JSON response (to dict)
    envelope = response.json()  # four key-value pairs: count, next, previous, results

    print(f"\nEnvelope ({type(envelope)}) = {envelope}")

    # Access Darth Vader from the "envelope"
    vader = envelope["results"][0]

    print(f"\nDarth Vader ({type(vader)}) = {vader}")

    # Extract Darth Vader's homeworld URL
    homeworld_url = vader["homeworld"]

    # Retrieve Darth Vader's homeworld
    homeworld = get_swapi_resource(homeworld_url).json()  # deserialize JSON to dict

    print(f"\nVader's homeworld {homeworld['name']} ({type(homeworld)}) = {homeworld}")


if __name__ == "__main__":
    main()
