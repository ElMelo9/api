from supabase_connection import supabase_client

def create_role(table_name, data):
    response, error = supabase_client.table(table_name).upsert(data).execute()
    if error:
        return error
    return response

def get_records(table_name):
    response, error = supabase_client.table(table_name).select().execute()
    if error:
        return error
    return response



