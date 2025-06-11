# import os
# import json

# # Sample chapter/section structure (normally you'd load this from a file)
# chapters = [ 
#     {
#         "title": "Chapter 1 General Provisions",
#         "dir": "chapter_1",
#         "file": "",
#         "sections": [
#             {
#                 "title": "§ 27.02.010 TITLE.",
#                 "file": "1.1",
#                 "section": []
#             },
#             {
#                 "title": "§ 27.02.020 INTENT—PURPOSE.",
#                 "file": "1.2",
#                 "section": []
#             }
#             # Add the rest of the sections...
#         ]
#     },
#     {
#         "title": "Chapter 15 Two-Unit Development Residential Overlay District – R1 Districts",
#         "dir": "chapter_15",
#         "file": "",
#         "sections": [
#             {
#                 "title": "§ Article I Two-Unit Development",
#                 "file": "15.1",
#                 "section": []
#             }
#         ]
#     }
#     # Add more chapters...
# ]

# # Placeholder function: replace with actual logic to get section content
# def get_section_content(section_title, section_file):
#     # You should replace this with actual data retrieval logic
#     return {
#         "source": "ecode",
#         "title": section_title,
#         "url": "https://example.com/section/" + section_file,
#         "html": "<div>Placeholder HTML content for {}</div>".format(section_title)
#     }

# # Base directory to store chapters
# base_dir = "output_law_data"

# # Create directories and files
# for chapter in chapters:
#     chapter_dir = os.path.join(base_dir, chapter["dir"])
#     os.makedirs(chapter_dir, exist_ok=True)
    
#     for section in chapter["sections"]:
#         section_filename = section["file"] + ".json"
#         section_path = os.path.join(chapter_dir, section_filename)
        
#         section_data = get_section_content(section["title"], section["file"])
        
#         with open(section_path, "w", encoding="utf-8") as f:
#             json.dump(section_data, f, indent=2, ensure_ascii=False)

# print("Chapters and section files generated successfully.")






import os
import json




# === Output directory ===
base_dir = "output_law_data"
os.makedirs(base_dir, exist_ok=True)

# === Create files ===
for chapter in chapters:
    chapter_title = chapter["title"]
    chapter_dir = os.path.join(base_dir, chapter["dir"])
    os.makedirs(chapter_dir, exist_ok=True)

    if chapter_title not in results:
        print(f"Warning: No data for {chapter_title}")
        continue

    chapter_data = results[chapter_title]

    for section in chapter["sections"]:
        heading_clean = section["title"].replace("§", "").strip()

        # Match the heading from results
        match = next((item for item in chapter_data if heading_clean.endswith(item["heading"])), None)
        if not match:
            print(f"Warning: No match for section '{section['title']}'")
            continue

        section_data = {
            "source": "ecode",
            "title": section["title"],
            "url": f"https://library.municode.com{match['id']}",
            "html": f"<div><p>{match['text']}</p></div>"
        }

        filename = section["file"] + ".json"
        file_path = os.path.join(chapter_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(section_data, f, indent=2, ensure_ascii=False)

print("✅ Section files created successfully.")
