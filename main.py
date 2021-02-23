from madlib_library import silly_animal, starwars, unicorns
import random

#Madlibs Game
# Project Overview:
# 1. Each Madlib + Input Prompts are stored in their own python File 
# 2. Randomly select one of these madlibs to play

arr = [silly_animal, starwars, unicorns]
arr = random.choice(arr)

if __name__ == "__main__":
    arr.madlibs()