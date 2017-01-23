
class Movie:
    """Creates movie object that maps movie with various attributes.
    Raises:
        TypeError: If missing the four(4) required positional arguments.
    """

    def __init__(self, title, storyline, poster_image, trailer_video):
        self.title                  = title
        self.storyline              = storyline
        self.poster_image_url       = poster_image
        self.trailer_youtube_url    = trailer_video
