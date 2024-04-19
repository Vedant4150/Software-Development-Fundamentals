import sys

try:
    import turtle
except ImportError:
    print("The turtle module is not installed. Please install it before running this script.")
    sys.exit(1)

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Bouncing Ball Animation")
screen.tracer(0)  # Turns off the screen updates for better performance

# Create a turtle object for the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)

# Set the initial position and velocity of the ball
ball.goto(0, 200)
dx, dy = 2, -2  # Initial velocity components in the x and y directions

# Define the boundaries of the screen
screen_width = screen.window_width() / 2
screen_height = screen.window_height() / 2

# Function to exit the program
def quit_animation():
    screen.bye()

# Function to increase speed
def increase_speed():
    global dx, dy
    dx *= 1.1
    dy *= 1.1

# Function to decrease speed
def decrease_speed():
    global dx, dy
    dx *= 0.9
    dy *= 0.9

# Bind the exit function to a key press
screen.onkeypress(quit_animation, "q")
screen.onkeypress(increase_speed, "Up")
screen.onkeypress(decrease_speed, "Down")
screen.listen()

# Main animation loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

    # Check for collision with the walls
    if ball.xcor() > screen_width or ball.xcor() < -screen_width:
        dx *= -1  # Reverse the x-direction
    if ball.ycor() > screen_height or ball.ycor() < -screen_height:
        dy *= -1  # Reverse the y-direction

    screen.update()  # Only update the screen after changes

# Keep the window open until it is closed by the user
screen.mainloop()
