from fileinput import filename
from operator import index
import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


def read_some_data(context, filepath, use_some_setting):
    #bpy.context = context
    bpy.context.object.keyframe_insert(data_path="location", frame=0, index=2)
    context.area.type = "GRAPH_EDITOR"
    bpy.ops.graph.sound_bake(filepath=filepath)

    return {'FINISHED'}

class AvizToolPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Audio Viz Tools"
    bl_idname = "OBJECT_PT_aviz"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Keyframe")

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        row = layout.row()
        row.label(text="Selected Audio")
        
        row = layout.row()
        row.operator(ImportAudioSeg.bl_idname)


class ImportAudioSeg(Operator, ImportHelper):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Apply"
    bl_context = "scene"
    bl_idname = "import_test.some_data"

    # ImportHelper mixin class uses this
    filename_ext = ".wav"

    filter_glob: StringProperty(
        default="*.wav",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    use_setting: BoolProperty(
        name="Example Boolean",
        description="Example Tooltip",
        default=True,
    )

    type: EnumProperty(
        name="Output Format",
        description="Choose output File Format",
        items=(
            ('OPT_A', ".wav", "Description one"),
            ('OPT_B', ".ogg", "Description two"),
        ),
        default='OPT_A',
    )

    def execute(self, context):
        return read_some_data(context, self.filepath, self.use_setting)

def menu_func_import(self, context):
    self.layout.operator(AvizToolPanel.bl_idname, text="Text Import Operator")
    self.layout.operator(ImportAudioSeg.bl_idname, text="Audio Import Helper")

def register():
    bpy.utils.register_class(AvizToolPanel)
    bpy.utils.register_class(ImportAudioSeg)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(AvizToolPanel)
    bpy.utils.unregister_class(ImportAudioSeg)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    


if __name__ == "__main__":
    register()