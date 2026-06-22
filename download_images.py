import os
import urllib.request

# Create output folder
os.makedirs("cadoa_images", exist_ok=True)

urls = [
    "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1464226184884-fa280b87c399?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1464366400600-7168b8af9bc3?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1500937386664-56d1dfef3854?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1504148455328-c376907d081c?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1509391366360-2e959784a276?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1520340356584-f9917d1eea6f?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1527529482837-4698179dc6ce?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1540575467063-178a50c2df87?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1541888946425-d81bb19240f5?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1555244162-803834f70033?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1556761175-4b46a572b786?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1556910103-1c02745aae4d?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1558317374-067fb5f30001?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1562259949-e8e7689d7828?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1566576721346-d4a3b4eaeb55?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1568844293986-8d0400bd4745?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1576602976047-174e57a47881?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1581244277943-fe4a9c777189?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1593941707882-a5bba14938c7?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1619642751034-765dfdf7c58e?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?auto=format&fit=crop&w=600&h=400",
    "https://images.unsplash.com/photo-1677442135703-1787eea5ce01?auto=format&fit=crop&w=600&h=400",
]

headers = {"User-Agent": "Mozilla/5.0"}

print(f"Downloading {len(urls)} images into 'cadoa_images' folder...\n")

for i, url in enumerate(urls, 1):
    filename = f"cadoa_images/image_{i:02d}.jpg"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(filename, "wb") as f:
            f.write(response.read())
        print(f"[{i:02d}/{len(urls)}] ✅ {filename}")
    except Exception as e:
        print(f"[{i:02d}/{len(urls)}] ❌ Failed: {e}")

print(f"\n✅ Done! All images saved in the 'cadoa_images' folder.")
