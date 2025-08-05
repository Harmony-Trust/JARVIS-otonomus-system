# ?? Supabase Integration
from supabase import create_client

url = "https://your-project.supabase.co"
key = "your-supabase-key"
supabase = create_client(url, key)

def store_payload(table, data):
    response = supabase.table(table).insert(data).execute()
    return response
