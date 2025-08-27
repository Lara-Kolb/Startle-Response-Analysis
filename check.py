import os
import filecmp

backup_dir = "backup"
results_dir = "Peakfinder Results"

# List files in both directories
backup_files = set(os.listdir(backup_dir))
results_files = set(os.listdir(results_dir))

# Compare file lists
print("Files only in backup:", backup_files - results_files)
print("Files only in results:", results_files - backup_files)
print("Files in both:", backup_files & results_files)

# Compare contents of files present in both
for filename in backup_files & results_files:
    backup_path = os.path.join(backup_dir, filename)
    results_path = os.path.join(results_dir, filename)
    same = filecmp.cmp(backup_path, results_path, shallow=False)
    print(f"{filename}: {'SAME' if same else 'DIFFERENT'}")