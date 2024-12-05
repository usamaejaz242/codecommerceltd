# Paths for the uploaded files
bootstrap_path = r"D:\USAMA\Others\codecommerceltd\aaa\bootstrap_660000.css"
style_path = r"D:\USAMA\Others\codecommerceltd\aaa\style_660000.css"

# Reading the files
with open(bootstrap_path, "r") as bootstrap_file:
    bootstrap_content = bootstrap_file.read()

with open(style_path, "r") as style_file:
    style_content = style_file.read()

# professional_color = "#2E2E2E"
professional_color = "#013220"  # Dark Forest Green
# professional_color = "#2B2D42"  # Dark Charcoal


# Replace all instances of #660000 with the professional color
bootstrap_updated = bootstrap_content.replace("#660000", professional_color)
style_updated = style_content.replace("#660000", professional_color)

# Paths for the modified files
bootstrap_modified_path = r"D:\USAMA\Others\codecommerceltd\css\bootstrap.css"
style_modified_path = r"D:\USAMA\Others\codecommerceltd\css\style.css"

# Writing the updated content to new files
with open(bootstrap_modified_path, "w") as bootstrap_file:
    bootstrap_file.write(bootstrap_updated)

with open(style_modified_path, "w") as style_file:
    style_file.write(style_updated)

bootstrap_modified_path, style_modified_path
