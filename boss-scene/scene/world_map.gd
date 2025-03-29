extends Node2D


func _on_mon_transition_point_body_entered(body: Node2D) -> void:
	if body.has_method("slimeRPG"):
		global.transition_scene = true



func _on_mon_transition_point_body_exited(body: Node2D) -> void:
	if body.has_method("slimeRPG"):
		global.transition_scene = false
		
		
func change_scene():
	if global.transition_scene == true:
		if global.current_scene == "world":
			get_tree().change_scene_to_file()
