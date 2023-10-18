from supabase_connection import supabase_client

# Define el nombre de la tabla de la que deseas recuperar registros
table_name = 'usuarios'

# Realiza una consulta para recuperar registros de la tabla
response, error = supabase_client.table(table_name).select().execute()

if error:
    print(f"Error al realizar la consulta: {error}")
else:
    data = response.json()
    print(f"Registros de la tabla {table_name}: {data}")
