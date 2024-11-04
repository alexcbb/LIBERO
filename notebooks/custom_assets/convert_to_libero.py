import os
import shutil

def process_folder(base_folder):
    # Go through each object folder
    for folder_name in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder_name)
        
        # Check if it's a folder with the correct format
        if os.path.isdir(folder_path) and "_" in folder_name:
            obj_id, obj_name = folder_name.split("_", 1)
            textured_folder_path = os.path.join(folder_path, "textured")
            
            # Rename 'textured' folder to <obj_name>
            new_folder_path = os.path.join(folder_path, obj_name)
            if os.path.exists(textured_folder_path):
                os.rename(textured_folder_path, new_folder_path)
            
            # Move and rename material_0.png
            move_and_rename_texture(folder_path, new_folder_path, obj_name)
            
            # Update files inside the new <obj_name> folder
            update_material_mtl(new_folder_path, obj_name)
            update_textured_obj(new_folder_path, obj_name)
            update_textured_xml(new_folder_path, obj_name)

def move_and_rename_texture(base_folder_path, textured_folder_path, obj_name):
    texture_file_path = os.path.join(base_folder_path, "material_0.png")
    if os.path.isfile(texture_file_path):
        # Move and rename to <obj_name>.png
        new_texture_path = os.path.join(textured_folder_path, f"{obj_name}.png")
        shutil.move(texture_file_path, new_texture_path)

def update_material_mtl(folder_path, obj_name):
    mtl_file_path = os.path.join(folder_path, "material.mtl")
    if os.path.isfile(mtl_file_path):
        with open(mtl_file_path, "r") as file:
            lines = file.readlines()
        
        # Replace 'material_0' in the first and last line with <obj_name>
        if lines:
            lines[0] = lines[0].replace("material_0", obj_name)
            if len(lines) > 1:
                lines[-1] = lines[-1].replace("material_0", obj_name)

        with open(mtl_file_path, "w") as file:
            file.writelines(lines)

def update_textured_obj(folder_path, obj_name):
    obj_file_path = os.path.join(folder_path, "textured.obj")
    new_obj_file_path = os.path.join(folder_path, f"{obj_name}.obj")
    
    if os.path.isfile(obj_file_path):
        with open(obj_file_path, "r") as file:
            lines = file.readlines()
        
        # Replace 'material.mtl' with <obj_name>.mtl in the first two lines
        # Replace 'material_0' with <obj_name> in the second line
        if len(lines) >= 2:
            lines[0] = lines[0].replace("material.mtl", f"{obj_name}.mtl")
            lines[1] = lines[1].replace("material.mtl", f"{obj_name}.mtl")
            lines[1] = lines[1].replace("material_0", obj_name)

        # Write to new file with updated name
        with open(new_obj_file_path, "w") as file:
            file.writelines(lines)
        
        # Remove the old 'textured.obj' file
        os.remove(obj_file_path)

def update_textured_xml(folder_path, obj_name):
    xml_file_path = os.path.join(folder_path, "textured.xml")
    new_xml_file_path = os.path.join(folder_path, f"{obj_name}.xml")
    
    if os.path.isfile(xml_file_path):
        with open(xml_file_path, "r") as file:
            xml_content = file.read()
        
        # Replace content in the XML file as specified
        new_xml_content = f'''<mujoco model="{obj_name}">
  <default>
    <default class="visual">
      <geom group="1" type="mesh" contype="0" conaffinity="0"/>
    </default>
    <default class="collision">
      <geom group="0" type="mesh"/>
    </default>
  </default>
  <asset>
    <texture type="2d" name="{obj_name}" file="{obj_name}.png"/>
    <material name="{obj_name}" texture="{obj_name}" specular="0.4000000000000001" shininess="0.001"/>
    <mesh name="{obj_name}" file="{obj_name}.obj"/>
  </asset>
  <worldbody>
    <body>
    <body name="object">
      <geom material="{obj_name}" mesh="{obj_name}" class="visual"/>
      <geom mesh="{obj_name}" class="collision"/>
    </body>
      <site rgba="0 0 0 0" size="0.005" pos="0 0 -0.04" name="bottom_site" />
      <site rgba="0 0 0 0" size="0.005" pos="0 0 0.04" name="top_site" />
      <site rgba="0 0 0 0" size="0.005" pos="0.005 0.005 0" name="horizontal_radius_site" />
   </body>
  </worldbody>
</mujoco>'''

        # Write to new file with updated name
        with open(new_xml_file_path, "w") as file:
            file.write(new_xml_content)
        
        # Remove the old 'textured.xml' file
        os.remove(xml_file_path)

# Path to the base folder containing all object folders
base_folder = "/home/achapin/Documents/LIBERO/notebooks/custom_assets"
process_folder(base_folder)
