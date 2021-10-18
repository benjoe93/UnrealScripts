import unreal

@unreal.uclass()
class Global(unreal.GlobalEditorUtilityBase):
    pass

selected_actors = Global().get_selection_set()

align_to = selected_actors[0].get_actor_location().z
i = 0

for actor in selected_actors:
    current_loc = actor.get_actor_location()
    new_loc = (current_loc.x, current_loc.y, align_to)
    
    actor.set_actor_location(new_loc, False, False)
    i += i
    unreal.log("{} actors aligned!".format(i))