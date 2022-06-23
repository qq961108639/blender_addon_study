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
        row.operator("shader.diamond_operator")


# 钻石材质
class SHADER_OT_DIAMOND(bpy.types.Operator):
    bl_label = "Diamond"
    bl_idname = "shader.diamond_operator"

    def execute(self, context):
        # Creating a New Shader,Calling it Diamond
        material_diamond = bpy.data.materials.new(name="Diamond")
        # 新建一个名为Diamond的材质球
        material_diamond.use_nodes = True
        # 使用材质球
        # 移除principled bsdf
        material_diamond.node_tree.nodes.remove(
            material_diamond.node_tree.nodes.get('Principled BSDF'))
        material_output = material_diamond.node_tree.nodes.get(
            'Material Output')
        # set location of node
        material_output.location = (1262, 208)
        # Adding Glass1 Node
        grass1_node = material_diamond.node_tree.nodes.new(
            'ShaderNodeBsdfGlass')
        # set  Location of Node
        grass1_node.location = (-600, 0)
        # Setting the Default Color
        grass1_node.inputs[0].default_value = (1, 0, 0, 1)
        # Setting the Default IOR Value
        grass1_node.inputs[2].default_value = 1.446

        # Adding Glass2 Node
        grass2_node = material_diamond.node_tree.nodes.new(
            'ShaderNodeBsdfGlass')
        # set  Location of Node
        grass2_node.location = (-600, -150)
        # Setting the Default Color
        grass2_node.inputs[0].default_value = (0, 1, 0, 1)
        # Setting the Default IOR Value
        grass2_node.inputs[2].default_value = 1.450

        # Adding Glass3 Node
        grass3_node = material_diamond.node_tree.nodes.new(
            'ShaderNodeBsdfGlass')
        # set  Location of Node
        grass3_node.location = (794, 142)
        # Setting the Default Color
        grass3_node.inputs[0].default_value = (0, 1, 0, 1)
        # Setting the Default IOR Value
        grass3_node.inputs[2].default_value = 1.450

        # Adding Glass4 Node
        grass4_node = material_diamond.node_tree.nodes.new(
            'ShaderNodeBsdfGlass')
        # set  Location of Node
        grass4_node.location = (854, 166)
        # Setting the Default Color
        grass4_node.inputs[0].default_value = (1, 1, 1, 1)
        # Setting the Default IOR Value
        grass4_node.inputs[2].default_value = 1.450

        add1_node = material_diamond.node_tree.nodes.new("ShaderNodeAddShader")
        add1_node.location = (646, 392)
        add1_node.label = "Add 1"
        add1_node.hide = True
        add1_node.select = False

        add2_node = material_diamond.node_tree.nodes.new("ShaderNodeAddShader")
        add2_node.location = (948, 126)
        add2_node.label = "Add 2"
        add2_node.hide = True
        add2_node.select = False

        mix1_node = material_diamond.node_tree.nodes.new("ShaderNodeMixShader")
        mix1_node.location = (1322, 394)
        add1_node.select = False

        # 玻璃节点1 🔗 add1 的1 入口
        material_diamond.node_tree.links.new(
            grass1_node.outputs[0], add1_node.inputs[0])
        # 玻璃节点2 🔗 add1 的2 入口
        material_diamond.node_tree.links.new(
            grass2_node.outputs[0], add1_node.inputs[1])
        # add1的出口1 🔗  add2的 入口1
        material_diamond.node_tree.links.new(
            add1_node.outputs[0], add2_node.inputs[0])
        # add1的出口1 🔗  add2的 入口1
        material_diamond.node_tree.links.new(
            mix1_node.outputs[0], material_output.inputs[0])
        # add2的出口1 🔗  glass4的 出口1
        material_diamond.node_tree.links.new(
            add2_node.outputs[0], mix1_node.inputs[1])
        material_diamond.node_tree.links.new(
            grass4_node.outputs[0], mix1_node.inputs[2])

        material_diamond.node_tree.links.new(
            grass3_node.outputs[0], add2_node.inputs[1])

        material_diamond.node_tree.links.new(
            mix1_node.outputs[0], material_output.inputs[0]
        )

        bpy.context.object.active_material = material_diamond

        return{
            "完成"
        }
# 钻石材质结束
# 明天开始


def register():
    bpy.utils.register_class(ShaderAddPanel)
    bpy.utils.register_class(SHADER_OT_DIAMOND)


def unregister():
    bpy.utils.unregister_class(ShaderAddPanel)
    bpy.utils.unregister_class(SHADER_OT_DIAMOND)


if __name__ == "__main__":
    register()
