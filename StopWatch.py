# "Stopwatch: The Game"
# Works when opened or copy/pasted in http://www.codeskulptor.org

# importing modules
import simplegui

# define global variables
one_tenth_counter = 0
timer_status = False
stop_counter = 0
zero_stop_counter = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(timer):
    D = timer % 10
    temp1 = timer / 10
    C = temp1 % 10
    temp2 = temp1 / 10
    B = temp2 % 6
    A = temp2 / 6
    return str(A) + ":" + str(B) + str (C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer_status
    timer.start()
    timer_status = True
    
def stop():
    global timer_status, one_tenth_counter, stop_counter, zero_stop_counter
    timer.stop()
    if timer_status == True:
        timer_status = False
        stop_counter += 1
        if one_tenth_counter % 10 == 0:
            zero_stop_counter += 1
     
def reset():
    global one_tenth_counter, stop_counter, zero_stop_counter
    timer.stop()
    one_tenth_counter = 0
    zero_stop_counter = 0
    stop_counter = 0

# define event handler for timer with 0.1 sec interval
def update():
    global one_tenth_counter
    one_tenth_counter += 1

# define draw handler
def draw(canvas):
    clock_output = format(one_tenth_counter)
    canvas.draw_text(clock_output, [100, 200], 55, "White")
    canvas.draw_text(str(zero_stop_counter) + "/" + str(stop_counter), [340, 40], 30, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 400, 300)
frame.set_draw_handler(draw)
# register event handlers
start_button = frame.add_button('Start', start, 100)
stop_button = frame.add_button('Stop', stop, 100)
reset_button = frame.add_button('Reset', reset, 100)
timer = simplegui.create_timer(100, update)

# start frame and timer
frame.start()


# Please remember to review the grading rubric