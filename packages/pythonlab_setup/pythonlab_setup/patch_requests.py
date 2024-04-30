import requests
import urllib.parse

def get_proxy_path(host, url, channel_id):
    return f"{host}/xhr?u={urllib.parse.quote(url, safe='/:')}&c={urllib.parse.quote(channel_id, safe='/:')}"


def patch_requests(host, channel_id):
    print("in patch requests")
    # try:
    #     requests.has_been_patched
    #     print("has been patched already")
    # except:
    print("patching...")
    _old_get = requests.get

    def get(url, params=None, **kwargs):
        print("hello from patch!")
        print(f"host: {host}, url: {url}, channel_id: {channel_id}")
        url = get_proxy_path(host, url, channel_id)
        return _old_get(url, params, **kwargs)

    requests.get = get
        # requests.has_been_patched = True
