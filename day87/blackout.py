import tkinter as tk

import random



class BreakoutGame:

    def __init__(self, root):

        self.root = root

        self.root.title("Breakout Game")

        self.canvas = tk.Canvas(root, width=500, height=400, bg="black")

        self.canvas.pack()



        self.paddle = self.canvas.create_rectangle(200, 370, 300, 380, fill="white")

        self.ball = self.canvas.create_oval(245, 245, 255, 255, fill="red")



        self.bricks = []

        self.create_bricks()



        self.ball_dx = 3

        self.ball_dy = -3

        self.lives = 3

        self.game_running = True



        self.root.bind("<Left>", self.move_left)

        self.root.bind("<Right>", self.move_right)



        self.animate()



    def create_bricks(self):

        colors = ["red", "orange", "green", "yellow"]

        for i in range(4):

            for j in range(10):

                x1 = j * 50

                y1 = i * 20

                x2 = x1 + 48

                y2 = y1 + 18

                brick = self.canvas.create_rectangle(x1, y1, x2, y2, fill=colors[i], outline="black")

                self.bricks.append(brick)



    def move_left(self, event):

        if self.canvas.coords(self.paddle)[0] > 0:

            self.canvas.move(self.paddle, -20, 0)



    def move_right(self, event):

        if self.canvas.coords(self.paddle)[2] < 500:

            self.canvas.move(self.paddle, 20, 0)



    def animate(self):

        if not self.game_running:

            return



        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)

        ball_coords = self.canvas.coords(self.ball)

        paddle_coords = self.canvas.coords(self.paddle)



        # Wall collision

        if ball_coords[0] <= 0 or ball_coords[2] >= 500:

            self.ball_dx *= -1

        if ball_coords[1] <= 0:

            self.ball_dy *= -1

        if ball_coords[3] >= 400:

            self.lives -= 1

            if self.lives == 0:

                self.game_over("Game Over ?")

                return

            else:

                self.canvas.coords(self.ball, 245, 245, 255, 255)

                self.ball_dy *= -1



        # Paddle collision

        if (paddle_coords[1] <= ball_coords[3] <= paddle_coords[3] and

            paddle_coords[0] <= ball_coords[2] and

            paddle_coords[2] >= ball_coords[0]):

            self.ball_dy *= -1



        # Brick collision

        hit_brick = None

        for brick in self.bricks:

            if self.canvas.coords(brick):

                if self.check_collision(self.canvas.coords(brick), ball_coords):

                    hit_brick = brick

                    break



        if hit_brick:

            self.canvas.delete(hit_brick)

            self.bricks.remove(hit_brick)

            self.ball_dy *= -1

            if not self.bricks:

                self.game_over("You Win! ?")



        self.root.after(20, self.animate)



    def check_collision(self, rect, ball):

        return not (rect[2] < ball[0] or rect[0] > ball[2] or

                    rect[3] < ball[1] or rect[1] > ball[3])



    def game_over(self, message):

        self.canvas.create_text(250, 200, text=message, fill="white", font=("Arial", 24))

        self.game_running = False



# Run the game

if __name__ == "__main__":

    root = tk.Tk()

    game = BreakoutGame(root)

    root.mainloop()
