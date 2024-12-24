# -*- coding: utf-8 -*-
"""Untitled33.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10I-ZUYZwdxLoHhSiMAAHPHgjbuKQc16M
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Function to plot the graph based on parameters a, b, and c
def update(val):
    a = slider_a.val
    b = slider_b.val
    c = slider_c.val
    x = np.linspace(-10, 10, 1000)
    y = a * x**2 + b * x + c
    line.set_ydata(y)
    fig.canvas.draw_idle()  # Update the plot

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.25)  # Adjust the bottom margin for sliders

# Define the x range for plotting
x = np.linspace(-10, 10, 1000)
y = 0 * x  # Initial y values (start with y=0)

# Plot the initial graph
line, = ax.plot(x, y, label="Graph", color="blue")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Interactive Graph with Adjustable Sliders')
ax.grid(True)
ax.axhline(0, color='black',linewidth=1)
ax.axvline(0, color='black',linewidth=1)
ax.legend()

# Create sliders for 'a', 'b', and 'c'
ax_slider_a = plt.axes([0.1, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_a = Slider(ax_slider_a, 'a', -10.0, 10.0, valinit=0, valstep=0.1)

ax_slider_b = plt.axes([0.1, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_b = Slider(ax_slider_b, 'b', -10.0, 10.0, valinit=0, valstep=0.1)

ax_slider_c = plt.axes([0.1, 0.11, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_c = Slider(ax_slider_c, 'c', -10.0, 10.0, valinit=0, valstep=0.1)

# Attach the update function to sliders
slider_a.on_changed(update)
slider_b.on_changed(update)
slider_c.on_changed(update)

# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Function to plot the graph based on the equation and the adjusted x, y ranges
def update(val):
    a = slider_a.val
    b = slider_b.val
    c = slider_c.val
    x_min = slider_x_min.val
    x_max = slider_x_max.val
    y_min = slider_y_min.val
    y_max = slider_y_max.val

    # Define the x values in the specified range
    x = np.linspace(x_min, x_max, 1000)

    # The equation of the graph (for example: y = a * x^2 + b * x + c)
    y = a * x**2 + b * x + c

    # Update the graph with the new data
    line.set_xdata(x)
    line.set_ydata(y)

    # Update the limits of the graph based on slider values
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])

    fig.canvas.draw_idle()  # Update the plot

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.35)  # Adjust the bottom margin for sliders

# Define the initial x and y range
x_init = np.linspace(-10, 10, 1000)
y_init = 0 * x_init  # Initial y values (y = 0)

# Plot the initial graph
line, = ax.plot(x_init, y_init, label="Graph", color="blue")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Interactive Graph with Adjustable Sliders')
ax.grid(True)
ax.axhline(0, color='black',linewidth=1)
ax.axvline(0, color='black',linewidth=1)
ax.legend()

# Create sliders for 'a', 'b', and 'c' (coefficients of the equation)
ax_slider_a = plt.axes([0.1, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_a = Slider(ax_slider_a, 'a', -10.0, 10.0, valinit=0, valstep=0.1)

ax_slider_b = plt.axes([0.1, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_b = Slider(ax_slider_b, 'b', -10.0, 10.0, valinit=0, valstep=0.1)

ax_slider_c = plt.axes([0.1, 0.11, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_c = Slider(ax_slider_c, 'c', -10.0, 10.0, valinit=0, valstep=0.1)

# Create sliders for adjusting the x and y range
ax_slider_x_min = plt.axes([0.1, 0.17, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_x_min = Slider(ax_slider_x_min, 'x min', -20.0, 0.0, valinit=-10, valstep=0.1)

ax_slider_x_max = plt.axes([0.1, 0.22, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_x_max = Slider(ax_slider_x_max, 'x max', 0.0, 20.0, valinit=10, valstep=0.1)

ax_slider_y_min = plt.axes([0.1, 0.27, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_y_min = Slider(ax_slider_y_min, 'y min', -20.0, 0.0, valinit=-10, valstep=0.1)

ax_slider_y_max = plt.axes([0.1, 0.32, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_y_max = Slider(ax_slider_y_max, 'y max', 0.0, 20.0, valinit=10, valstep=0.1)

# Attach the update function to sliders
slider_a.on_changed(update)
slider_b.on_changed(update)
slider_c.on_changed(update)
slider_x_min.on_changed(update)
slider_x_max.on_changed(update)
slider_y_min.on_changed(update)
slider_y_max.on_changed(update)

# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Define the general equation for the graph
def update(val):
    # Get the current values of the sliders
    a = slider_a.val
    b = slider_b.val
    c = slider_c.val
    d = slider_d.val

    # Define the x range for plotting
    x_min = slider_x_min.val
    x_max = slider_x_max.val
    x = np.linspace(x_min, x_max, 1000)

    # Define the general equation (can be modified)
    y = a * np.sin(b * x + c) + d  # Example equation: y = a*sin(b*x + c) + d

    # Update the line data and plot
    line.set_xdata(x)
    line.set_ydata(y)

    # Update the axes limits dynamically
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([min(y) - 1, max(y) + 1])

    fig.canvas.draw_idle()  # Refresh the plot

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.35)  # Adjust space for sliders

# Define the initial x and y range
x_init = np.linspace(-10, 10, 1000)
y_init = np.sin(x_init)  # Initial y values (y = sin(x))

# Plot the initial graph
line, = ax.plot(x_init, y_init, label="Graph", color="blue")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Interactive Graph Plotter with Adjustable Sliders')
ax.grid(True)
ax.axhline(0, color='black',linewidth=1)
ax.axvline(0, color='black',linewidth=1)
ax.legend()

# Create sliders for 'a', 'b', 'c', 'd' (coefficients for the equation)
ax_slider_a = plt.axes([0.1, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_a = Slider(ax_slider_a, 'a', -10.0, 10.0, valinit=1, valstep=0.1)

ax_slider_b = plt.axes([0.1, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_b = Slider(ax_slider_b, 'b', -10.0, 10.0, valinit=1, valstep=0.1)

ax_slider_c = plt.axes([0.1, 0.11, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_c = Slider(ax_slider_c, 'c', -10000.0, 10.0, valinit=0, valstep=0.1)

ax_slider_d = plt.axes([0.1, 0.16, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_d = Slider(ax_slider_d, 'd', -10.0, 10.0, valinit=0, valstep=0.1)

# Create sliders for adjusting the x-range
ax_slider_x_min = plt.axes([0.1, 0.21, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_x_min = Slider(ax_slider_x_min, 'x min', -20.0, 0.0, valinit=-10, valstep=0.1)

ax_slider_x_max = plt.axes([0.1, 0.26, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_x_max = Slider(ax_slider_x_max, 'x max', 0.0, 20.0, valinit=10, valstep=0.1)

# Attach the update function to sliders
slider_a.on_changed(update)
slider_b.on_changed(update)
slider_c.on_changed(update)
slider_d.on_changed(update)
slider_x_min.on_changed(update)
slider_x_max.on_changed(update)

# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Define the general equation for the graph
def update(val):
    # Get the current values of the sliders
    a = slider_a.val
    b = slider_b.val
    c = slider_c.val
    d = slider_d.val

    # Define the x range for plotting
    x_min = slider_x_min.val
    x_max = slider_x_max.val
    x = np.linspace(x_min, x_max, 1000)

    # Define the general equation (can be modified)
    y = a * np.sin(b * x + c) + d  # Example equation: y = a*sin(b*x + c) + d

    # Update the line data and plot
    line.set_xdata(x)
    line.set_ydata(y)

    # Update the axes limits dynamically
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([min(y) - 1, max(y) + 1])

    fig.canvas.draw_idle()  # Refresh the plot

def reset(event):
    # Reset sliders to default values
    slider_a.reset()
    slider_b.reset()
    slider_c.reset()
    slider_d.reset()
    slider_x_min.reset()
    slider_x_max.reset()

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.35)  # Adjust space for sliders and button

# Define the initial x and y range
x_init = np.linspace(-10, 10, 1000)
y_init = np.sin(x_init)  # Initial y values (y = sin(x))

# Plot the initial graph
line, = ax.plot(x_init, y_init, label="Graph", color="blue")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Interactive Graph Plotter with Adjustable Sliders and Reset Button')
ax.grid(True)
ax.axhline(0, color='black',linewidth=1)
ax.axvline(0, color='black',linewidth=1)
ax.legend()

# Create sliders for 'a', 'b', 'c', 'd' (coefficients for the equation)
ax_slider_a = plt.axes([0.1, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_a = Slider(ax_slider_a, 'a', -10.0, 10.0, valinit=1, valstep=0.1)

ax_slider_b = plt.axes([0.1, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_b = Slider(ax_slider_b, 'b', -10.0, 10.0, valinit=1, valstep=0.1)

ax_slider_c = plt.axes([0.1, 0.11, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_c = Slider(ax_slider_c, 'c', -10.0, 10.0, valinit=0, valstep=0.1)

ax_slider_d = plt.axes([0.1, 0.16, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_d = Slider(ax_slider_d, 'd', -10.0, 10.0, valinit=0, valstep=0.1)

# Create sliders for adjusting the x-range
ax_slider_x_min = plt.axes([0.1, 0.21, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_x_min = Slider(ax_slider_x_min, 'x min', -20.0, 0.0, valinit=-10, valstep=0.1)

ax_slider_x_max = plt.axes([0.1, 0.26, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_x_max = Slider(ax_slider_x_max, 'x max', 0.0, 20.0, valinit=10, valstep=0.1)

# Create a button for resetting the plot
ax_reset_button = plt.axes([0.8, 0.01, 0.1, 0.05], facecolor='lightgoldenrodyellow')
reset_button = Button(ax_reset_button, 'Reset', color='lightblue', hovercolor='lightgreen')

# Attach the update function to sliders
slider_a.on_changed(update)
slider_b.on_changed(update)
slider_c.on_changed(update)
slider_d.on_changed(update)
slider_x_min.on_changed(update)
slider_x_max.on_changed(update)

# Attach the reset function to the reset button
reset_button.on_clicked(reset)

# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Define the general equation for the graph (this is an example equation)
def update(val):
    # Get the current values of the sliders
    a = slider_a.val
    b = slider_b.val
    c = slider_c.val
    d = slider_d.val

    # Define the x range for plotting
    x_min = slider_x_min.val
    x_max = slider_x_max.val
    x = np.linspace(x_min, x_max, 1000)

    # Define the general equation (you can replace this with any equation)
    y = a * np.sin(b * x + c) + d  # Example: y = a * sin(b * x + c) + d

    # Update the line data and plot
    line.set_xdata(x)
    line.set_ydata(y)

    # Update the axes limits dynamically
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([min(y) - 1, max(y) + 1])

    fig.canvas.draw_idle()  # Refresh the plot

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.35)  # Adjust space for sliders

# Define the initial x and y range
x_init = np.linspace(-10, 10, 1000)
y_init = np.sin(x_init)  # Initial y values (example y = sin(x))

# Plot the initial graph
line, = ax.plot(x_init, y_init, label="Graph", color="blue")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Interactive Graph Plotter with Adjustable Sliders')
ax.grid(True)
ax.axhline(0, color='black',linewidth=1)
ax.axvline(0, color='black',linewidth=1)
ax.legend()

# Create sliders for 'a', 'b', 'c', 'd' (coefficients for the equation)
ax_slider_a = plt.axes([0.1, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_a = Slider(ax_slider_a, 'a', -10.0, 10.0, valinit=1, valstep=0.1)

ax_slider_b = plt.axes([0.1, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_b = Slider(ax_slider_b, 'b', -10.0, 10.0, valinit=1, valstep=0.1)

ax_slider_c = plt.axes([0.1, 0.11, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_c = Slider(ax_slider_c, 'c', -10.0, 10.0, valinit=0, valstep=0.1)

ax_slider_d = plt.axes([0.1, 0.16, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_d = Slider(ax_slider_d, 'd', -10.0, 10.0, valinit=0, valstep=0.1)

# Create sliders for adjusting the x-range
ax_slider_x_min = plt.axes([0.1, 0.21, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_x_min = Slider(ax_slider_x_min, 'x min', -20.0, 0.0, valinit=-10, valstep=0.1)

ax_slider_x_max = plt.axes([0.1, 0.26, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_x_max = Slider(ax_slider_x_max, 'x max', 0.0, 20.0, valinit=10, valstep=0.1)

# Attach the update function to sliders
slider_a.on_changed(update)
slider_b.on_changed(update)
slider_c.on_changed(update)
slider_d.on_changed(update)
slider_x_min.on_changed(update)
slider_x_max.on_changed(update)

# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Function to update the plot when slider values change
def update(val):
    # Get values of sliders
    a = slider_a.val
    b = slider_b.val
    c = slider_c.val
    d = slider_d.val

    # Define the range of x values
    x_min = slider_x_min.val
    x_max = slider_x_max.val
    x = np.linspace(x_min, x_max, 1000)

    # General equation: y = a * sin(b * x + c) + d (this can be modified for other equations)
    y = a * np.sin(b * x + c) + d  # Example equation: sine wave with adjustable parameters

    # Update the line data and the plot
    line.set_xdata(x)
    line.set_ydata(y)

    # Adjust the axis limits based on the y-values
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([min(y) - 2, max(y) + 2])

    # Redraw the plot
    fig.canvas.draw_idle()

# Create the figure and axis for the plot
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.35)  # Add space at the bottom for the sliders

# Initial range for x and y
x_init = np.linspace(-10, 10, 1000)
y_init = np.sin(x_init)  # Initial y values for the sine function

# Plot the initial graph
line, = ax.plot(x_init, y_init, label="Graph", color="blue")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Interactive Graph Plotter with Adjustable Sliders')
ax.grid(True)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.legend()

# Define sliders for 'a', 'b', 'c', 'd' (coefficients for the equation)
ax_slider_a = plt.axes([0.1, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_a = Slider(ax_slider_a, 'a', -10.0, 10.0, valinit=1, valstep=0.1)

ax_slider_b = plt.axes([0.1, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_b = Slider(ax_slider_b, 'b', -10.0, 10.0, valinit=1, valstep=0.1)

ax_slider_c = plt.axes([0.1, 0.11, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_c = Slider(ax_slider_c, 'c', -10.0, 10.0, valinit=0, valstep=0.1)

ax_slider_d = plt.axes([0.1, 0.16, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_d = Slider(ax_slider_d, 'd', -10.0, 10.0, valinit=0, valstep=0.1)

# Create sliders for adjusting the x-range
ax_slider_x_min = plt.axes([0.1, 0.21, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_x_min = Slider(ax_slider_x_min, 'x min', -20.0, 0.0, valinit=-10, valstep=0.1)

ax_slider_x_max = plt.axes([0.1, 0.26, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_x_max = Slider(ax_slider_x_max, 'x max', 0.0, 20.0, valinit=10, valstep=0.1)

# Attach the update function to sliders
slider_a.on_changed(update)
slider_b.on_changed(update)
slider_c.on_changed(update)
slider_d.on_changed(update)
slider_x_min.on_changed(update)
slider_x_max.on_changed(update)

# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,TextBox
import sympy as sp

# Function to update the plot when sliders change
def update(val):
    # Get the current values of the sliders
    a = slider_a.val
    b = slider_b.val
    c = slider_c.val
    d = slider_d.val

    # Define the range of x values based on slider inputs
    x_min = slider_x_min.val
    x_max = slider_x_max.val
    x = np.linspace(x_min, x_max, 1000)

    # Generate the function's y values dynamically using the parameters
    y = eval(equation_string)  # Evaluate the user-provided equation string

    # Update the line data and the plot
    line.set_xdata(x)
    line.set_ydata(y)

    # Update the axis limits
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([min(y) - 2, max(y) + 2])

    # Redraw the plot
    fig.canvas.draw_idle()

# Function to update the equation string from user input
def update_equation(val):
    global equation_string
    equation_string = eq_input.val  # Get equation input from user
    update(0)  # Call update to refresh the plot

# Create the figure and axis for the plot
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.4)  # Adjust the space at the bottom for the sliders

# Initial range for x and y
x_init = np.linspace(-10, 10, 1000)
y_init = np.sin(x_init)  # Initial y values for the sine function

# Plot the initial graph
line, = ax.plot(x_init, y_init, label="Graph", color="blue")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Interactive Graph Plotter with Adjustable Sliders')
ax.grid(True)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.legend()

# Slider setup for parameters a, b, c, d (coefficients of the equation)
ax_slider_a = plt.axes([0.1, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_a = Slider(ax_slider_a, 'a', -10.0, 10.0, valinit=1, valstep=0.1)

ax_slider_b = plt.axes([0.1, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_b = Slider(ax_slider_b, 'b', -10.0, 10.0, valinit=1, valstep=0.1)

ax_slider_c = plt.axes([0.1, 0.11, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_c = Slider(ax_slider_c, 'c', -10.0, 10.0, valinit=0, valstep=0.1)

ax_slider_d = plt.axes([0.1, 0.16, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_d = Slider(ax_slider_d, 'd', -10.0, 10.0, valinit=0, valstep=0.1)

# Slider setup for adjusting the x-range
ax_slider_x_min = plt.axes([0.1, 0.21, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_x_min = Slider(ax_slider_x_min, 'x min', -20.0, 0.0, valinit=-10, valstep=0.1)

ax_slider_x_max = plt.axes([0.1, 0.26, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_x_max = Slider(ax_slider_x_max, 'x max', 0.0, 20.0, valinit=10, valstep=0.1)

# Input box for user-defined equation
ax_eq_input = plt.axes([0.1, 0.31, 0.65, 0.04], facecolor='lightgoldenrodyellow')
eq_input = TextBox(ax_eq_input, 'Enter equation (in terms of a, b, c, d):', initial='a*np.sin(b*x + c) + d') # Use TextBox directly


# Update the equation string when the user changes the equation
eq_input.on_submit(update_equation)

# Attach the update function to the sliders
slider_a.on_changed(update)
slider_b.on_changed(update)
slider_c.on_changed(update)
slider_d.on_changed(update)
slider_x_min.on_changed(update)
slider_x_max.on_changed(update)

# Initialize the equation string with a default equation
equation_string = 'a * np.sin(b * x + c) + d'

# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import simpledialog
import sympy as sp

# Function to evaluate the user's input equation
def eval_equation(x, a, b, c, d):
    try:
        # The equation is in the format of a string (using numpy functions)
        return eval(equation_string)
    except Exception as e:
        return np.zeros_like(x)

# Update the graph when a slider is changed
def update_graph(val):
    a = slider_a.get()
    b = slider_b.get()
    c = slider_c.get()
    d = slider_d.get()
    x_min = slider_x_min.get()
    x_max = slider_x_max.get()

    x = np.linspace(x_min, x_max, 1000)
    y = eval_equation(x, a, b, c, d)

    # Update the plot
    ax.clear()  # Clear the previous plot
    ax.plot(x, y, label="Graph", color="blue")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Interactive Graph Plotter')
    ax.grid(True)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.legend()

    # Redraw the plot
    canvas.draw()

# Function to update the equation string
def update_equation_string():
    global equation_string
    equation_string = eq_input.get()
    update_graph(None)  # Update the graph immediately

# Create main window
root = tk.Tk()
root.title("Interactive Graph Plotter")

# Equation input field
eq_input_label = tk.Label(root, text="Enter the equation (use a, b, c, d as variables):")
eq_input_label.pack()

eq_input = tk.Entry(root, width=50)
eq_input.insert(0, "a*np.sin(b*x + c) + d")  # Default equation
eq_input.pack()

eq_button = tk.Button(root, text="Update Equation", command=update_equation_string)
eq_button.pack()

# Sliders for parameters a, b, c, d
slider_a = tk.Scale(root, from_=-10, to=10, resolution=0.1, orient='horizontal', label='a')
slider_a.set(1)
slider_a.pack()

slider_b = tk.Scale(root, from_=-10, to=10, resolution=0.1, orient='horizontal', label='b')
slider_b.set(1)
slider_b.pack()

slider_c = tk.Scale(root, from_=-10, to=10, resolution=0.1, orient='horizontal', label='c')
slider_c.set(0)
slider_c.pack()

slider_d = tk.Scale(root, from_=-10, to=10, resolution=0.1, orient='horizontal', label='d')
slider_d.set(0)
slider_d.pack()

# Sliders for adjusting x range
slider_x_min = tk.Scale(root, from_=-20, to=0, resolution=0.1, orient='horizontal', label='x min')
slider_x_min.set(-10)
slider_x_min.pack()

slider_x_max = tk.Scale(root, from_=0, to=20, resolution=0.1, orient='horizontal', label='x max')
slider_x_max.set(10)
slider_x_max.pack()

# Button to update the graph
update_button = tk.Button(root, text="Update Graph", command=lambda: update_graph(None))
update_button.pack()

# Initializing the plot with Matplotlib
fig, ax = plt.subplots(figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, master=root)  # Creating a canvas for matplotlib
canvas.get_tk_widget().pack()

# Default equation string (to be changed by user)
equation_string = "a*np.sin(b*x + c) + d"  # Default function for plotting

# Run the application
root.mainloop()