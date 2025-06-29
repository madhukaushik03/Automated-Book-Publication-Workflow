

import os

# Load AI-spun content
with open("chapter1_spun_by_ai.txt", "r", encoding="utf-8") as f:
    ai_text = f.read()

# Display to user
print("Here is the AI version:")
print("="*50)
print(ai_text[:1000])  # Just show a part if it's long
print("...\n")
print("="*50)

print(" Now enter your edits (or press Enter to keep as-is):")
print(" You can paste your new version or leave it empty to skip.")

# Take user edits
user_input = input("\nPaste your edited version:\n\n")

# Use human version if edited
if user_input.strip():
    final_version = user_input
    with open("chapter1_human_edited.txt", "w", encoding="utf-8") as f:
        f.write(final_version)
    print(" Saved your edited version as 'chapter1_human_edited.txt'")
else:
    print(" No changes made. Proceeding with AI version.")
