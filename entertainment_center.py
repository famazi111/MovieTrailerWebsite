"""
Movie Trailer Website
Usage:
    Just run this file from your Python interpreter.
    Alternatively, you can open the 'fresh_tomatoes.html' file.
"""
__author__ = 'famazi'

from media import Movie
import fresh_tomatoes

# Movie Objects:
deadpool = Movie(
    'Deadpool',
    'This is the origin story of former Special Forces operative turned '
    'mercenary Wade Wilson, who after being subjected to a rogue experiment '
    'that leaves him with accelerated healing powers, adopts the alter ego '
    'Deadpool. Armed with his new abilities and a dark, twisted sense of '
    'humor, Deadpool hunts down the man who nearly destroyed his life.',
    'https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg',
    'https://www.youtube.com/watch?v=FyKWUTwSYAs')

avengers = Movie(
    'Avengers: Age of Ultron',
    "When Tony Stark and Bruce Banner try to jump-start a dormant peacekeeping "
    "program called Ultron, things go horribly wrong and it's up to Earth's "
    "Mightiest Heroes to stop the villainous Ultron from enacting his terrible"
    "plans.",
    'https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg',
    'https://www.youtube.com/watch?v=rD8lWtcgeyg')

the_witch = Movie(
    'The Witch',
    'A family in 1630s New England is torn apart by the forces of witchcraft, black magic and possession.',
    'https://upload.wikimedia.org/wikipedia/en/b/bf/The_Witch_poster.png',
    'https://www.youtube.com/watch?v=iQXmlf3Sefg')

the_martian = Movie(
    'The Martian',
    'After a massive storm forces his crew to leave the planet, an astronaut, '
    'Mark Watney (played by Matt Damon), is marooned on Mars, and presumed dead. '
    'Figuring that it would be at least four years until someone can rescue him, he sets out, '
    'though often ingenious means, to survive.',
    'https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg',
    'https://www.youtube.com/watch?v=ej3ioOneTy8')

furious7 = Movie(
    'Furious 7',
    "Brian O'Conner's now calm and peaceful life gets shaken up when he and his family are "
    "attacked. He and his crew soon find out that Deckard Shaw is seeking revenge for his "
    "brother Owen starting with the death of Hans. Brian now puts it all on the line for one last ride.",
    'https://upload.wikimedia.org/wikipedia/pt/b/b8/Furious_7_poster.jpg',
    'https://www.youtube.com/watch?v=Skpu5HaVkOc')

insurgent = Movie(
    'Insurgent',
    'Tris, Four, and her remaining allies are on the run from ruthless Jean Matthews, and '
    'her Erudite faction, where they take refuge at the Amity stronghold. While there, Tris '
    'learns that the Erudite are gaining power and decides that she must fight with her inner '
    'fears and decide what to do to protect her home.',
    'https://upload.wikimedia.org/wikipedia/en/a/af/Insurgent_poster.jpg',
    'https://www.youtube.com/watch?v=UtgPdoxU-SY')


def main():
    # store movie objects as list to be processed by fresh_tomatoes
    movies = [deadpool, avengers, the_witch, the_martian, furious7,
              insurgent]
    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    main()
