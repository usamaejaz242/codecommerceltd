# Paths to the uploaded files
bootstrap_path = "bootstrap__.css"
style_path = "style__.css"

# Reading the files
with open(bootstrap_path, "r") as bootstrap_file:
    bootstrap_content = bootstrap_file.read()

with open(style_path, "r") as style_file:
    style_content = style_file.read()

# # Replacing purple-related color codes with black (#000000)
# bootstrap_modified = bootstrap_content.replace("#6f42c1", "#000000")
# style_modified = style_content.replace("#7335b7", "#000000").replace("#5a2a8f", "#000000")

bootstrap_330000_modified = bootstrap_content.replace("#660000", "#330000")
style_330000_modified = style_content.replace("#660000", "#330000")

# Paths for files with #330000 color
bootstrap_330000_path = "bootstrap_330000.css"
style_330000_path = "style_330000.css"

# Writing the #330000-modified content to new files
with open(bootstrap_330000_path, "w") as bootstrap_file:
    bootstrap_file.write(bootstrap_330000_modified)

with open(style_330000_path, "w") as style_file:
    style_file.write(style_330000_modified)

bootstrap_330000_path, style_330000_path
