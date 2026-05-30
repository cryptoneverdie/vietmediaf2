import os
import hashlib
from xml.etree import ElementTree

repo_dir = r"c:\Users\thien\Documents\vietmediaF2_repo"
addon_xml_path = r"c:\Users\thien\Documents\plugin.video.vietmediaF-11.37.4\plugin.video.vietmediaF2\addon.xml"

# Parse the addon.xml
tree = ElementTree.parse(addon_xml_path)
addon_elem = tree.getroot()

# Create the root <addons> element
addons_root = ElementTree.Element("addons")
addons_root.append(addon_elem)

# Write to addons.xml
addons_xml_path = os.path.join(repo_dir, "addons.xml")
with open(addons_xml_path, "wb") as f:
    f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
    ElementTree.ElementTree(addons_root).write(f, encoding="utf-8", xml_declaration=False)

# Compute MD5
with open(addons_xml_path, "rb") as f:
    content = f.read()
    md5_hash = hashlib.md5(content).hexdigest()

with open(addons_xml_path + ".md5", "w") as f:
    f.write(md5_hash)

print("Created addons.xml and addons.xml.md5")
