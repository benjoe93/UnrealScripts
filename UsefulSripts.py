import unreal

def SetStaticMeshLodGroup ():
    
    allStaticMesh = unreal.AssetRegistry.get_assets_by_class('StaticMesh')
    
    for mesh in allStaticMesh:
        unreal.StaticMeshEditorSubsystem.set_lod_group(mesh, 'LargeProp')