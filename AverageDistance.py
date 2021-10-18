import unreal

@unreal.uclass()
class Global(unreal.GlobalEditorUtilityBase):
    pass


#variables
selected_actors = Global().get_selection_set()

#logic
min = 0
max = 0

for actor in selected_actors:
    actor_loc = actor.get_actor_location().y
    if actor_loc < min:
        min = actor_loc

    if actor_loc > max:
        max = actor_loc

dist = max-min
delta_dist = dist/len(selected_actors)

i = 1
for actor in selected_actors:
    current_loc = actor.get_actor_location()
    delta = delta_dist*i
    
    new_loc = (current_loc.x, current_loc.y+delta, current_loc.z)
    actor.set_actor_location(new_loc, False, False)
    i = i+1