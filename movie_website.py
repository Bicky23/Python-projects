import webbrowser

class Movie():
    """ This class defines a movie """
    def __init__(self, title, storyline, poster_image, youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image = poster_image
        self.youtube_url = youtube_url

    def show_trailer(self):
        webbrowser.open(self.youtube_url)

toy_story = Movie('Toy Story', 'Anime Film',
                  'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story_jpg',
                 'https://www.youtube.com/watch?v=vwyZH85NQC4')


# print(toy_story.storyline)
# print(toy_story.youtube_url)
# toy_story.show_trailer()
print(toy_story.__doc__)
