import unreal

# instances
@unreal.uclass()
class Global(unreal.GlobalEditorUtilityBase):
    pass

sys_lib = unreal.SystemLibrary()

# varables
selected_actors = Global().get_selection_set()
min = selected_actors[0].get_actor_location().x
max = selected_actors[-1].get_actor_location().x
dist = abs(min-max)/(len(selected_actors)-1)
i = 0

# begin Undo recording
sys_lib.begin_transaction("Py_util", "Distribute X", None)

# loop through actors
for i in range(1, (len(selected_actors)-1)):
    # update undo
    sys_lib.transact_object(selected_actors[i])
    
    current_loc = selected_actors[i].get_actor_location()
    #check the direction of movement
    if min < max:
        new_loc_x= min+(dist*i)
    else:
        new_loc_x= min-(dist*i)
    new_loc = (new_loc_x, current_loc.y, current_loc.z)
    
    selected_actors[i].set_actor_location(new_loc, False, False)
    unreal.log(selected_actors[i].get_fname())

# close undo
sys_lib.end_transaction()
