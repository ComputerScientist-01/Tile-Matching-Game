import pygame
import game_config as gc

from pygame import display, event, image
from time import sleep
from animal import Animal

def find_index_from_xy(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return row, col, index

pygame.init()
# used to initialize the pygame methods
display.set_caption('My Game')
# set the game title on the title screen
screen = display.set_mode((gc.SCREEN_SIZE, gc.SCREEN_SIZE))
# defining the window size of the screen
matched = image.load('other_assets/matched.png')
# loading the image assets
#screen.blit(matched,(0,0)) -> not needed for now 
#displaying the image in full screen mode 
#blit -> draw one image onto another

#display.flip() -> not needed for now
#display.flip() -> This will update the contents of the entire display

running = True
# set a boolean for the while loop

tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]
# we will instantiate the images
current_images_displayed = []

while running: #setting up the game loop
    current_events = event.get()
    #This will get all the messages and remove them from the queue

    for e in current_events:# looping over the events
        if e.type == pygame.QUIT:#if user wants to quit exit the game loop
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
                # pressing escape will lead to quiting of the game

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #getting the positiion of mouse after clicking on animal
            row, col, index = find_index_from_xy(mouse_x, mouse_y)
            # using a function to find the row and column number
            if index not in current_images_displayed:
                if len(current_images_displayed) > 1:
                    current_images_displayed = current_images_displayed[1:] + [index]
                    	# we are doing this so that unique images get matched	
			            #appending the index to the list current images
                else:
                    current_images_displayed.append(index)

    # Display animals
    screen.fill((255, 255, 255))
    # set wthe screen color to white
    total_skipped = 0

    for i, tile in enumerate(tiles):
        current_image = tile.image if i in current_images_displayed else tile.box
        # if the image is present in current images
        # display it other wiise display a grey box
        if not tile.skip:
            screen.blit(current_image, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
            #iterating over tiles and displaying them
            # enumerate gives the iterator index
        else:
            total_skipped += 1

    display.flip()
    #update the screen with display.flip()

    # Check for matches
    if len(current_images_displayed) == 2:
        idx1, idx2 = current_images_displayed
        if tiles[idx1].name == tiles[idx2].name:
            tiles[idx1].skip = True
            tiles[idx2].skip = True
            # display matched message
            sleep(0.2)
            screen.blit(matched, (0, 0))
            display.flip()
            sleep(0.5)
            current_images_displayed = []

    if total_skipped == len(tiles):
        running = False

print('Goodbye!')
