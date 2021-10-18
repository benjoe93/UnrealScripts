import unreal

# instance classes
editor_util_lib = unreal.EditorUtilityLibrary()

# variables
selected_assets = editor_util_lib.get_selected_assets()
changed = 0

# change the RGBCurve value to 1
for asset in selected_assets:
    try:
        if asset.get_editor_property("AdjustRGBCurve") != 1.0:
            name = asset.get_name()
            asset.set_editor_property("AdjustRGBCurve", 1.0)   
            changed += 1
    except:
        unreal.log_error("{} is not a Texture2D file".format(asset.get_fname()))
        continue

unreal.log_warning("{} object has been updated!".format(changed))