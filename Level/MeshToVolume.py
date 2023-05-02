#
# Unreal 5.0 convert static mesh to volume for Wwise AkSpatialAudioVolume placement
#

import unreal

unreal.log("Generating...")

# Generated volume type
volume = unreal.BlockingVolume

# Get selected actors and current world
selected_actors = unreal.EditorActorSubsystem().get_selected_level_actors()
world = unreal.UnrealEditorSubsystem().get_editor_world()

# create dynamic mesh pool and setting up options
dynamic_mesh_pool = unreal.GeometryScript_SceneUtils().create_dynamic_mesh_pool()
asset_opt = unreal.GeometryScriptCopyMeshFromAssetOptions()
dm_lod = unreal.GeometryScriptMeshWriteLOD()
vol_opt = unreal.GeometryScriptCreateNewVolumeFromMeshOptions(volume, False, 250)

# Converting all of the selected actors
for actor in selected_actors:
    asset = actor.get_component_by_class(unreal.StaticMeshComponent).static_mesh
    
    # needs cleaning up
    if asset is None:
        unreal.log_warning(actor.get_actor_lable() + "has no Static mesh component!")
        continue

    # get variables
    transform = actor.get_actor_transform()
    name = "AKS_" + actor.get_actor_label()

    # get dynamic mesh and populate with static mesh data
    dm = unreal.DynamicMeshPool().request_mesh()  # dynamic mesh
    unreal.GeometryScript_AssetUtils.copy_mesh_from_static_mesh(
        asset, dm, asset_opt, unreal.GeometryScriptMeshReadLOD()
    )

    # convert to volume
    unreal.GeometryScript_NewAssetUtils.create_new_volume_from_mesh(dm, world, transform, name, vol_opt)

    # return mesh to pool
    unreal.DynamicMeshPool.return_mesh(dynamic_mesh_pool, dm)
