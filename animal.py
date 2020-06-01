import random
import os
import game_config as gc

from pygame import image, transform

animals_count = dict((a, 0) for a in gc.ASSET_FILES)
#creating a dictionary to keep count of animals
#setting all the values to 0 for all the keys
#the keys are going to be all the files from our asset dir
def available_animals():
    return [animal for animal, count in animals_count.items() if count < 2]

#returns a list of animals which are available
#meaning all the keys whose values is less tha 2
class Animal:
    def __init__(self, index):
        self.index = index
        
        self.name = random.choice(available_animals())
        # randomly choose the name from all the available names
        
        self.image_path = os.path.join(gc.ASSET_DIR, self.name)
        # setting up our image path
        # os.path.join -> Join one or more path components intelligently

        self.row = index // gc.NUM_TILES_SIDE
        # we will get the resultant int as the row number
        
        self.col = index % gc.NUM_TILES_SIDE
        # we will get the resultant int as column number
        
        self.skip = False
        # if the animals are matched the we can skip
        # printing the image/box as it has been
        # removed from the game

        self.image = image.load(self.image_path)
        # loading the images

        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))
        #pygame.transform.scale -> resize to new resolution
        # we are subtracting the margin length to get actual size

        self.box = self.image.copy()
        # creating a copy of the image

        self.box.fill((200, 200, 200))
         # filling the box to get a light grey color

        animals_count[self.name] += 1
        # updating the key value in the dictonary
