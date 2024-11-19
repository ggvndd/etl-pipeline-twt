from etl.extract import fetch_twitter_trends, fetch_google_trends
def test_fetch_twitter_trends():
    API_KEY = 'qvX4Zq69gxYO9bmPpcE2HBzWR'
    API_KEY_SECRET = 'CNhVsfWIH8wkB7xNMHXmhQVlmUrSm8ruO3p8XpUBKRApFzhR7k'
    ACCESS_TOKEN = '1081790378729066497-ISlmB5WusykCcDjwftd3TtfaLTsKiV'
    ACCESS_TOKEN_SECRET = '6yYU43aRCmnliSUOymRXFKFwVSiDZOzOMtLKZNg8NzHtw'
    #Bearer = AAAAAAAAAAAAAAAAAAAAANTxwwEAAAAAc5tt0dum2yxXSYmjCDSbPXFXR0Q%3DoJ2npeXQpLspUxUSFhXMViy4t7cmadXjSRxIqu0XETTGG1IcIx
    twitter_trends = fetch_twitter_trends(
        API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
    )
    
    assert isinstance(twitter_trends, list), "Twitter trends should be a list"
    assert "topic" in twitter_trends[0], "Each trend should have a 'topic' field"
    
def test_fetch_google_trends():
    keywords = ["AI", "Python"]
    google_trends = fetch_google_trends(keywords)
    assert not google_trends.empty, "Google trends should not be empty"
    assert "date" in google_trends.columns, "'date' column should be present"

if __name__ == "__main__":
    API_KEY = 'qvX4Zq69gxYO9bmPpcE2HBzWR'
    API_KEY_SECRET = 'CNhVsfWIH8wkB7xNMHXmhQVlmUrSm8ruO3p8XpUBKRApFzhR7k'
    ACCESS_TOKEN = '1081790378729066497-ISlmB5WusykCcDjwftd3TtfaLTsKiV'
    ACCESS_TOKEN_SECRET = '6yYU43aRCmnliSUOymRXFKFwVSiDZOzOMtLKZNg8NzHtw'
    twitter_trends = fetch_twitter_trends(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    print("Twitter Trends:", twitter_trends)

    keywords = [trend["topic"] for trend in twitter_trends]
    google_trends = fetch_google_trends(keywords)
    print("Google Trends:", google_trends)
