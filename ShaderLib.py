import bpy
bl_info = {
    "name": "My Addon Name",
    "description": "Description of this addon",
    "author": "Authors name",
    "version": (0, 0, 1),
    "blender": (2, 9, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Object"}


class ShaderAddPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Shader Add Panel"
    bl_idname = "SHADER_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Shader Libary"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text='添加着色器')
        row.operator("")


class SHADER_OT_DIAMOND(bpy.types.Operator):
    bl_label = "Diamond"
    bl_idname = "shader.diamond_operator"

    def execute(self, context):
        # Creating a New Shader,Calling it Diamond
        material_diamond = bpy.data.meterials.new(name="Diamond")
        # 新建一个名为Diamond的材质球
        material_diamond.use_nodes = True
        # 使用材质球
        # 移除principled bsdf
        material_diamond.node_tree.nodes.remove(
            material_diamond.node_tree.nodes.get('Principled BSDF'))
        material_output = material_diamond.node_tree.nodes.get(
            'Material Output')
        material_output.location(-400, 0)
        grass1_node = material_diamond.node_tree.nodes.add(
            'ShaderNodeBsdfGlass')
        grass1_node.location = (-600, 0)


def register():
    bpy.utils.register_class(ShaderAddPanel)


def unregister():
    bpy.utils.unregister_class(ShaderAddPanel)


if __name__ == "__main__":
    register()
