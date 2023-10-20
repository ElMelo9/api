from supabase_connection import supabase_client


data = supabase_client.table("roles").select('id_rol','nombre_rol').execute()
# Assert we pulled real data.
assert len(data.data) > 0
print(data)
