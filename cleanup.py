from twelvelabs import TwelveLabs

API_KEY = "{KEY}" 
client = TwelveLabs(api_key=API_KEY)

def cleanup_indexes():
    print("🔍 Fetching all Twelve Labs indexes...")
    
    # Convert the SyncPager generator to a standard Python list
    indexes = list(client.indexes.list())
    
    if not indexes:
        print("✅ No indexes found. Your account space is fully cleared!")
        return
        
    print(f"Found {len(indexes)} index(es). Commencing cleanup...")
    print("-" * 50)
    
    # Iterate through and delete each index
    for index in indexes:
        print(f"🗑️ Deleting index: '{index.index_name}' (ID: {index.id})...")
        try:
            client.indexes.delete(index.id)
            print("   ↳ Success.")
        except Exception as e:
            print(f"   ↳ ⚠️ Failed to delete: {e}")
            
    print("-" * 50)
    print("✨ Cleanup complete! You now have space to run live multimodal reasoning.")

if __name__ == "__main__":
    cleanup_indexes()
