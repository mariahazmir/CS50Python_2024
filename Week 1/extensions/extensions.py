file=input("File name: ").strip().lower().split(".")[-1]

if file in ["gif", "jpeg", "png"]:
    print(f"image/{file}")
elif file == "jpg":
    print(f"image/jpeg")
elif file in ["pdf", "zip"]:
    print(f"application/{file}")
elif file == "txt":
    print(f"text/plain")
else:
    print(f"application/octet-stream")
