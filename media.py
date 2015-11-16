# import webbrowser
# the above 'import' statement is not actually needed but can be used
# to test the loading of a video trailer if fresh_tomatoes would not
# work for example


class Movie():
    """This class provides a way to store movie related information"""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, release_year, lead_actor):
                    self.title = movie_title
                    self.storyline = movie_storyline
                    self.poster_image_url = poster_image
                    self.trailer_youtube_url = trailer_youtube
                    self.year = release_year
                    self.actor = lead_actor


    
        
