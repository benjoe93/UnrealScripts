import unreal

# instances of unreal classes
editor_lvl_lib = unreal.EditorLevelLibrary()
editor_filter_lib = unreal.EditorFilterLibrary()

# get all the actor and filter to specific elements
actors = editor_lvl_lib.get_all_level_actors()

static_meshes = editor_filter_lib.by_class( actors, unreal.StaticMeshActor )
reflection_cap = editor_filter_lib.by_class( actors, unreal.ReflectionCapture )
lightmass_imp_vol = editor_filter_lib.by_class( actors, unreal.LightmassImportanceVolume )
postprocess_vol = editor_filter_lib.by_class( actors, unreal.PostProcessVolume )
blocking_vol = editor_filter_lib.by_class( actors, unreal.BlockingVolume )
cine_camera = editor_filter_lib.by_class( actors, unreal.CineCameraActor )
lightmass_portal = editor_filter_lib.by_class( actors, unreal.LightmassPortal )
ds_scene = editor_filter_lib.by_class( actors, unreal.DatasmithSceneActor )
player_start = editor_filter_lib.by_class( actors, unreal.PlayerStart )

point_light = editor_filter_lib.by_class( actors, unreal.PointLight )
spot_light = editor_filter_lib.by_class( actors, unreal.SpotLight )
rect_light = editor_filter_lib.by_class( actors, unreal.RectLight )
directional_light = editor_filter_lib.by_class( actors, unreal.DirectionalLight )
atmospheric_fog = editor_filter_lib.by_class( actors, unreal.AtmosphericFog )
height_fog = editor_filter_lib.by_class( actors, unreal.ExponentialHeightFog )
sky = editor_filter_lib.by_actor_label( actors, "sky" )

blueprints = editor_filter_lib.by_actor_label( actors, "BP_" )
bp_interactable = editor_filter_lib.by_actor_label( actors, "BP_InteractablePoint" )
bp_ip = editor_filter_lib.by_actor_label( actors, "BP_IP_" )
bp_teleport = editor_filter_lib.by_actor_label( actors, "BP_Teleport_" )
bp_tp = editor_filter_lib.by_actor_label( actors, "BP_TP_" )
bp_hotspot = editor_filter_lib.by_actor_label( actors, "BP_HotSpot" )
bp_h = editor_filter_lib.by_actor_label( actors, "BP_H_" )

moved = 0

# create mapping between folder names and arrays
mapping = {
    "Meshes" : static_meshes,
    "ReflectionCaptures" : reflection_cap,
    "Blueprints" : blueprints,
    "Blueprints/Configs" : bp_ip,
    "Blueprints/Configs" : bp_interactable,
    "Blueprints/Teleports" : bp_teleport,
    "Blueprints/Teleports" : bp_tp,
    "Blueprints/Hotspots" : bp_h,
    "Blueprints/Hotspots" : bp_hotspot,
    "Cameras" : cine_camera,
    "Datasmith" : ds_scene,
    "Gameplay": player_start,
    "PP" : postprocess_vol,
    "Volumes/BlockingVolumes" : blocking_vol,
    "Volumes/LightMassImportance" : lightmass_imp_vol,
    "Lights/LightmassPostal" : lightmass_portal,
    "Lights/Point" : point_light,
    "Lights/Spot" : spot_light,
    "Lights/Rect" : rect_light,
    "Lights/_Exterior" : directional_light,
    "Lights/_Exterior" : atmospheric_fog,
    "Lights/_Exterior" : height_fog,
    "Lights/_Exterior" : sky,
    }

for folder_name in mapping:
    # for every list of actors, set new folder path
    for actor in mapping[folder_name]:
        actor_name = actor.get_fname()
        actor.set_folder_path(folder_name)
        unreal.log("Moved {} into {}".format(actor_name, folder_name))
        
        moved += 1

unreal.log("Moved {} actors into respective folders".format(moved))