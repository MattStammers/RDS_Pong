import arcade

# Define the screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "RDS Pong"

# Define the ball properties
BALL_RADIUS = 32
BALL_X_SPEED = 7
BALL_Y_SPEED = 5

# Define the player properties
PLAYER_WIDTH = 10
PLAYER_HEIGHT = 64
PLAYER_SPEED = 10

# Define the score properties
SCORE_SIZE = 50
SCORE_X = SCREEN_WIDTH / 2
SCORE_Y = SCREEN_HEIGHT - SCORE_SIZE

# Define the game class
class Pong(arcade.Window):
  def __init__(self, width, height, title):
    super().__init__(width, height, title)

    # Initialize the ball
    self.ball = arcade.Sprite("resources/shiba_inu_ball.png", center_x=SCREEN_WIDTH / 2, center_y=SCREEN_HEIGHT / 2)

    # Initialize the left player
    self.left_player = arcade.Sprite("resources/left_player_paddle.png", center_x=0, center_y=SCREEN_HEIGHT / 2)

    # Initialize the right player
    self.right_player = arcade.Sprite("resources/right_player_paddle.png", center_x=SCREEN_WIDTH, center_y=SCREEN_HEIGHT / 2)

    # Initialize the game state
    self.ball_x_speed = BALL_X_SPEED
    self.ball_y_speed = BALL_Y_SPEED
    self.left_score = 0
    self.right_score = 0
    self.game_over = False
    self.up_pressed = False
    self.down_pressed = False
    self.w_pressed = False
    self.s_pressed = False
    self.text_angle = 0
    self.time_elapsed = 0
    self.background_color = arcade.color.BLUE

  def on_key_press(self, key, key_modifiers):
    # Handle the player movement keys
    if key == arcade.key.UP:
        self.up_pressed = True
    elif key == arcade.key.DOWN:
        self.down_pressed = True
    elif key == arcade.key.W:
        self.w_pressed = True
    elif key == arcade.key.S:
        self.s_pressed = True

  def on_key_release(self, key, key_modifiers):
    # Handle the player movement keys
    if key == arcade.key.UP:
        self.up_pressed = False
    elif key == arcade.key.DOWN:
        self.down_pressed = False
    elif key == arcade.key.W:
        self.w_pressed = False
    elif key == arcade.key.S:
        self.s_pressed = False      

  def on_update(self, delta_time):
    if self.game_over:
        return

  # Move the ball
    self.ball.center_x += self.ball_x_speed
    self.ball.center_y += self.ball_y_speed

  # Check for screen boundaries
    if self.ball.center_y > SCREEN_HEIGHT - BALL_RADIUS or self.ball.center_y < BALL_RADIUS:
      self.ball_y_speed *= -1
    elif self.ball.center_x < 0:
      self.right_score += 1
      self.ball_x_speed = BALL_X_SPEED
      self.ball_y_speed = BALL_Y_SPEED
      self.reset_game()

    elif self.ball.center_x > SCREEN_WIDTH:
      self.left_score += 1
      self.ball_x_speed = -BALL_X_SPEED
      self.ball_y_speed = -BALL_Y_SPEED
      self.reset_game()

  # Check for collision with the paddles
    if (self.ball.center_x - BALL_RADIUS <= PLAYER_WIDTH and
      abs(self.ball.center_y - self.left_player.center_y) < PLAYER_HEIGHT / 2):
      self.ball_x_speed = abs(self.ball_x_speed)

    if (self.ball.center_x + BALL_RADIUS >= SCREEN_WIDTH - PLAYER_WIDTH and
      abs(self.ball.center_y - self.right_player.center_y) < PLAYER_HEIGHT / 2):
      self.ball_x_speed = -abs(self.ball_x_speed)

    # Move the paddles
    if self.up_pressed:
      self.left_player.center_y += PLAYER_SPEED
    if self.down_pressed:
      self.left_player.center_y -= PLAYER_SPEED

    if self.w_pressed:
      self.right_player.center_y += PLAYER_SPEED
    if self.s_pressed:
      self.right_player.center_y -= PLAYER_SPEED

  # Check for paddle boundaries
    if self.left_player.center_y > SCREEN_HEIGHT - PLAYER_HEIGHT / 2:
      self.left_player.center_y = SCREEN_HEIGHT - PLAYER_HEIGHT / 2
    elif self.left_player.center_y < PLAYER_HEIGHT / 2:
      self.left_player.center_y = PLAYER_HEIGHT / 2

    if self.right_player.center_y > SCREEN_HEIGHT - PLAYER_HEIGHT / 2:
      self.right_player.center_y = SCREEN_HEIGHT - PLAYER_HEIGHT / 2
    elif self.right_player.center_y < PLAYER_HEIGHT / 2:
      self.right_player.center_y = PLAYER_HEIGHT / 2

     # movement with
    if self.up_pressed and self.left_player.center_y < SCREEN_HEIGHT - PLAYER_HEIGHT / 2:
      self.left_player.center_y += PLAYER_SPEED

    if self.down_pressed and self.left_player.center_y > PLAYER_HEIGHT / 2:
      self.left_player.center_y -= PLAYER_SPEED

    if self.w_pressed and self.right_player.center_y < SCREEN_HEIGHT - PLAYER_HEIGHT / 2:
      self.right_player.center_y += PLAYER_SPEED

    if self.s_pressed and self.right_player.center_y > PLAYER_HEIGHT / 2:
      self.right_player.center_y -= PLAYER_SPEED

    self.text_angle += 1
    self.time_elapsed += delta_time

  def reset_game(self):
    self.ball.center_x = SCREEN_WIDTH / 2
    self.ball.center_y = SCREEN_HEIGHT / 2

  # Check if the game is over
    if self.left_score >= 10 or self.right_score >= 10:
      self.game_over = True

  def on_draw(self):
    arcade.start_render()

    # Draw the ball
    self.ball.draw()

    # Draw the players
    self.left_player.draw()
    self.right_player.draw()

    # Draw the scores
    arcade.draw_text(f"{self.left_score}", SCORE_X - SCORE_SIZE, SCORE_Y, arcade.color.WHITE, SCORE_SIZE)
    arcade.draw_text(f"{self.right_score}", SCORE_X + SCORE_SIZE, SCORE_Y, arcade.color.WHITE, SCORE_SIZE)

    # Graffiti
    start_x = 500
    start_y = 250
    arcade.draw_point(start_x, start_y, arcade.color.GREEN, 5)
    arcade.draw_text("Cai, Michael, Ashley, Tom, Florina, Matt and Ben are Legends",
                         start_x, start_y,
                         arcade.color.BARN_RED,
                         30,
                         anchor_x="center",
                         anchor_y="center",
                         rotation=self.text_angle)

    if self.game_over:
      arcade.draw_text("Game Over!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.WHITE, 36)

if __name__ == "__main__":
  game = Pong(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
  arcade.run()
