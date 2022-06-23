#from msilib.schema import Icon
import bpy
bl_info = {
    "name": "Object Adder",
    "autor": "wangkan",
    "version": (1, 0),
    "blender": (3, 20, 0),
    "location": "view3d>Tool",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}


class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"
    bl_category = "My 1st Addon"

    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.4
        row = layout.row()
        row.label(text="Add an object")
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon="CUBE")
        row = layout.row()
        row.label(text="Add an uv_sphere")
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", icon="SPHERE")


class PanelA(bpy.types.Panel):
    bl_label = "Scaling"
    bl_idname = "PT_PanelA"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    # bl_category = "Tool"
    bl_category = "My 1st Addon"
    bl_parent_id = "PT_TestPanel"
    bl_optiton = {
        "DEFAULT_CLOSED"

    }

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.label(text="select a object to scale", icon="FONT_DATA")
        row = layout.row()
        row.operator("transform.resize")
        layout.scale_y = 1.4
        col = layout.column()
        col.prop(obj, "scale")


class PanelB(bpy.types.Panel):
    bl_label = "PanelB"
    bl_idname = "PT_PanelB"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    # bl_category = "Tool"
    bl_category = "My 1st Addon"
    bl_parent_id = "PT_TestPanel"
    bl_optiton = {
        "DEFAULT_CLOSED"

    }

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="This Is PanelB", icon="COLOR_BLUE")
        row = layout.row()
        row.operator("object.shade_smooth")
        row = layout.row()
        row.operator("object.subdivision_set")
        row = layout.row()
        row.operator("object.modifier_add")


def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)


def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(PanelB)


if __name__ == "__main__":
    register()
