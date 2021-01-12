def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                x-------x
                |       |
                |       0
                |      /|\\
                |      / \\
                |
                """,
                # head, torso, both arms, and one leg
                """
                x-------x
                |       |
                |       0
                |      /|\\
                |      /
                |
                """,
                # head, torso, and both arms
                """
                x-------x
                |       |
                |       0
                |      /|\\
                |
                |
                """,
                # head, torso, and one arm
                """
                x-------x
                |       |
                |       0
                |       |
                |
                |
                """,
                # head and torso
                """
                x-------x
                |       |
                |       0
                |
                |
                |
                """,
                # head
                """
                x-------x
                |
                |
                |
                |
                |
                """,
                # initial empty state
                """
                x-------x
                """
    ]
    return stages[tries]