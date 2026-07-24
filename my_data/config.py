from supabase import create_client
import sys

print("--- FX MASTAR سسٹم ---")
url = input("अपना Supabase URL डालें: ").strip()
key = input("अपनी Supabase Key डालें: ").strip()

try:
    supabase = create_client(url, key)
    print("\n🚀 کامیابی! FX MASTAR سسٹم جڑ گیا ہے۔")
except Exception as e:
    print(f"\n❌ کنکشن میں مسئلہ: {e}")

