from pytube import YouTube

YouTube(
    'http://youtube.com/watch?v=2lAe1cqCOXo',
    use_oauth=False,
    allow_oauth_cache=True
)