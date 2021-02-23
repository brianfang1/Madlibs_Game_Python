def madlibs():
    adjective1 = input("Adjective: ")
    noun_animal = input("Noun (Animal): ")
    noun_country = input("Noun (Country): ")
    color1 = input("Color: ")
    number = input("Number: ")
    food_plural = input("Noun (Food, Plural): ")
    verb1 = input("Verb: ")
    song_name = input("Song Name: ")
    emotion1 = input("Emotion (Feeling): ")
    language = input("Language: ")
    emotion2 = input("Emotion (Feeling): ")

    madlib = f"Silly Animal Tale \
    \
    There was once a {adjective1} \
    {noun_animal} from {noun_country}. \
    Nobody knew he was a {noun_animal} \
    because he had {color1} fur and \
    ate {number} {food_plural} each \
    day. He liked to {verb1} and \
    sing {song_name}. Whenever \
    he was {emotion1}, he would start \
    speaking {language}. Then he would \
    feel {emotion2}!"


    print(madlib)