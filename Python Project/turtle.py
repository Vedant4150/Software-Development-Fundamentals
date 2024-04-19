import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Bouncing Ball Animation")
screen.tracer(0)  # Turns off the screen updates

# Create a turtle object for the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)

# Set the initial position and velocity of the ball
ball.goto(0, 200)
dx, dy = 2, -2  # Velocity components in the x and y directions

# Define the boundaries of the screen
screen_width = screen.window_width() / 2
screen_height = screen.window_height() / 2

# Function to exit the program
def quit_animation():
    screen.bye()

# Bind the exit function to a key press, e.g., "q" for quit
screen.onkeypress(quit_animation, "q")
screen.listen()

# Animation loop
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

screen.mainloop()
