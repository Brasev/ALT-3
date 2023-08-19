from turtle import *  # Import necessary modules: turtle and csv.
import turtle
import csv

ws = turtle.Screen()  # Set up the turtle screen.
width = 1000
height = 600
ws.setup(width, height)
ws.tracer(1)

gravity = turtle.textinput("Gravity", "Enter gravity (1-5 works best)")  # Set gravity using user input.
velocity = turtle.textinput("Velocity", f"Gravity: {gravity} \nEnter Velocity (y, 1-20 works best)")  # Set y-velocity using user input.
xvelocity = turtle.textinput("Velocity", f"Gravity: {gravity}\nY Velocity: {velocity} \nEnter Velocity (x, 1-20 works best)")  # Set x-velocity using user input.

original_velocity = velocity  # Store the original velocity value
original_xvelocity = xvelocity  # Store the original xvelocity value

ball = turtle.Turtle()  # Set properties of the ball object.
ball.color("green")
ball.shape("circle")
ball.penup()
energy_loss = 0.8  # Set energy loss value.
x_energy_loss = 0.95  # Set x-energy loss value.
cut_off = 0.001  # Set cutoff value.
cor = []  # Create an empty list to store x and y coordinates.

myFile = open("ballpositions.csv", 'w', newline="")  # Open a CSV file to write ball positions.
writer = csv.writer(myFile)
writer.writerow(['X', 'Y', "Gravity", "yv", "xv"])  # Write headers to the CSV file.


x = 0  # Initialize x variable.
y = 0  # Initialize y variable.

while True:  # Start an infinite loop.
    velocity = float(velocity) - float(gravity)  # Update velocity based on gravity.

    x += float(xvelocity)  # Update x position based on x-velocity.
    y += float(velocity)  # Update y position based on velocity.

    ball.setx(x)  # Move the ball to the updated x position.
    ball.sety(y)  # Move the ball to the updated y position.

    cor.append(ball.pos())  # Append the current position to the x-coordinate list.

    if ball.ycor() < -height / 2 - 20:  # Check if the ball is below the screen.
        velocity = int(-velocity + float(gravity)) * energy_loss  # Update velocity with energy loss and gravity.

        if abs(velocity) < cut_off:  # Check if velocity is below cutoff.
            break  # Exit the loop if velocity is below cutoff.
        elif abs(velocity) < 25:  # Check if velocity is below a certain threshold.
            xvelocity = int(xvelocity) * x_energy_loss  # Update x-velocity with energy loss.

    if ball.xcor() > width / 2 or ball.xcor() < -width / 2:  # Check if the ball is outside the screen horizontally.
        xvelocity = -int(xvelocity)  # Reverse the x-velocity if it hits the boundary.

    myFile = open("ballpositions.csv", 'a', newline="")  # Open the CSV file in append mode.
    writer = csv.writer(myFile)
    #writer.writerow([cor[-1],"", gravity, velocity, xvelocity])  # Write the last recorded position to the CSV file.
    #writer.writerow(cor[-1])
    xc, yc = ball.pos()
    writer.writerow([xc,yc,gravity, original_velocity, original_xvelocity])
    print(ball.pos())  # Print the current position of the ball.

turtle.done()  # Exit the turtle graphics environment.
