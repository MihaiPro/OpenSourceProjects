"""
This file will contain the Game class.
This class will be responsible for every action that our
main function was responsible for thus far.
"""
# Import the Player class from our player.py module
import os
from player import *
from main import *
from pprint import pprint as pp


class Game():
    def __init__(self, screen_width, screen_height, player_width, player_height, tile_size, background):
        # Initialize pygame
        pygame.init()

        # Create screen and add title
        self.screen = pygame.display.set_mode([screen_width, screen_height])
        pygame.display.set_caption("Game")

        # FPS clock. Will be used to set max fps
        self.clock = pygame.time.Clock()

        # Create a player object
        player_x, player_y = 1, 1
        self.player = Player(player_x, player_y, player_width, player_height, tile_size)

        # Set the game environment
        self.background = background        
        self.screen_width, self.screen_height = screen_width, screen_height        
        self.tile_size = tile_size
        self.tiles = self.read_mapfile('map.txt')
        self.camerax, self.cameray = 0, 0
        
    def read_mapfile(self, filename):
        """
        Reads a text file called filename and generates the map
        
        Input: Text file with spaces and #'s
        Output: 2 dimensional array of booleans
        """
        assert os.path.exists(filename), 'Cannot find the level file: %s' % (filename)
        
        # read file and store in a list
        mapfile_read = open(filename, 'r')
        content = mapfile_read.readlines() + ['\r\n']
        mapfile_read.close()

        levelmap = []    
        for linenum in range(len(content)):
           # process each line that was in the level file
            line = content[linenum].rstrip('\r\n')
            if line != '':
                levelmap.append([])
                for i in line:
                    if i == ' ':
                        levelmap[linenum].append(False)
                    elif i == '#':
                        levelmap[linenum].append(True)
                    else:
                        print("UNKONWN CHARACTER IN MAP FILE")
                
        return levelmap
        
    def draw_room(self, tiles, screen):
        """
        Notes: Draws the room
        Input:
            tiles - 2 dimensional array of booleans, True is a wall block
            screen - Pygame screen object
        """
        for y in range(len(tiles)):
            for x in range(len(tiles[y])):
                if tiles[y][x]:
                    pygame.draw.rect(screen, GRAY, [x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size], 0);

    def run(self):
        running = True
        while running:
            # Event processing
            for event in pygame.event.get():
                # If user hits 'x' exit
                if event.type == pygame.QUIT:
                    running = False
                # Key down events
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.move(0, -1, self.tiles)
                    elif event.key == pygame.K_DOWN:
                        self.player.move(0, 1, self.tiles)
                    elif event.key == pygame.K_RIGHT:
                        self.player.move(1, 0, self.tiles)
                    elif event.key == pygame.K_LEFT:
                        self.player.move(-1, 0, self.tiles)

            # Drawing
            self.screen.fill(self.background)            
            mapsurf = pygame.Surface((self.screen_width, self.screen_height))
            mapsurf.fill(BLUE)
            
            # Update and draw room
            self.draw_room(self.tiles, mapsurf)

            # Update and draw player
            self.player.draw(mapsurf)

            # Update the display
            mapsurf_rect = mapsurf.get_rect()
            mapsurf_rect.center = (int(self.screen_width / 2) + self.camerax, int(self.screen_height / 2) - self.cameray)
            self.screen.blit(mapsurf, mapsurf_rect)
            pygame.display.flip()

            # Set fps clock to 60 frames per second
            self.clock.tick(60)

        pygame.quit()
