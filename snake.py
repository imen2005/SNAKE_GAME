from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]


class Snake(Turtle):
    
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
            
    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.segments[-1].position())
        
        
        
    
    def move(self):
        for seg_num in range(len(self.segments) - 1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x,y=new_y)
        self.segments[0].forward(20)
        
        
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
    
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
            
    
        