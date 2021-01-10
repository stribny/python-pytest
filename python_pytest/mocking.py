import requests


def download_google_result_page(query: str) -> str:
    results_page = requests.get(f"https://www.google.com/search?q={query}")
    return results_page.text


def is_link_on_result_page(link: str, query: str) -> bool:
    return True if link in download_google_result_page(query) else False

