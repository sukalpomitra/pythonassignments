# template for "Stopwatch: The Game"
import simplegui
# define global variables
interval = 0
stops = 0
score = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = str(t / 600)
    seconds = str((t % 600) / 10)
    if len(seconds) < 2:
        seconds = "0" + seconds
    tenths = str((t % 600) % 10)
    return minutes + ":" + seconds + "." + tenths
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global stops
    global score
    if timer.is_running():
        timer.stop()
        stops = stops + 1
        if (interval % 10) == 0:
            score = score + 1
    
def reset():
    global interval
    global stops
    global score
    timer.stop()
    interval = 0
    stops = 0
    score = 0

# define event handler for timer with 0.1 sec interval
def updateTime():
    global interval
    interval = interval + 1
    

# define draw handler
def draw(canvas):
    time = format(interval)
    canvas.draw_text(time, (300, 350), 72, 'White')
    canvas.draw_text(str(score) + "/" + str(stops), (650, 50), 72, 'Yellow')
    
# create frame
frame = simplegui.create_frame('StopWatch', 800, 600)

# register event handlers
timer = simplegui.create_timer(100, updateTime)
frame.set_draw_handler(draw)
frame.add_button('Start', start,200)
frame.add_button('Stop', stop,200)
frame.add_button('Reset', reset,200)
# start frame
frame.start()

# Please remember to review the grading rubric
