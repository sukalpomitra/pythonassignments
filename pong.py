# Implementation of classic arcade game Pong

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

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos =[WIDTH / 2 , HEIGHT / 2]
    if (direction == RIGHT):
        vHoriz = random.randrange(120,240)
    else:
        vHoriz = -1 * random.randrange(120,240)
    vVert = -1 * random.randrange(60,180)
    ball_vel = [vHoriz/60.0,vVert/60.0]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,score1,score2  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = 199
    paddle2_pos = 199
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    
    if random.randint(0,1) == 0:
        spawn_ball(LEFT)
    else:
        spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel
    radius = 5
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ball_pos[1] <= radius + 5 or ball_pos[1] >= (HEIGHT - 1) - (radius + 5):
        ball_vel[1] = -1 * ball_vel[1]
        
    
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos,radius,5,"White","White")
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos <= PAD_HEIGHT / 2 and paddle1_vel < 0:
        paddle1_vel = 0
    if paddle1_pos >= (HEIGHT - 1) - (PAD_HEIGHT / 2) and paddle1_vel > 0:
        paddle1_vel = 0
    if paddle2_pos <= PAD_HEIGHT / 2 and paddle2_vel < 0:
        paddle2_vel = 0
    if paddle2_pos >= (HEIGHT - 1) - (PAD_HEIGHT / 2) and paddle2_vel > 0:
        paddle2_vel = 0
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos - (PAD_HEIGHT / 2)],[0, paddle1_pos + (PAD_HEIGHT / 2)],[PAD_WIDTH,paddle1_pos + (PAD_HEIGHT / 2)],[PAD_WIDTH, paddle1_pos - (PAD_HEIGHT / 2)]], 1, "White","White")
    canvas.draw_polygon([[WIDTH, paddle2_pos - (PAD_HEIGHT / 2)],[WIDTH, paddle2_pos + (PAD_HEIGHT / 2)],[WIDTH - PAD_WIDTH,paddle2_pos + (PAD_HEIGHT / 2)],[WIDTH - PAD_WIDTH, paddle2_pos - (PAD_HEIGHT / 2)]], 1, "White","White")
    # determine whether paddle and ball collide  
    
    if ball_pos[0] <= ((PAD_WIDTH + 5) + radius) and (ball_pos[1] <= paddle1_pos + (PAD_HEIGHT / 2) and ball_pos[1] >= paddle1_pos - (PAD_HEIGHT / 2)):
        ball_vel[0] = -1 * (ball_vel[0] + (.1 * ball_vel[0]))
        ball_vel[1] = (ball_vel[1] + (.1 * ball_vel[1]))
    elif ball_pos[0] <= (PAD_WIDTH + 5) + radius:
        score2 += 1
        spawn_ball(RIGHT)
    
    if ball_pos[0] >= (WIDTH - 1) - ((PAD_WIDTH + 5) + radius) and (ball_pos[1] <= paddle2_pos + (PAD_HEIGHT / 2) and ball_pos[1] >= paddle2_pos - (PAD_HEIGHT / 2)):
        ball_vel[0] = -1 * (ball_vel[0] + (.1 * ball_vel[0]))
        ball_vel[1] = (ball_vel[1] + (.1 * ball_vel[1]))
    elif ball_pos[0] >= (WIDTH - 1) - ((PAD_WIDTH + 5) + radius):
        score1 += 1
        spawn_ball(LEFT)
    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 4,HEIGHT / 2], 24, "White")
    canvas.draw_text(str(score2), [WIDTH - WIDTH / 4,HEIGHT / 2], 24, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel += 3
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel += 3
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 3
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 3

def reset():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
button1 = frame.add_button('Reset', reset,200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()