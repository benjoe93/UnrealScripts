import unreal

# instaces
@unreal.uclass()
class Global(unreal.GlobalEditorUtilityBase):
    pass

sys_lib = unreal.SystemLibrary()

# variables
selected_actors = Global().get_selection_set()
min = selected_actors[0].get_actor_location().z
max = selected_actors[-1].get_actor_location().z
dist = abs(min-max)/(len(selected_actors)-1)
i = 0

# begin Undo recording
sys_lib.begin_transaction("Py_util", "Distribute Z", None)

# loop through actors
for i in range(1, (len(selected_actors)-1)):
    # update undo
    sys_lib.transact_object(selected_actors[i])
    
    current_loc = selected_actors[i].get_actor_location()
    #check the direction of movement
    if min < max:
        new_loc_z= min+(dist*i)
    else:
        new_loc_z= min-(dist*i)
    new_loc = (current_loc.x, current_loc.y, new_loc_z)
    
    selected_actors[i].set_actor_location(new_loc, False, False)
    unreal.log(selected_actors[i].get_fname())

# close undo
sys_lib.end_transaction()
