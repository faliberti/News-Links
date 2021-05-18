import os
import pytest
import datetime as dt

from app.news_link import get_article_links

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")
def article_links_test():
    startdate = dt.date(int(2021), int(5), int(4))
    enddate = dt.date(int(2021), int(5), int(14))
    result = get_article_links(keyword=tesla, user_start_date=startdate, user_end_date=enddate, sorting_choice='newest')
    assert result["totalResults"] == 7139
    assert result['articles'][0]['url'] == 'https://www.daemonology.net/hn-daily/2021-05-14.html'
    
