import requests


# TODO: handle authentifications with api_keys stored in assistant
def handleAction(action: dict) -> dict:
    """
    :param action: Action dictionary ("endpoint", "method", ("json"))
    :return: Locals dictionary
    """
    headers = { "Content-Type": "application/json" }

    response = requests.request(
        url= action["endpoint"],
        method= action["method"],
        headers= headers,
        json= action["json"] if "json" in action else None,
    )
    return response.json()