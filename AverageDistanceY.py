import unreal

@unreal.uclass()
class Global(unreal.GlobalEditorUtilityBase):
    pass

# variables
selected_actors = Global().get_selection_set()

min = 0
max = 0
i = 0

# logic
# find min and max position 
for actor in selected_actors:
    actor_loc = actor.get_actor_location().y
    if actor_loc < min:
        min = actor_loc

    if actor_loc > max:
        max = actor_loc

dist = abs(min-max)/(len(selected_actors)-1)

# move actors
for actor in selected_actors:
    current_loc = actor.get_actor_location()
    new_loc_y = min+(dist*i)
    
    new_loc = (current_loc.x, new_loc_y, current_loc.z)
    actor.set_actor_location(new_loc, False, False)
    i += 1
