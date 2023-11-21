file_name = input("")

if file_name.endswith(".gif"):
    media_type = "image/gif"
elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
    media_type = "image/jpeg"
elif file_name.endswith(".pdf"):
    media_type = "application/pdf"
elif file_name.endswith(".txt"):
    media_type = "txt/plain"
elif file_name.endswith(".zip"):
    media_type = "application/zip"
else:
    media_type = "application/octet-system"

print("File name: " + media_type)