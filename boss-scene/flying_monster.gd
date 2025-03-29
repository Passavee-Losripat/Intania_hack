extends CharacterBody2D

var speed: float = 100

func _ready():
	input_pickable = true
	velocity = _random_up_direction() * speed
	
func _random_up_direction():
	var x = deg_to_rad(randf_range(0, 180))
	return Vector2(cos(x), sin(x)).normalized()
	
func _physics_process(delta):
	var col = move_and_collide(velocity * delta)
	
	if col:
		velocity = velocity.bounce(col.get_normal())
		
	#_check_direction()
	#
#func _check_direction():
	#if velocity.x < 0:
		#sprite.flip_h = true
	#else:
		#sprite.flip_h = false
		
func _on_input_event(viewport, event, shape_idx):
	if event.is_action_pressed("shoot"):
		print("Shoot!")
		queue_free()
