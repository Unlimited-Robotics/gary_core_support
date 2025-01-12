import os

# Path to your project folder
project_path = "../project_files"
output_file = "combined_project.py"
this_file = "make_all_one_file.py"
def get_import_file(importline):
    start = ""
    if ("from" in importline):
        start = importline.split("import")[0]
        # print(importline)
        start = start.split("from")[1]
        # print(importline)

        start = start.strip()
    else:
        start = importline.split("import")[1]
        start = start.strip()
    return start



with open(output_file, "w") as outfile:
    imports_list = []
    imports_after_thing_list = []
    imports_names_only = []
    output_lines = []
    main_lines = []
    file_names = []
    for file_name in os.listdir(project_path):
        if file_name.endswith(".py"):
            # print(file_name)
            if (output_file in file_name or this_file in file_name or "qt_design1" in file_name):
                # print("skipped")
                continue
            file_names.append(file_name.replace(".py",""))
            file_path = os.path.join(project_path, file_name)
            with open(file_path, "r") as infile:
                # Write a comment indicating the file's origin
                if ("main.py" in file_name):
                    main_lines.append(f"# Start of {file_name}\n")
                    for line in infile.read().split("\n"):
                        main_lines.append(line + "\n")
                    main_lines.append(f"\n# End of {file_name}\n\n")
                else:
                    output_lines.append(f"# Start of {file_name}\n")
                    for line in infile.read().split("\n"):
                        output_lines.append(line+"\n")
                    output_lines.append(f"\n# End of {file_name}\n\n")
    for line in output_lines:
        if "import" in line:

            imports_list.append(line)
    # print(os.listdir(project_path))
    for importline in imports_list:
        # print(get_import_file(importline))
        if ((get_import_file(importline)+".py") in os.listdir(project_path)):
            continue
        imports_names_only.append(get_import_file(importline))
        imports_after_thing_list.append(importline.strip()+"\n")
    for line in imports_after_thing_list:
        outfile.write(line)
    outfile.write("from sys import platform\n")
    outfile.write("from PyQt5.QtCore import QObject, QThread, pyqtSignal\n")
    outfile.write("from PyQt5 import QtWidgets\n")
    outfile.write("from qt_design1 import Ui_qt_designer_save1\n")

    for line in output_lines:
        if not ("import" in line):
            outfile.write(line)
    for line in main_lines:
        if not ("import" in line):
            outfile.write(line)

print(f"All .py files combined into {output_file}")