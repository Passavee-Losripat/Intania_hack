extends CharacterBody2D

const SPEED = 200
const JUMP_VELOCITY = -400
const GRAVITY = 900

func _physics_process(delta):
	var input_vector = Vector2.ZERO

	# Horizontal movement
	if Input.is_action_pressed("ui_right"):
		input_vector.x += 1
	if Input.is_action_pressed("ui_left"):
		input_vector.x -= 1

	# Apply gravity
	if not is_on_floor():
		velocity.y += GRAVITY * delta
	else:
		# Jump
		if Input.is_action_just_pressed("ui_accept"):  # default is spacebar or Z
			velocity.y = JUMP_VELOCITY

	# Apply horizontal velocity
	velocity.x = input_vector.x * SPEED

	move_and_slide()
