# Dave, chatbot inutile v1.0
# (c) 2025 DancingCopter (GNU GPL v3)
# Ce bot est aussi con que drôle.

import threading
import time

secondes = 0

def chronometre():
    while True:
        time.sleep(1)
        global secondes
        secondes += 1

# Lancer le chronomètre (comme si quelqu'un en avait quelque chose à foutre)
thread = threading.Thread(target=chronometre, daemon=True)
thread.start()

print("bienvenue! :)\nje suis Dave, un chatbot inutile et completement con!\n")

def chat():
    reponse = input("que veut tu me dire ?\n")
    
    if reponse.lower() == "pourquoi est tu si con ?":
        print("parce que cette feignasse de DancingCopter est pas foutu de me rendre smart, il hardcode toute mes réponses, lol\n")
        chat()

    elif reponse.lower() == "comment t'appelles tu ?":
        print("je te l'ai deja dit, ducon (ouais je suis aigri, et alors mdrrrrr)\n")
        chat()

    # si la personne dit "bye", on simule une erreur, juste pour la faire flipper

    elif reponse.lower() == "bye":
        print("""Traceback (most recent call last):
  File "/data/user/0/ru.iiec.pydroid3/files/accomp_files/iiec_run/iiec_run.py", line 31, in <module>
    start(fakepyfile,mainpyfile)
    ~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/user/0/ru.iiec.pydroid3/files/accomp_files/iiec_run/iiec_run.py", line 30, in start
    exec(open(mainpyfile).read(),  __main__.__dict__)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 33, in <module>
  File "<string>", l""")
        print("\n\033[91mWTF C'EST QUOI CETTE MERDE?!\033[0m\n")

    elif reponse.lower() == "quelle age as tu ?":
        print(f"approximativement {secondes} secondes.\nMDRRRR\ntu t'attendais à rien, hein ?")
        chat()

    else:
        print("je te comprends pas zebi, je te l'ai dit que je suis con, lol")
        chat()

chat()
