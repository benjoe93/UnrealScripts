import unreal

# instance unreal library
editor_util = unreal.EditorUtilityLibrary()
string_lib = unreal.StringLibrary()

# selected asset
selected_assets = editor_util.get_selected_assets()
chaged = 0
naming = ["_MRA", "_RMA", "_R","roughness", "_M", "_mask"]

#loop through selected assets
for asset in selected_assets:
    if string_lib.contains(asset, naming, False):
        unreal.log(asset.get_name())