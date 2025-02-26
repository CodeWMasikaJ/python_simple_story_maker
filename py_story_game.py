def silly_story_generator():
    """Generates a silly story based on user input."""

    noun = input("Enter a noun (e.g., dog, table): ")
    adjective = input("Enter an adjective (e.g., silly, bright): ")
    verb = input("Enter a verb (e.g., jump, sing): ")
    place = input("Enter a place (e.g., park, school): ")

    story = f"Once upon a time, there was a {adjective} {noun} that loved to {verb} at the {place}."

    print("\nHere's your silly story:")
    print(story)

silly_story_generator()