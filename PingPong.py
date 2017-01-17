# Implementation of classic arcade game Pong
# Works only when opened or copy pasted in http://www.codeskulptor.org

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [3, -1]
paddle1_pos = [PAD_WIDTH / 2, HEIGHT / 2 ]
paddle2_pos = [WIDTH - PAD_WIDTH / 2, HEIGHT / 2 ]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, LEFT, RIGHT # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [3, -1]
 
    if direction == False:
        ball_vel[0] = -ball_vel[0]
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)
  

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
       
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH: 
        if (ball_pos[1] - paddle1_pos[1]) ** 2 > (PAD_HEIGHT / 2) ** 2:
            score2 += 1
            spawn_ball(RIGHT)
        else:
            ball_vel[0] = -(ball_vel[0] + 0.1 * ball_vel[0])
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if (ball_pos[1] - paddle2_pos[1]) ** 2 > (PAD_HEIGHT / 2) ** 2:
            score1 += 1
            spawn_ball(LEFT)
        else:
            ball_vel[0] = -(ball_vel[0] + 0.1 * ball_vel[0])
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, 'Green', 'Green')
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel[1]
    paddle2_pos[1] += paddle2_vel[1]
    
    if paddle1_pos[1] <= HALF_PAD_HEIGHT:
        paddle1_pos[1] = HALF_PAD_HEIGHT
    elif paddle1_pos[1] >= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - HALF_PAD_HEIGHT
        
    if paddle2_pos[1] <= HALF_PAD_HEIGHT:
        paddle2_pos[1] = HALF_PAD_HEIGHT
    elif paddle2_pos[1] >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT
        
    # draw paddles
    canvas.draw_polygon([[paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT], [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT], [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT]], 1, "Red", "Red")
    canvas.draw_polygon([[paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT]], 1, "Blue", "Blue")
        
    # draw scores
    
    canvas.draw_text(str(score1), [145, 50], 50, 'Red')
    canvas.draw_text(str(score2), [445, 50], 50, 'Blue')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 5
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= vel
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] += vel
    elif key == simplegui.KEY_MAP["W"]:
        paddle1_vel[1] -= vel
    elif key == simplegui.KEY_MAP["S"]:
        paddle1_vel[1] += vel
          
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0
    if key == simplegui.KEY_MAP["W"] or key == simplegui.KEY_MAP["S"]:
        paddle1_vel[1] = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button('Restart', new_game, 100)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)



# start frame
new_game()
frame.start()