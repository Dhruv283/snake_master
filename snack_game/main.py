import pygame
import random
import os


pygame.mixer.init()





pygame.init()


white = (255,255,255)
red = (255,0,0)
black =(0,0,0)
screen_width = 900
screen_height = 600
gamewindow = pygame.display.set_mode((screen_width ,screen_height))
bg ="C:\\python\\pygame\\snack_game\\bg.jpg"

bgimg = pygame.image.load(bg)
bgimg = pygame.transform.scale(bgimg,(screen_width, screen_height)).convert_alpha()



pygame.display.set_caption("Snakes master")
pygame.display.update()
clock = pygame.time.Clock() 
font = pygame.font.SysFont(None, 55)





def screen_score(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])




def plot_snake(gamewindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])


def welcome():
        exit_game = False

        while not exit_game:

            gamewindow.fill((255,165,0))
            gamewindow.blit(bgimg, (0,0))
            screen_score("Welcome to Snake master",white,200,20)
            screen_score("Press enter!!!",white,310,60)
            # font = pygame.font.SysFont(None, 20)
            screen_score("Devlop by : Dhruv Patel",red,10,560)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        back ="C:\\python\\pygame\\snack_game\\back.mp3"
                        pygame.mixer.music.load(back)
                        pygame.mixer.music.play()
                        gameloop()   
            
            pygame.display.update()
            clock.tick(60)



        




def gameloop():

    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size= 10
    fps = 60
    food_x = random.randint(20,screen_width/1.2)
    food_y =  random.randint(20,screen_height/1.2)
    score = 0  
    init_velocity= 3

    snk_list = []
    snk_length = 1

    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt","w") as f:
            f.write("0")

    with open("hiscore.txt","r") as f:
        hiscore = f.read()


    while not exit_game:
        if game_over:
            with open("hiscore.txt","w") as f:
                f.write(str(hiscore))

            gamewindow.fill((255,165,0))
            screen_score("Game over !!!!!!  Press Enter to continue ",black, 100, 250)
            screen_score("Press Q to exit ",black, 300, 290)


            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

                    if event.key == pygame.K_q:
                        exit_game = True




        else:

            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0


                    if event.key == pygame.K_d:
                        score += 10

                    


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y


            if abs(snake_x-food_x)<3 and (snake_y-food_y)<3:
                score += 10 
                # print("Score:",score*10)
                snk_length += 5
                if score>int(hiscore):
                    hiscore = score
                
                
                food_x = random.randint(20,screen_width/1.2)
                food_y =  random.randint(20,screen_height/1.2)


            gamewindow.fill(black)
            screen_score("Score : "+ str(score) + " HighScore:"+ str(hiscore), (255,165,0), 5, 5)


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            pygame.draw.rect(gamewindow, red, [food_x,food_y, snake_size, snake_size])

            if len(snk_list)>snk_length:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True


            plot_snake(gamewindow, white, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)



    pygame.quit()
    quit()
welcome()
