label questions:
    # questions are constructed as tuples
    # first item: question as a string
    # second item: possible answers as another tuple
    # third item: correct answer as an integer.
    # note the zero-based numbering. the first possible answer is "0", the second is "1", the third is "2"

    $ q_01 = ("Who plays \"Buffy\" in the 1992 film \"Buffy the Vampire Slayer\"?",
        ("Sarah Michelle Geller", "Kristy Swanson", "Kate Beckinsale"),
        1)
    $ q_02 = ("A dhampir is an offspring of a vampire and a mortal.\n Who is not a dhampir?",
        ("Rayne", "Adrian Tepes", "Gabriel Van Helsing"),
        2)
    $ q_03 = ("Who wrote the novel \"Dracula\"?",
        ("Neil Gaiman", "Bram Stoker", "Stephen King"),
        1)
    $ q_04 = ("In the world of \"Vampire the Masquerade\", which clan has the gift of insight?",
        ("Malkavian", "Tremere", "Brujah"),
        0)
    $ q_05 = ("In Castlevania, who is the first Belmont?",
        ("Simon", "Trevor", "Leon"),
        2)
    $ q_06 = ("This vampire is not a detective.",
        ("Selene", "Nick Knight", "Angel"),
        0)
    $ q_07 = ("What series did Hideyuki Kikuchi create?",
        ("Blood+", "Vampire Hunter D", "Hellsing"),
        1)
    $ q_08 = ("Who is the sire of Angelus?",
        ("Drusilla", "Darla", "Dracula"),
        1)
    $ q_09 = ("In what year was Eric Brooks born?",
        ("1992", "1972", "1922"),
        2)
    $ q_10 = ("How did Claudia try to kill Lestat?",
        ("Poisoned Blood", "Sunlight", "Garlic"),
        0)

    # add the questions to the list below
    # the list will be used and shuffled in script.rpy

    $ question_list = [q_01, q_02, q_03, q_04, q_05, q_06, q_07, q_08, q_09, q_10]

    return
