#!/usr/bin/python3

import turtle  # Import turtle graphics for creating the game window and objects
import time    # Import time module for delay in game execution
import random  # Import random module to generate random coordinates for the food

# Delay between moves
delay = 0.1  # This sets the delay between moves of the snake
segments = []  # This list will hold the body segments of the snake as it grows

# Setup the screen
wn = turtle.Screen()  # Create a screen/window object
wn.title("Snake Game By Cobby")  # Set the window title
wn.bgcolor("green")  # Set the background color of the window to green
wn.setup(width=600, height=600)  # Set the size of the window to 600x600 pixels
wn.tracer(0)  # Turns off the automatic screen updates to manually control the screen refresh

# Snake head setup
head = turtle.Turtle()  # Create the snake's head as a turtle object
head.speed(0)  # Set the initial speed of the head (0 is the fastest for drawing)
head.shape("square")  # Set the shape of the head to a square
head.color("black")  # Set the color of the snake head to black
head.penup()  # Disable drawing a line when the head moves
head.goto(0, 0)  # Set the initial position of the head to the center of the screen
head.direction = "stop"  # Initial direction is set to "stop", so the snake doesn't move until the player controls it

# Snake food setup
food = turtle.Turtle()  # Create the food as a turtle object
food.speed(0)  # Set the speed of the food object
food.shape("circle")  # Set the shape of the food to a circle
food.color("red")  # Set the color of the food to red
food.penup()  # Disable drawing a line when the food moves
food.goto(0, 100)  # Set the initial position of the food (randomly placed on the board)

# Function to change the direction of the snake to "up"
def go_up():
    if head.direction != "down":  # Prevent the snake from reversing
        head.direction = "up"

# Function to change the direction of the snake to "down"
def go_down():
    if head.direction != "up":  # Prevent the snake from reversing
        head.direction = "down"

# Function to change the direction of the snake to "right"
def go_right():
    if head.direction != "left":  # Prevent the snake from reversing
        head.direction = "right"

# Function to change the direction of the snake to "left"
def go_left():
    if head.direction != "right":  # Prevent the snake from reversing
        head.direction = "left"

# Function to move the snake based on its current direction
def move():
    if head.direction == "up":
        y = head.ycor()  # Get the current y-coordinate of the head
        head.sety(y + 20)  # Move the head 20 pixels upwards

    if head.direction == "down":
        y = head.ycor()  # Get the current y-coordinate of the head
        head.sety(y - 20)  # Move the head 20 pixels downwards

    if head.direction == "left":
        x = head.xcor()  # Get the current x-coordinate of the head
        head.setx(x - 20)  # Move the head 20 pixels to the left

    if head.direction == "right":
        x = head.xcor()  # Get the current x-coordinate of the head
        head.setx(x + 20)  # Move the head 20 pixels to the right

# Keyboard bindings (listen for specific keypresses and call respective functions)
wn.listen()  # Listen for keyboard input
wn.onkeypress(go_up, "w")  # Call go_up function when "w" key is pressed
wn.onkeypress(go_down, "s")  # Call go_down function when "s" key is pressed
wn.onkeypress(go_right, "d")  # Call go_right function when "d" key is pressed
wn.onkeypress(go_left, "a")  # Call go_left function when "a" key is pressed

# Main game loop
while True:
    wn.update()  # Update the screen after every iteration of the game loop

    # Check for collision with the border of the game screen
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)  # Pause the game for 1 second after collision
        head.goto(0, 0)  # Reset the head's position to the center of the screen
        head.direction = "stop"  # Stop the snake's movement

        # Hide all the segments of the snake's body after collision
        for segment in segments:
            segment.goto(1000, 1000)  # Move segments far off-screen
        
        # Clear the list of segments to reset the snake's body length
        segments.clear()

    # Check for collision between the snake's head and the food
    if head.distance(food) < 20:  # If the head is close enough to the food
        # Move the food to a random position within the screen's boundaries
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a new segment to the snake's body
        new_segment = turtle.Turtle()  # Create a new segment
        new_segment.speed(0)  # Set its speed to maximum (instantaneous)
        new_segment.shape("square")  # Shape of the segment is square
        new_segment.color("grey")  # Set the color of the segment to grey
        new_segment.penup()  # Disable drawing while moving
        segments.append(new_segment)  # Add the new segment to the list of segments

    # Move the end segments of the snake's body first, in reverse order
    for index in range(len(segments) - 1, 0, -1):
        # Move each segment to the position of the previous segment
        x = segments[index - 1].xcor()  # Get the x-coordinate of the previous segment
        y = segments[index - 1].ycor()  # Get the y-coordinate of the previous segment
        segments[index].goto(x, y)  # Move the segment to the previous segment's position

    # Move the first segment to the current position of the head
    if len(segments) > 0:
        x = head.xcor()  # Get the x-coordinate of the head
        y = head.ycor()  # Get the y-coordinate of the head
        segments[0].goto(x, y)  # Move the first segment to the head's position

    move()  # Call the move function to move the snake in the current direction

    # Check for collision between the head and the body segments
    for segment in segments:
        if segment.distance(head) < 20:  # If the head collides with a segment
            time.sleep(1)  # Pause the game for 1 second after collision
            head.goto(0, 0)  # Reset the head's position to the center of the screen
            head.direction = "stop"  # Stop the snake's movement

            # Hide all the segments of the snake's body after collision
            for segment in segments:
                segment.goto(1000, 1000)  # Move segments far off-screen

            # Clear the list of segments to reset the snake's body length
            segments.clear()

    time.sleep(delay)  # Control the game speed by adding a delay after each loop iteration

wn.mainloop()  # Keep the window open until the player closes it
