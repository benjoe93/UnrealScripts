# Utility scripts for Unreal Engine.
# To use the script you need to call the functions through the command line by their name, the axis the operation is happening, and the amount. If the operation doesn't require amount enter "0".
# e.g.: py "Utility.py" Align x 0

import unreal
import random
import sys

@unreal.uclass()
class Global(unreal.GlobalEditorUtilityBase):
    pass

sys_lib = unreal.SystemLibrary()

# functions
def Align(selected_actors, axis):
    i = 0
    
    # begin Undo recording
    sys_lib.begin_transaction("Py_util", "Align", None)
    
    # loop through actors
    for actor in selected_actors:
        # update undo
        sys_lib.transact_object(actor)
        
        current_loc = actor.get_actor_location()
        if axis == "x":
            align_to = selected_actors[0].get_actor_location().x
            new_loc = (align_to, current_loc.y, current_loc.z)
        elif axis == "y":
            align_to = selected_actors[0].get_actor_location().y
            new_loc = (current_loc.x, align_to, current_loc.z)
        else:
            align_to = selected_actors[0].get_actor_location().z
            new_loc = (current_loc.x, current_loc.y, align_to)
        actor.set_actor_location(new_loc, False, False)
        i += i
    
    # close undo
    sys_lib.end_transaction()
    unreal.log("{} actors aligned!".format(i))

def Distribute(selected_actors, axis):
    # local variables
    i = 0
    if axis == "x":
        min = selected_actors[0].get_actor_location().x
        max = selected_actors[-1].get_actor_location().x
        dist = abs(min-max)/(len(selected_actors)-1)
    elif axis == "y":
        min = selected_actors[0].get_actor_location().y
        max = selected_actors[-1].get_actor_location().y
        dist = abs(min-max)/(len(selected_actors)-1)
    else:
        min = selected_actors[0].get_actor_location().z
        max = selected_actors[-1].get_actor_location().z
        dist = abs(min-max)/(len(selected_actors)-1)
    
    # begin Undo recording
    sys_lib.begin_transaction("Py_util", "Distribute", None)
    
    # loop through actors
    for i in range(1, (len(selected_actors)-1)):
        # update undo
        sys_lib.transact_object(selected_actors[i])
        
        current_loc = selected_actors[i].get_actor_location()
        #check the direction of movement
        if min < max:
            delta_loc= min+(dist*i)
        else:
            delta_loc= min-(dist*i)
        
        if axis == "x":
            new_loc = (delta_loc, current_loc.y, current_loc.z)
        elif axis == "y":
            new_loc = (current_loc.x, delta_loc, current_loc.z)
        else:
            new_loc = (current_loc.x, current_loc.y, delta_loc)
        selected_actors[i].set_actor_location(new_loc, False, False)
    
    # close undo
    sys_lib.end_transaction()

def Rotate(selected_actors, axis, amount):
    # local variables
    i = 0
    
    # begin Undo recording
    sys_lib.begin_transaction("Py_util", "Rotate", None)
    
    # loop through actors
    for i in range(0, (len(selected_actors))):
        # update undo
        sys_lib.transact_object(selected_actors[i])
        
        if axis == "x":
            new_rot = unreal.Rotator(float(amount), 0.0, 0.0)
        elif axis == "y":
            new_rot = unreal.Rotator(0.0, float(amount), 0.0)
        else:
            new_rot = unreal.Rotator(0.0, 0.0, float(amount))
        print(new_rot)
        selected_actors[i].add_actor_local_rotation(new_rot, False, False)
    
    # close undo
    sys_lib.end_transaction()

def RandRotate(selected_actors, axis):
    # local variables
    i = 0
    
    # begin Undo recording
    sys_lib.begin_transaction("Py_util", "RandRotate", None)
    
    # loop through actors
    for i in range(0, (len(selected_actors))):
        # update undo
        sys_lib.transact_object(selected_actors[i])
        rand = random.randrange(-180, 180)
        
        if axis == "x":
            new_rot = unreal.Rotator(float(rand), 0.0, 0.0)
        elif axis == "y":
            new_rot = unreal.Rotator(0.0, float(rand), 0.0)
        else:
            new_rot = unreal.Rotator(0.0, 0.0, float(rand))
        print(new_rot)
        selected_actors[i].add_actor_local_rotation(new_rot, False, False)
    
    # close undo
    sys_lib.end_transaction()

# variables
func = sys.argv[1]                              # gets the function name passed from unreal
axis = sys.argv[2]                              # gets axis name passed from unreal
amount = sys.argv[3]                            # gets number value passed from unreal
selected_actors = Global().get_selection_set()  # gets selected actors

if func == "Align":
    Align(selected_actors, axis)
elif func == "Distribute":
    Distribute(selected_actors, axis)
elif func == "Rotate":
    Rotate(selected_actors, axis, amount)
elif func == "RandRotate":
    RandRotate(selected_actors, axis)