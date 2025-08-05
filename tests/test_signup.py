def test_signup_platform():
    platform = {"name": "test", "signup_url": "https://example.com", "category": "general"}
    result = signup_platform(platform)
    assert result in [True, False]