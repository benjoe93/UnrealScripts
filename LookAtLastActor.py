import unreal

#instance libraries
lvl_lib = unreal.EditorLevelLibrary()
actor_util = unreal.Actor()
math_lib = unreal.MathLibrary()
sys_lib = unreal.SystemLibrary()

#variables
selected_actors = lvl_lib.get_selected_level_actors()
target_actor = selected_actors[-1]

# begin Undo recording
sys_lib.begin_transaction("Py_util", "Look at last selected actor", None)

# logic
for actor in selected_actors:
    # update undo
    sys_lib.transact_object(actor)
    
    target_pos = target_actor.get_actor_location()
    actor_pos = actor.get_actor_location()
    look_at_rot = math_lib.find_look_at_rotation(actor_pos, target_pos)
    actor.set_actor_rotation(look_at_rot, False)
    
# close undo
sys_lib.end_transaction()
