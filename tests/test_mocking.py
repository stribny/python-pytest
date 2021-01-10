from unittest.mock import patch
from python_pytest.mocking import is_link_on_result_page


def test_check_link_in_result_can_recognize_if_link_present():
    # given
    query = "python"
    link = 'https://stribny.name'
    result_page = f'<a href="{link}"></a>'

    # then
    with patch('python_pytest.mocking.download_google_result_page', lambda query: result_page):
        assert is_link_on_result_page(link, query) == True
