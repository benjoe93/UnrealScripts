import unreal

# instances
@unreal.uclass()
class Global(unreal.GlobalEditorUtilityBase):
    pass

sys_lib = unreal.SystemLibrary()

# variables
selected_actors = Global().get_selection_set()
align_to = selected_actors[0].get_actor_location().z
i = 0

# begin Undo recording
sys_lib.begin_transaction("Py_util", "Align Z", None)

# loop through actors
for actor in selected_actors:
    # update undo
    sys_lib.transact_object(actor)
    
    current_loc = actor.get_actor_location()
    new_loc = (current_loc.x, current_loc.y, align_to)
    actor.set_actor_location(new_loc, False, False)
    i += i

# close undo
sys_lib.end_transaction()
unreal.log("{} actors aligned!".format(i))
