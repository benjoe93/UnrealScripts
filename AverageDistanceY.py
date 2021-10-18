import unreal

@unreal.uclass()
class Global(unreal.GlobalEditorUtilityBase):
    pass

selected_actors = Global().get_selection_set()

min = selected_actors[0].get_actor_location().y
max = selected_actors[-1].get_actor_location().y
i = 0

dist = abs(min-max)/(len(selected_actors)-1)

for i in range(1, (len(selected_actors)-1)):
    current_loc = selected_actors[i].get_actor_location()
    new_loc_y= min+(dist*i)
    new_loc = (current_loc.x, new_loc_y, current_loc.z)
    
    selected_actors[i].set_actor_location(new_loc, False, False)
    unreal.log(selected_actors[i].get_fname())
