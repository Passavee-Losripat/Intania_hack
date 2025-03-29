extends CharacterBody2D

func _ready():
	var anim = $AnimatedSprite2D
	anim.play("idle")
