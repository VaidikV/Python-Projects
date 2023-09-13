from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # Here position() returns the turtle’s current location. In short we are adding a segment in the end of list.

        self.add_segment(self.segments[-1].position())

    def move(self):
        # In this for loop, the last element of the list "segments" is assigned to the variable seg_num.
        # Range in this for loop: we are accessing the last element of the segments list by subtracting 1 from the
        # length of the list. The stop is 0. The step is -1. The negative sign allows to start from the last element.

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        #   With these lines of code we are instructing the last segment of the snake to follow the second last segment.
        #   Hence how much ever segments you add in the end, they will follow the second last segment.
        #   With the same logic, the second segment will follow the head (1st segment). Conclusion: The basic movement
        #   of a snake is successfully transformed into code.

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Here the if statements prevents the snake to turn around in the same path. Tbc(to be clear), you can't turn up
        # if you are going down. This is just to align with the rules and methods of the original snake game.

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
